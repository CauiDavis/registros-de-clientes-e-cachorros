from configurações.database import database

class cachorroDAO:
    def __init__(self):
        pass
    def registrar(self,cachorro):
        bd = database().conectar()
        cursor = bd.cursor()
        script = ("insert into Cachorro(nome,idade) values('"+cachorro.get_nome()+"','"+cachorro.get_idade()+"')")
        cursor.execute(script)
        bd.commit()
        print("cachorro foi cadastrado")
    def deletar_cachorro(self,id):
        bd = database().conectar()
        cursor = bd.cursor()
        cursor.execute("delete from Cachorro where idCachorro="+id)
        bd.commit()
        print("cachorro foi excluído")
    def listar(self):
        bd = database().conectar()
        cursor = bd.cursor()
        cursor.execute("select* from Cachorro")
        resultado = cursor.fetchall()
        print("listagem feita")
        return resultado
    def buscar_cachorro(self,id):
        bd = database().conectar()
        cursor = bd.cursor()
        cursor.execute("select* from Cachorro where idCachorro="+id)
        resultado = cursor.fetchone()
        print("cachorro encontrado")
        return resultado