""" Update in MySQL"""
from mysql_oop import MySQL_DB

q1 = MySQL_DB('northwind', '****')

""" Update And Displayed The Changes """

q1.commit("update orders set ship_name = 'Avi Israeli ' where id = 30")
q1.execute('select ship_name from orders where id = 30')

q1.commit("update orders set ship_name = 'Eli Dasa ' where id = 30")
q1.execute('select ship_name from orders where id = 30')

q1.commit("update orders set ship_name = 'Fasil Maspin ' where id = 30")
q1.execute('select ship_name from orders where id = 30')

q1.commit("update orders set ship_name = 'Natan Mangisto ' where id = 30")
q1.execute('select ship_name from orders where id = 30')

q1.commit("update orders set ship_name = 'Lee Agada ' where id = 30")
q1.execute('select ship_name from orders where id = 30')

