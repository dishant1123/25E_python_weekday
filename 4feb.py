# pip install mysql-connector-python 

import mysql.connector 

conn = mysql.connector.connect(
    host="localhost",
    port=3306,
    user="root",
    password="root",
    database="25_MWF_python",
)

cursor = conn.cursor()

# create database   ==> create database database_name
# cursor.execute("CREATE DATABASE IF NOT EXISTS 25_MWF_python")
# print("database created successfully")

# cursor.execute("""
#                CREATE TABLE IF NOT EXISTS student(
#                    id INT  AUTO_INCREMENT PRIMARY KEY,
#                    name VARCHAR(50),
#                    age INT,
#                    department VARCHAR(50)
#                )
#                """)
# print("table created successfully")

cursor.execute("INSERT INTO student(name,age,department) Values('Krishna',21,'Computer')")
cursor.execute("INSERT INTO student(name,age,department) Values('Krish',20,'HR')")
cursor.execute("INSERT INTO student(name,age,department) Values('Aashta',22,'Developer')")
cursor.execute("INSERT INTO student(name,age,department) Values('Urja',25,'Finance')")
cursor.execute("INSERT INTO student(name,age,department) Values('Yash',19,'Sales')")

conn.commit()
print("data inserted successfully")
cursor.close()
conn.close()
