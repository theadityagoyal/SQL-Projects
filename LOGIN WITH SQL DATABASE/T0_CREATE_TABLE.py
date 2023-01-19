import sqlite3
db=sqlite3.connect('adi.db')
cr=db.cursor()
cr.execute("create table registration(USERNAME text,USER_PASSWORD text,USER_CONTACT_NUMBER text)")
db.commit()
db.close()
print('Table create')