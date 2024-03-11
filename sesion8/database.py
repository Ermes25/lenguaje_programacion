import mysql.connector
import os

class MYSQLDB:
    def __init__(self,host,user,password,database):
        self.host = host
        self.user = user
        self.pw = password
        self.db = database   
        self.connection = None     
                
    def connect(self):
        try:
            if(self.connection == None):
                self.connection = mysql.connector.connect(
                    host = self.host,
                    user = self.user,
                    password = self.pw,
                    database = self.db
                )
                os.system("color a2")
                print("Congratulations")
        except mysql.connector.Error as error:
            print("Error mientras se estaba conectando {}".format(error))
    def disconect(self):
        try:
             if self.connection:
                    self.connection.close
                    self.connection = None
        except mysql.connector.Error as error:
            print("Error")
    def execute_query(self,query,params=None):
        try:
            cursor = self.connection.cursor()
            cursor.execute(query,params)
            result = cursor.fetchall()
            return result
        except mysql.connector.Error as err:
            print(f"Error: {err}")
db =MYSQLDB("localhost","root","","lacteos_sa")
print("conectado")

db.connect()
categoria = db.execute_query("select * from categoria")
for reg in categoria:
    print(categoria)