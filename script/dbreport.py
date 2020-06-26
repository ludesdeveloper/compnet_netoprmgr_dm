import sqlite3

class dbreport:
    def __init__(self):
        #destroy table summarytable
        try:
            db = sqlite3.connect('pmdb')
            cursor = db.cursor()
            cursor.execute('''DROP TABLE swsumtable''')
            db.commit()
            db.close()
        except:
            pass
        try:
            db = sqlite3.connect('pmdb')
            cursor = db.cursor()
            cursor.execute('''DROP TABLE swtable''')
            db.commit()
            db.close()
        except:
            pass
        try:
            db = sqlite3.connect('pmdb')
            cursor = db.cursor()
            cursor.execute('''DROP TABLE hwsumtable''')
            db.commit()
            db.close()
        except:
            pass
        try:
            db = sqlite3.connect('pmdb')
            cursor = db.cursor()
            cursor.execute('''DROP TABLE hwcardtable''')
            db.commit()
            db.close()
        except:
            pass
        try:
            db = sqlite3.connect('pmdb')
            cursor = db.cursor()
            cursor.execute('''DROP TABLE cpusumtable''')
            db.commit()
            db.close()
        except:
            pass
        try:
            db = sqlite3.connect('pmdb')
            cursor = db.cursor()
            cursor.execute('''DROP TABLE memsumtable''')
            db.commit()
            db.close()
        except:
            pass
        try:
            db = sqlite3.connect('pmdb')
            cursor = db.cursor()
            cursor.execute('''DROP TABLE envtable''')
            db.commit()
            db.close()
        except:
            pass
        try:
            db = sqlite3.connect('pmdb')
            cursor = db.cursor()
            cursor.execute('''DROP TABLE logtable''')
            db.commit()
            db.close()
        except:
            pass
        #open db connection to table summary table
        try:
            db = sqlite3.connect('pmdb')
            cursor = db.cursor()
            cursor.execute('''
                CREATE TABLE swsumtable(id INTEGER PRIMARY KEY, version TEXT)                    
            ''')
            db.close()
        except:
            pass
        try:
            db = sqlite3.connect('pmdb')
            cursor = db.cursor()
            cursor.execute('''
                CREATE TABLE swtable(id INTEGER PRIMARY KEY, devicename TEXT,
                model TEXT, iosversion TEXT, uptime TEXT, confreg TEXT)                    
            ''')
            db.close()
        except:
            pass
        try:
            db = sqlite3.connect('pmdb')
            cursor = db.cursor()
            cursor.execute('''
                CREATE TABLE hwsumtable(id INTEGER PRIMARY KEY, model TEXT)                    
            ''')
            db.close()
        except:
            pass
        try:
            db = sqlite3.connect('pmdb')
            cursor = db.cursor()
            cursor.execute('''
                CREATE TABLE hwcardtable(id INTEGER PRIMARY KEY, devicename TEXT,
                model TEXT, card TEXT, slot TEXT, sn TEXT, hwdscr TEXT)                    
            ''')
            db.close()
        except:
            pass
        try:
            db = sqlite3.connect('pmdb')
            cursor = db.cursor()
            cursor.execute('''
                CREATE TABLE cpusumtable(id INTEGER PRIMARY KEY, devicename TEXT,
                model TEXT, total TEXT, process TEXT, interrupt TEXT, topcpu TEXT, status TEXT)                    
            ''')
            db.close()
        except:
            pass
        try:
            db = sqlite3.connect('pmdb')
            cursor = db.cursor()
            cursor.execute('''
                CREATE TABLE memsumtable(id INTEGER PRIMARY KEY, devicename TEXT,
                model TEXT, utils TEXT, topproc TEXT, status TEXT)                    
            ''')
            db.close()
        except:
            pass
        try:
            db = sqlite3.connect('pmdb')
            cursor = db.cursor()
            cursor.execute('''
                CREATE TABLE envtable(id INTEGER PRIMARY KEY, devicename TEXT,
                                system TEXT, item TEXT, status TEXT)
            ''')
            db.close()
        except:
            pass
        try:
            db = sqlite3.connect('pmdb')
            cursor = db.cursor()
            cursor.execute('''
                CREATE TABLE logtable(id INTEGER PRIMARY KEY, devicename TEXT, model TEXT, script TEXT)
            ''')
            db.close()
        except:
            pass
