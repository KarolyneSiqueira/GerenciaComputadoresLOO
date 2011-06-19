'''
Created on 15/02/2011

@author: Michael
'''
class Impressora():
    todasImpressoras = []
    
    def __init__(self, codPatrimonio, descricao, velocidade):
        self.codPatrimonio = codPatrimonio
        self.descricao = descricao
        self.velocidade = velocidade
        self.armazenaImpressoras(self)
        
    
    def armazenaImpressoras(self, impressora):
        self.todasImpressoras.append(impressora)
        