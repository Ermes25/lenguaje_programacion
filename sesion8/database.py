import mysql.connector
#la importancion de la libreria OS o Operative System fundamenta los usos y las funciones de la Terminal ya sea Windows o Linux
import os
#La clase MYSQLDB fundamentara el inicio de los parametros de nuestra base de datos que utilizaremos
class MYSQLDB:
    #la definicion o el primer metodo lo utilizaremos para la interfaz o el arranque de nuestra base de datos que nos asegura
    #relacionar no solo en nuestra base datos si no que tambien en otros usuarios que necesitan usarlo 
    def __init__(self,host,user,password,database):
        self.host = host
        self.user = user
        self.pw = password
        self.db = database   
        self.connection = None     
    #el segundo metodo es una herencia que permite conectar el usuario con la base de datos            
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
    #El tercer metodo tambien es una herencia que me permite usuario desconectarse desde el editor de Codigo
    def disconect(self):
        try:
             if self.connection:
                    self.connection.close
                    self.connection = None
        except mysql.connector.Error as error:
            print("Error")
    #El cuarto metodo no solo permite presentar las peticion del usuario si no que tambien encapsula los demas metodos permitiendo al usuario
    #usar solo una peticion de manera automatica reduciendo la cantidad de espera de codigos
    def execute_query(self,query,params=None):
        try:
            cursor = self.connection.cursor()
            cursor.execute(query,params)
            result = cursor.fetchall()
            return result
        except mysql.connector.Error as err:
            print(f"Error: {err}")
db =MYSQLDB("localhost","root","","testlp")
print("conectado")

db.connect()
categorias = db.execute_query("select * from categorias")
for reg in categorias:
    print(categorias)