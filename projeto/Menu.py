'''
Created on 15/02/2011

@author: Michael&karolyne
'''
from Estacao import Estacao
from Micro import Micro
from Servidor import Servidor
from Usuario import Usuario
from Impressora import Impressora
from Impressao import Impressao

class Menu():
    def __init__(self):
        self.iniciaMenu()
        
    def iniciaMenu(self):      
        opcao = 0

        while opcao != 12:
            print "1 - Cadastrar Usuario"
            print "2 - Cadastrar Estacao"
            print "3 - Cadastrar Servidor"
            print "4 - Cadastrar Impressora"
            print "5 - Cadastrar Impressao"
            print "6 - Listar Usuarios"
            print "7 - Listar Estacoes"
            print "8 - Listar Servidores"
            print "9 - Listar Impressoras"
            print "10 - Associar Impressoras a um Servidor"
            print "11 - Conectar Usuario a uma Estacao"
            print "12 - Sair"
            opcao = input("O que deseja fazer: ")
    
            if opcao == 1:
                nomeGuerra = raw_input("Nome: ")
                senha = input("Senha: ")
                usuario = Usuario(nomeGuerra, senha)
               
            if opcao == 2:
                codPatrimonio = raw_input("Codigo do Patrimonio: ")
                descricao = raw_input("Descricao: ")
                hd = input("HD: ")
                memoria = input("Memoria: ")
                localizacao = raw_input("Localizacao: ")
                estacao = Estacao(codPatrimonio, descricao, hd, memoria, localizacao)
                
            if opcao == 3:
                codPatrimonio = raw_input("Codigo do Patrimonio: ")
                descricao = raw_input("Descricao: ")
                hd = input("HD: ")
                memoria = input("Memoria: ")
                tamanhoBuffer = input("Tamanho do Buffer: ")
                quantidadeBuffer = input("Quantidade de Buffer: ")
                servidor = Servidor(codPatrimonio, descricao, hd, memoria, tamanhoBuffer, quantidadeBuffer)              
                
            if opcao == 4:
                codPatrimonio = raw_input("Codigo do Patrimonio: ")
                descricao = raw_input("Descricao: ")
                velocidade = input("Velocidade: ")
                impressora = Impressora(codPatrimonio, descricao, velocidade)
                
            if opcao == 5:
                #usuarioaRealizarImpressao = raw_input("Infome o usuario que deseja realizar a impressao: ")
                impressao = Impressao()
                impressao.realizarImpressao(usuario, servidor, impressora, estacao)

            if opcao == 6:
                for i in range(len(usuario.todosUsuarios)):
                    print usuario.todosUsuarios[i].nomeGuerra
                    print usuario.todosUsuarios[i].senha       

            if opcao == 7:
                print "Listando Estacoes"
                for i in range(len(estacao.todasEstacoes)):
                    print "Codigo: " + estacao.todasEstacoes[i].codPatrimonio
                    """print "Descricao: " + estacao.todasEstacoes[i].descricao
                    print "HD: ", estacao.todasEstacoes[i].hd
                    print "Memoria: ", estacao.todasEstacoes[i].memoria
                    print "Localizacao: " + estacao.todasEstacoes[i].localizacao"""
                    print "Usuario Ativo: " + estacao.todasEstacoes[i].usuario
                    print "Data e Hora da Conexao: " + estacao.todasEstacoes[i].dataHoraAtualdaConexao
                    print "\n"
                    
            if opcao == 8:
                print "Listando Servidores"
                for i in range(len(servidor.todosServidores)):
                    
                    print "Codigo: " + servidor.todosServidores[i].codPatrimonio
                    print "Descricao: " + servidor.todosServidores[i].descricao
                    print "HD: ", servidor.todosServidores[i].hd
                    print "Memoria: ", servidor.todosServidores[i].memoria
                    print "Tamanho do Buffer: ", servidor.todosServidores[i].tamanhoBuffer
                    print "Quantidade de Buffer: ", servidor.todosServidores[i].quantidadeBuffer
                    print "Impressoras conectadas: ", servidor.todosServidores[i].recuperaImpressorasConectadas(i)
                        
                    print "\n"
            
            if opcao == 9:
                for i in range(len(impressora.todasImpressoras)):
                    print "Codigo: " + impressora.todasImpressoras[i].codPatrimonio
                    print "Descricao: " + impressora.todasImpressoras[i].descricao
                    print "Velocidade: ", impressora.todasImpressoras[i].velocidade
            
            if opcao == 10:
                conectarImpressoraaoServidor = raw_input("Selecione o servidor desejado: ")
                for i in range(len(servidor.todosServidores)):
                    if servidor.todosServidores[i].codPatrimonio == conectarImpressoraaoServidor:
                        achou = True
                        break
                    else:
                        achou = False
                if achou == True:
                    servidor.todosServidores[i].armazenaImpressorasConectadas(i, impressora)
                    achou = False
                else:
                    print "O servidor pesquisado nao foi localizado!"
                    print "\n"
                    
            if opcao == 11:
                associarUsuarioaEstacao = raw_input("Selecione a estacao desejada: ")
                for i in range(len(estacao.todasEstacoes)):
                    if estacao.todasEstacoes[i].codPatrimonio == associarUsuarioaEstacao:
                        achou = True
                        break
                    else:
                        achou = False
                if achou == True:
                    estacao.todasEstacoes[i].defineUsuarioAtivoemUmaEstacao(i, usuario)
                    achou = False
                else:
                    print "A estacao pesquisada nao foi localizada!"
                    print "\n"
                    
            
                
                                           
menu = Menu()
