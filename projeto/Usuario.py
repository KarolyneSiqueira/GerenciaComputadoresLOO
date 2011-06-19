'''
Created on 12/02/2011

@author: Karolyne
'''
class Usuario():
    todosUsuarios = []
    
    def __init__(self, nomeGuerra, senha):
        self.nomeGuerra = nomeGuerra
        self.senha = senha
        self.armazenaUsuarios(self)
        #self.cadastraUsuarios()
        
    def armazenaUsuarios(self, usuario):
        self.todosUsuarios.append(usuario)