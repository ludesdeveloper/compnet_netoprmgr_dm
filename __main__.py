import os
import sys
import shutil
import time
from datetime import datetime
import pkg_resources
import json
import urllib.request
from werkzeug.utils import secure_filename
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField
from wtforms.validators import DataRequired, Length, EqualTo, ValidationError
from flask import Flask, render_template, send_file, flash, request, redirect, Response
from flask_login import (login_user, current_user, logout_user,
						login_required, LoginManager, UserMixin)
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_wtf import FlaskForm

#FLASK CONFIGURATION
app = Flask(__name__)
app.config['SECRET_KEY'] = 'a35ca9f60ead933ddcbf093ed5a92296'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'
#DATABASE
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)

    def __repr__(self):
        return f"User('{self.username}')"
#DIRECTORY
BASE_DIR = pkg_resources.resource_filename('netoprmgr_dm', '')
os.chdir(BASE_DIR)
CAPT_DIR = os.path.join(BASE_DIR,'static','capture')
DATA_DIR = os.path.join(BASE_DIR,'static','data')
SCRIPT_DIR = os.path.join(BASE_DIR,'script')
RESULT_DIR = os.path.join(BASE_DIR,'static','result')

ALLOWED_EXTENSIONS_CAPT = set(['txt', 'log'])
ALLOWED_EXTENSIONS_DATA = set(['xlsx',])

app.config['UPLOAD_FOLDER_CAPT'] = CAPT_DIR
app.config['UPLOAD_FOLDER_DATA'] = DATA_DIR

def allowed_file_capt(filename):
	return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS_CAPT

def allowed_file_data(filename):
	return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS_DATA
#FORM
class RegistrationForm(FlaskForm):
    username = StringField('Username',
                           validators=[DataRequired(), Length(min=2, max=20)])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password',
                                     validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('That username is taken. Please choose a different one.')

class LoginForm(FlaskForm):
    username = StringField('Username',
                        validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')
#ROUTE
@app.route("/")
@login_required               
def home():
	chg_dir = os.chdir(SCRIPT_DIR)
	current_dir=os.getcwd()
	read_file = open('file_identification.py','r')
	read_file_list = read_file.readlines()
	for line in read_file_list:
		if '#' not in line and 'except NameError' in line:
			flash('Debug File Identification Still On')
	return render_template('home.html')

@app.route("/about")
def about():
	return render_template('about.html')

@app.route("/register", methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created! You are now able to log in', 'success')
        return redirect('/login')
    return render_template('register.html', title='Register', form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect('/')
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect('/')
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)

@app.route("/logout")
def logout():
    logout_user()
    return redirect('/')

@app.route("/template_generate_page")
@login_required
def template_generate_page():
    return render_template('template_generate_page.html')

@app.route('/template_generate/')
@login_required
def template_generate():
	from main_cli import MainCli
	MainCli.createTemplate()
	return send_file(DATA_DIR+'/template.xlsx', attachment_filename='template.xlsx', as_attachment=True)
	#return redirect('/raw_data/upload')

@app.route("/raw_data/upload")
@login_required
def raw_data_upload_page():
    return render_template('raw_data_upload_page.html')

@app.route('/raw_data/upload', methods=['POST'])
@login_required
def raw_data_upload():
	if request.method == 'POST':
        # check if the post request has the file part
		if 'file' not in request.files:
			flash('No file part')
			return redirect(request.url)
		file = request.files['file']
		if file.filename == '':
			flash('No file selected for uploading')
			return redirect(request.url)
		if file and allowed_file_data(file.filename):
			#filename = secure_filename(file.filename)
			#file.save(os.path.join(app.config['UPLOAD_FOLDER_DATA'], filename))
			file.save(os.path.join(app.config['UPLOAD_FOLDER_DATA'], 'raw_data.xlsx'))
			flash('File successfully uploaded')
			return redirect('/generate_device_data_page')
		else:
			flash('Allowed file type is xlsx')
			return redirect(request.url)

@app.route('/raw_data/result')
@login_required
def raw_download():
	return render_template('raw_data_download.html')

@app.route('/generate_device_data_page')
@login_required
def generate_device_data_page():
	return render_template('generate_device_data_page.html')

@app.route('/generate_device_data')
@login_required
def generate_device_data():
	from main_cli import MainCli
	MainCli.deviceIdentification()
	return redirect('/capture_log_page')

@app.route("/device_data/upload")
@login_required
def device_data_upload_page():
    return render_template('device_data_upload_page.html')

@app.route('/device_data/upload', methods=['POST'])
@login_required
def device_data_upload():
	if request.method == 'POST':
        # check if the post request has the file part
		if 'file' not in request.files:
			flash('No file part')
			return redirect(request.url)
		file = request.files['file']
		if file.filename == '':
			flash('No file selected for uploading')
			return redirect(request.url)
		if file and allowed_file_data(file.filename):
			#filename = secure_filename(file.filename)
			#file.save(os.path.join(app.config['UPLOAD_FOLDER_DATA'], filename))
			file.save(os.path.join(app.config['UPLOAD_FOLDER_DATA'], 'devices_data.xlsx'))
			flash('File successfully uploaded')
			return redirect('/device_data/result')
		else:
			flash('Allowed file type is xlsx')
			return redirect(request.url)

@app.route('/device_data/result')
@login_required
def data_download():
	return render_template('device_data_download.html')


@app.route("/log/upload")
@login_required
def log_upload_page():
    return render_template('log_upload_page.html')

@app.route('/log/upload', methods=['POST'])
@login_required
def log_upload():
	if request.method == 'POST':
        # check if the post request has the files part
		if 'files[]' not in request.files:
			flash('No file part')
			return redirect(request.url)
		files = request.files.getlist('files[]')
		for file in files:
			if file and allowed_file_capt(file.filename):
				filename = secure_filename(file.filename)
				file.save(os.path.join(app.config['UPLOAD_FOLDER_CAPT'], filename))
				print('Uploading '+str(file))
			#flash('Logs successfully uploaded')
		flash(str(len(files))+' logs successfully uploaded')
		return redirect('/log/upload')

@app.route('/capture_log_page')
@login_required
def capture_log_page():
    return render_template('capture_log_page.html')

@app.route('/capture_log')
@login_required
def capture_log():
	from main_cli import MainCli
	MainCli.captureDevice()
	return redirect('/capture_log/download')

@app.route('/command_guide')
@login_required
def command_guide():
    return render_template('command_guide.html')

@app.route('/capture_log/download')
@login_required
def capture_log_download():
	return render_template('capture_log_download.html')

@app.route('/log')
@login_required
def log_delete_page():
	return render_template('log_delete.html')

@app.route('/log/delete')
@login_required
def log_delete():
	from main_cli import MainCli
	MainCli.deleteCapture()
	return redirect('/capture_log_page')

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port='5001')