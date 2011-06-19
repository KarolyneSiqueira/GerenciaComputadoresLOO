'''
Created on 16/02/2011

@author: Karolyne
'''

class Impressao():
    todasImpressoes = []
    achouUsuariocomConexaoAtiva = True
    achouImpressoras = True
    achou = True
    
    #def __init__(self, arquivo, usuario, impressora, numeroCopias):
    def __init__(self):
        self.arquivo = ""
        self.usuario = ""
        self.impressora = ""
        self.numeroCopias = ""
        self.armazenaImpressoes(self)
        
    def armazenaImpressoes(self, impressao):
        self.todasImpressoes.append(impressao)
        
    """def realizarImpressao(self, usuario, servidor, impressora, estacao):
        usuarioqueDesejaImprimir = raw_input("Infome o usuario que deseja imprimir: ")
        achouUsuarioConectado = self.achouUsuariocomConexaoAtiva(usuarioqueDesejaImprimir, estacao)
        
        if achouUsuarioConectado == True:
            impressoraaSerUtilizada = raw_input("Informe a impressora desejada: ")
            achouImpressora = self.verificaImpressoraAtivanaEstacaodoUsuario(impressoraaSerUtilizada, servidor)
            
            if achouImpressora == True:
                arquivo = raw_input("Infome o arquivo: ")
                numeroCopias = raw_input("Informe o numero de copias: ")
                #self.todasImpressoes.
        else:
            print "Este usuario nao possui conexao ativa no momento!"
            
    def verificaImpressoraAtivanaEstacaodoUsuario(self, impressoraaSerutilizada, servidor):
        for i in range(len(servidor.todosServidores)):
            if impressoraaSerutilizada in servidor.todosServidores[i].impressora:
                achou = True
            else:
                achou = False
        return achou
        
    def verificarUsuariocomConexaoAtiva(self, usuario, estacao):
        for i in range(len(estacao.todasEstacoes)):
            if estacao.todasEstacoes[i].usuario == usuario:
                achou = True
                break
            else:
                achou = False
        return achou"""
            