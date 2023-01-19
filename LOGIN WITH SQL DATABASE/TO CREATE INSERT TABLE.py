import sqlite3
db=sqlite3.connect('adi.db')
cr=db.cursor()
cr.execute("""create table ins(RollNo text,
          Name text,
         PHY_Marks text,
        CHE_Marks text,
       Maths_Marks text)""")
db.commit()
db.close()
print('Table create')
