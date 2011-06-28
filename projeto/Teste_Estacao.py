from Estacao import Estacao
from Teste_Usuario import Teste_Usuario
from should_dsl import should, should_not
import unittest

class Teste_Estacao(unittest.TestCase):
    
    def testeAdicionaUmaEstacao(self):
        self.estacao = Estacao("001", "Estacao SUN", 1000, 8, "Sala 101")
        self.estacao.localizacao |should| equal_to("Sala 101")
        self.estacao.codPatrimonio |should| equal_to("001")
        self.estacao.descricao |should| equal_to("Estacao SUN")
        self.estacao.hd |should| equal_to(1000)
        self.estacao.memoria |should| equal_to(8)
        self.estacao.usuario = "karol"
        self.estacao.dataHoraAtualdaConexao |should_not| equal_to("18/03/2011")
        self.estacao.usuario |should| equal_to("karol")

        
    def testaArmazenaEstacoes(self):
        self.testeAdicionaUmaEstacao()
        self.estacao.todasEstacoes[0].codPatrimonio |should| equal_to("001")
        self.estacao.todasEstacoes[0].descricao |should| equal_to("Estacao SUN")
        self.estacao.todasEstacoes[0].hd |should| equal_to(1000)
        self.estacao.todasEstacoes[0].memoria |should| equal_to(8)
        self.estacao.todasEstacoes[0].localizacao |should| equal_to("Sala 101")
        self.estacao.todasEstacoes[0].usuario |should| equal_to("karol")
        self.estacao.todasEstacoes[0].dataHoraAtualdaConexao |should_not| equal_to("18/03/2011")
        
    def testeVerificaseUsuarioestaoConectadosnaEstacao(self):
        self.testaArmazenaEstacoes()
        testaAchou = self.estacao.verificaseUsuarioestaConectadonaEstacao("karol")
        testaAchou |should| equal_to(True)   


if __name__ == "__main__":
    unittest.main()  
