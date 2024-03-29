"""MySQL class with select and update methods"""

import mysql.connector
class MySQL_DB:
    def __init__(self, database, password, host='localhost', user='root', port='3306'):
        self.host = host
        self.user = user
        self.password = password
        self.port = port
        self.database = database

    def connect(self):
        my_db = mysql.connector.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            port=self.port,
            database=self.database
        )
        return my_db

    def execute(self, query):
        my_db = self.connect()
        my_cursor = my_db.cursor()
        my_cursor.execute(query)
        table_name = my_cursor.fetchall()
        for value in table_name:
            print(value)

    def commit(self, query):
        my_db = self.connect()
        my_cursor = my_db.cursor()
        my_cursor.execute(query)
        return my_db.commit()

