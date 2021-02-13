import mysql.connector
from mysql.connector import Error, cursor


class DbConnection:
    def __init__(self):
       self.conn = mysql.connector.connect(host='localhost', database='inventory_system', user='root', password='1234')

       self.cursor = self.conn.cursor()

    def registration(self,query,values):
       self.cursor.execute(query,values)
       self.conn.commit()

    def login(self,query,values):
        self.cursor.execute(query,values)
        self.a=self.cursor.fetchall()
        return self.a









