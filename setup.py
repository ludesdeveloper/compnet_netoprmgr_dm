import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="netoprmgr_dm", # Replace with your own username
    version="1.2.0",
    author="Funguardian, Dedar, Luthfi",
    author_email="cristiano.ramadhan@gmail.com",
    description="Project to Manage Network Operation.",
    long_description="Project to Manage Network Operation.\nType 'python -m netoprmgr_dm.__main__' to run program.\nNow using flask",
    long_description_content_type="text/markdown",
    url="https://github.com/FunGuardian/netoprmgr_dm",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
    install_requires=[
        'netmiko==3.1.0',
        'xlrd==1.2.0',
        'XlsxWriter==1.2.8',
        'python-docx==0.8.10',
        'Flask==1.1.2',
        'Flask-SQLAlchemy==2.4.1',
        'Flask-Bcrypt==0.7.1',
        'Flask-Login==0.5.0',
        'Flask-WTF==0.14.3',
        'Werkzeug==1.0.1',
    ],
    include_package_data=True
)