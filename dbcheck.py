import sqlite3.3.3
MySchool=sqlite3.connect('schooltest.db')
cursschool=MySchool.cursor()
#cursschool.execute('''CREATE TABLE students (StudentID INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT (20) NOT NULL, house TEXT, marks REAL);''')
cursschool.execute("INSERT INTO students (StudentID, name, house, marks) VALUES (5,'Sherlock',32,50);")
#print(MySchool)
MySchool.close()
