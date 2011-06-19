'''
Created on 16/02/2011

@author: Karolyne
'''

from Micro import Micro
from DataHoraAtual import dataHoraAtual

class Estacao(Micro):
    todasEstacoes = []
    achou = True
    achouUsuarioConectado = True
    
    def __init__(self, codPatrimonio, descricao, hd, memoria, localizacao):
        Micro.__init__(self, codPatrimonio, descricao, hd, memoria)
        self.localizacao = localizacao
        self.usuario = ""
        self.dataHoraAtualdaConexao = dataHoraAtual()
        self.armazenaEstacoes(self)
        
    def armazenaEstacoes(self, estacao):
        self.todasEstacoes.append(estacao)
        
    def defineUsuarioAtivoemUmaEstacao(self, posicao, usuario):
        opcao = raw_input("Deseja associar um usuario a esta estacao(sim/nao): ")
        
        while opcao.lower() != "nao":
            nomedoUsuario = raw_input("Infome o nome do usuario: ")
            achou = self.verificarUsuarioCadastrado(nomedoUsuario, usuario)
            
            if achou == True:
                achouUsuarioConectado = self.verificaseUsuarioestaConectadonaEstacao(nomedoUsuario)
                if achouUsuarioConectado == False:
                    self.todasEstacoes[posicao].usuario = nomedoUsuario
                    print "Usuario conectado a estacao com sucesso!"
                else:
                    print "O usuario ja esta conectado a uma estacao!"
            else:
                print "Nao foi possivel conectar o usuario a estacao, pois o mesmo nao esta cadastrado!"
            opcao = raw_input("Deseja associar um usuario a esta estacao(sim/nao): ")           
            
    def verificarUsuarioCadastrado(self, nome, usuario):
        for i in range(len(usuario.todosUsuarios)):
            if usuario.todosUsuarios[i].nomeGuerra == nome:
                achou = True
                break
            else:
                achou = False
        return achou
    
    def verificaseUsuarioestaConectadonaEstacao(self, nome):
        for i in range(len(self.todasEstacoes)):
            if self.todasEstacoes[i].usuario == nome:
                achouUsuarioConectado = True         
                break
            else:
                achouUsuarioConectado = False
        return achouUsuarioConectado  
            