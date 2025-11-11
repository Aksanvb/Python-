import mysql.connector
mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="sanjay1231",
    database="mysql"
)
mycursor=mydb.cursor()
##mycursor.execute("Show databases;")
##mycursor.execute("""
##Create table students(
##id INT AUTO_INCREMENT PRIMARY KEY,
##name varchar(100),
##age INT
##)
##""")
##print("Table created successfully!")
mycursor=mydb.cursor()
sql="INSERT INTO students(name,age)VALUES(%s,%s)"
students=[
    ("Arun",20),
    ("Bala",21),
    ("Chitra",22),
    ("Deepa",23)
]
mycursor.executemany(sql,students)
mydb.commit()
mycursor.execute("select * from students;")
for row in mycursor:
    print(row)
