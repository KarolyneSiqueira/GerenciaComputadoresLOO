class Usuario():
    todosUsuarios = []
    
    def __init__(self, nomeGuerra, senha):
        self.nomeGuerra = nomeGuerra
        self.senha = senha
        self.armazenaUsuarios(self)
                
    def armazenaUsuarios(self, usuario):
        self.todosUsuarios.append(usuario)
