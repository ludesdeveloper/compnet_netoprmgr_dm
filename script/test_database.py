import sqlite3
db = sqlite3.connect('pmdb')
cursor = db.cursor()
cursor.execute('''SELECT devicename, model, iosversion FROM summarytable''')
records = cursor.fetchall()

for row in records:

    print("Device Name: ", (row[0]))
    print("Model: ",(row[1]))
    print("Ios Version: ",(row[2]))

db.close()

input=input('')



"""cursor.execute('''SELECT devicename, model FROM summarytable WHERE id=?''', (id,))"""