"""Join in MySQL"""

from mysql_oop import MySQL_DB

# Connect To The DataBase
q2 = MySQL_DB('northwind', '******')

# The Queries:
q2.execute('select * from employees as A join employee_privileges as A1 on A.id = A1.employee_id')
q2.execute('select * from orders as O join employees as E on O.employee_id = E.id ')
q2.execute('select * from order_details as O1 join orders as O2 on O1.id = O2.id')
q2.execute("select * from customers as C join orders as O on C.id = O.customer_id where city = 'Las Vegas'")
q2.execute('select * from orders as O join invoices as I on O.id = I.order_id')