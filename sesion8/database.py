import mysql.connector
import os

class MYSQLDB:
    def __init__(self,host,user,password,database):
        self.host = host
        self.user = user
        self.pw = password
        self.db = database   
        self.Connection = None     
                
    def connect(self):
        try:
            if(self.connect == None):
                self.Connection = mysql.connector.connect(
                    host = self.host,
                    user = self.user,
                    password = self.pw,
                    database = self.db
                )
                print("Congratulations")
        except mysql.connector.Error as error:
            print("Error mientras se estaba conectando {}".format(error))
    def disconect(self):
        try:
             if self.Connection:
                    self.Connection.close
                    self.Connection = None
        except mysql.connector.error as Error:
            print("Error")
    def execute_query(self,query,params = None):
        try:
            cursor = self.Connection.cursor
            cursor.execute(query,params)
            result = cursor.fetchall()
            return result
        except mysql.connector.Error as err:
            print(f"error: {err}")
db =MYSQLDB("localhost","root","","testlp")
print("conectado")

db.connect()
categorias = db.execute_query("select * from categorias")
print(categorias)