import mysql.connector

class DatabaseConnection:
    def __init__(self, host="localhost", username="root", password="root", database="school"):
        self.host = host
        self.username = username
        self.password = password
        self.database = database

    def connect(self):
        connection_mysql = mysql.connector.connect(host=self.host, user=self.username, password=self.password,
                                                   database=self.database)

        cursor = connection_mysql.cursor()
        cursor.execute("SELECT * FROM students")
        result = cursor.fetchall()
        for row_num, row_data in enumerate(result):
            print(row_data)
        return connection_mysql

DatabaseConnection().connect()