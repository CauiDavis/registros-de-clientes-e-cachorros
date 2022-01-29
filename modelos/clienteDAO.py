from configurações.database import database

class clienteDAO:
    def __init__(self):
        pass

    def registrar1(self,cliente):
        bd = database().conectar()
        script = "insert into Cliente (nome,telefone) values ('"+cliente.get_nome()+"','"+cliente.get_telefone()+"')"
        cursor = bd.cursor()
        cursor.execute(script)
        bd.commit()
        print("cliente foi cadastrado")
    def deletar_cliente(self,id):
        bd = database().conectar()
        cursor = bd.cursor()
        cursor.execute("delete from Cliente where idCliente="+id)
        bd.commit()
        print("cliente foi excluído")
    def listar(self):
        bd = database().conectar()
        cursor = bd.cursor()
        cursor.execute("select* from Cliente")
        resultado = cursor.fetchall()
        print("listagem feita")
        return resultado
    def buscar_cliente(self,id):
        bd = database().conectar()
        cursor = bd.cursor()
        cursor.execute("select * from Cliente where idCliente = "+id)
        resultado = cursor.fetchone()
        print("cliente encontrado")
        return resultado