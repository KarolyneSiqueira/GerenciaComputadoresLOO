from Micro import Micro
class Servidor(Micro):
    todosServidores = []
    achou = True
    def __init__(self, codPatrimonio, descricao, hd, memoria, tamanhoBuffer, quantidadeBuffer):
        Micro.__init__(self, codPatrimonio, descricao, hd, memoria)
        self.tamanhoBuffer = tamanhoBuffer
        self.quantidadeBuffer = quantidadeBuffer
        self.impressoras = []
        self.armazenaServidores(self)
                
    def armazenaServidores(self, servidor):
        self.todosServidores.append(servidor)
        
    def armazenaImpressorasConectadas(self, posicao, impressora): 
        opcao = raw_input("Deseja cadastrar impressoras (sim/nao): ")
        
        while opcao.lower() != "nao":
            codImpressora = raw_input("Codigo da impressora: ")
            achouImpressora = self.verificaseImpressoraExiste(codImpressora, impressora)
            if achouImpressora == True:
                achou = self.verificaImpressorasConectadasaoServidor(codImpressora)
                if achou == False:
                    if (len(self.todosServidores[posicao].impressoras)) <= 2 or (len(self.todosServidores[posicao].impressoras)) == None:
                        self.todosServidores[posicao].impressoras.append(codImpressora)
                        print "Impressora conectada com sucesso ao servidor!"
                    else:
                        print "Para este servidor ja existem 3 impressoras cadastradas!"
            
                else:
                    print "Esta impressora ja esta conectada a um servidor!"
            else:
                print "A impressora nao foi localizada!"
            opcao = raw_input("Deseja cadastrar impressoras: sim/nao: ")
                
    
    def recuperaImpressorasConectadas(self, servidor):
        return self.todosServidores[servidor].impressoras
    
    def verificaImpressorasConectadasaoServidor(self, codImpressora):
        for i in range(len(self.todosServidores)):
            if codImpressora in self.todosServidores[i].impressoras:
                achou = True
                break
            else:
                achou = False
        return achou
    
    def verificaseImpressoraExiste(self, codImpressora, impressora):
        for i in range(len(impressora.todasImpressoras)):
            if codImpressora in impressora.todasImpressoras[i].codPatrimonio:
                achou = True
                break
            else:
                achou = False
        return achou
        
