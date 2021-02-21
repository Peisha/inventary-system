import mysql.connector
from mysql.connector import Error, cursor


class DbConnection:
    def __init__(self):
       self.conn = mysql.connector.connect(host='localhost', database='inventory_system', user='root', password='1234')

       self.cursor = self.conn.cursor()

    def registration(self,query=None,values=None):
       self.cursor.execute(query,values)
       self.conn.commit()

    def login(self,query,values):
        self.cursor.execute(query,values)
        self.a=self.cursor.fetchall()
        return self.a

    def view(self,query):
        self.cursor.execute(query)
        records=self.cursor.fetchall()
        return records
    def search(self,query):
        self.cursor.execute(query)
        records=self.cursor.fetchall()
        return records

    def delete(self,query,values=None):
        self.cursor.execute(query,values)
        self.conn.commit()

    def fetch1(self,query):
        self.cursor.execute(query)
        rows = self.cursor.fetchone()
        return rows

    def update(self,query,values):
        self.cursor.execute(query,values)
        self.conn.commit()

    def select(self,query,values):
        self.cursor.execute(query,values)
        rows = self.cursor.fetchall()
        return rows











