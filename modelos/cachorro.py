
class cachorro:
    def __init__(self,id,nome,idade,idcliente):
        self.id = id
        self.nome = nome
        self.idade = idade
        self.idcliente = idcliente
    def get_id(self):
        return self.id
    def get_nome(self):
        return self.nome
    def get_idade(self):
        return self.idade
    def get_idcliente(self):
        return self.idcliente