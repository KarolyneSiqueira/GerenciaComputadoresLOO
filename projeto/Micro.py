'''
Created on 13/02/2011

@author: Michael
'''

class Micro():  
    todosMicros = []
    
    def __init__(self, codPatrimonio, descricao, hd, memoria):
        self.codPatrimonio = codPatrimonio
        self.descricao = descricao
        self.hd = hd
        self.memoria = memoria
        self.armazenaMicros(self)
    
    def armazenaMicros(self, micro):
        self.todosMicros.append(micro)