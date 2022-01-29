import mysql.connector
class database:
    def __init__(self):
        self.bd= None
    def conectar(self):
        self.bd =mysql.connector.connect(host="localhost",database="caui",user="root",password="cauidavis")
        print("conexão realizada com sucesso")
        return self.bd
    def desconectar(self):
        self.bd.close()