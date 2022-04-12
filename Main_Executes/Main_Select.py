from Class_DataBase import DB_Connect


q1 = DB_Connect('localhost', 'root', '*****', '3306', 'sakila')

q1.execute('SELECT * FROM actor')
q1.execute('SELECT * FROM city')
q1.execute('SELECT COUNT(*) FROM actor')
q1.execute('SELECT COUNT(*) FROM city')
q1.execute('SELECT first_name FROM actor')
