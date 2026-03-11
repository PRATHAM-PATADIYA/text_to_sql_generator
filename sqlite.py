import sqlite3

# Connect to the SQLite database 
connection = sqlite3.connect('student.db')

# Create a cursor object to execute SQL commands
cursor = connection.cursor()

# create a table
table_info="""
Create table STUDENT(NAME VARCHAR(25), CLASS VARCHAR(25), SECTION VARCHAR(25), MARKS INT);
"""
cursor.execute(table_info)

# Insert some data into the table

cursor.execute('''INSERT INTO STUDENT VALUES ('Krish', 'Data Science', 'A', 90)''')
cursor.execute('''INSERT INTO STUDENT VALUES ('Sudhanshu', 'Data Science', 'B', 85)''')
cursor.execute('''INSERT INTO STUDENT VALUES ('Parth', 'Data Science', 'A', 88)''')
cursor.execute('''INSERT INTO STUDENT VALUES ('Kamo', 'DEVOPS', 'A', 92)''')
cursor.execute('''INSERT INTO STUDENT VALUES ('Neel', 'DEVOPS', 'A', 87)''')

# Display all the records in the table

print("The inserted records are:")
data = cursor.execute('''SELECT * FROM STUDENT;''')
for row in data:
    print(row)

# Commit the changes into database

connection.commit()
connection.close()