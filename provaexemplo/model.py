from hashlib import sha256

class Senha:
    def __init__(self, id, senha, hash):
        self.id = id
        self.senha = senha
        self.hash = hash

senhas = []

def add_senha(senha):
    id = len(senhas) + 1
    nova_senha = Senha(id, senha, sha256(senha.encode()).hexdigest())
    senhas.append(nova_senha)

def delete_senha(id):
    for senha in senhas:
        if senha.id == id:
            senhas.remove(senha)
            return