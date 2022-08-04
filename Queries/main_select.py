from mysql_oop import MySQL_DB


q1 = MySQL_DB('sakila', '*****')

q1.execute('SELECT * FROM actor')
q1.execute('SELECT * FROM city')
q1.execute('SELECT COUNT(*) FROM actor')
q1.execute('SELECT COUNT(*) FROM city')
q1.execute('SELECT first_name FROM actor')
