from Impressora import Impressora
from should_dsl import should
import unittest

class Teste_Impressora(unittest.TestCase):
    
    def testeAdicionaUmaImpressora(self):
        self.impressora = Impressora("001", "HP 2300", 500)
        self.impressora.codPatrimonio |should| equal_to("001")
        self.impressora.descricao |should| equal_to("HP 2300")
        self.impressora.velocidade |should| equal_to(500)
        
    def testeArmazenaImpressoras(self):
        self.testeAdicionaUmaImpressora()
        self.impressora.todasImpressoras[0].codPatrimonio |should| equal_to("001")
        self.impressora.todasImpressoras[0].descricao |should| equal_to("HP 2300")
        self.impressora.todasImpressoras[0].velocidade |should| equal_to(500)


if __name__ == "__main__":
    unittest.main()
