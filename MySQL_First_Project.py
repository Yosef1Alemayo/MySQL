import mysql.connector

my_db = mysql.connector.connect(
    host='localhost',
    user='root',
    port='3306',
    password='******',
    database='NORTHWIND'
)

# MySQL:1
my_cuorsor = my_db.cursor()
my_cuorsor.execute('SELECT * FROM employees WHERE job_title = "Sales Representative"')
employees = my_cuorsor.fetchall()

for employee in employees:
    print(employee)

# MySQL:2
my_cuorsor.execute('SELECT * FROM EMPLOYEES')
new_employees = my_cuorsor.fetchall()
for i in new_employees:
    print(i)
