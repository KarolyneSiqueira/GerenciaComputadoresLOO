from Micro import Micro
from should_dsl import should
import unittest

class Teste_Micro(unittest.TestCase):

    def testeAdicionaUmMicro(self):
        self.micro = Micro("001", "Micro ultra veloz", 500, 4)
        self.micro.codPatrimonio |should| be("001")
        self.micro.descricao |should| equal_to("Micro ultra veloz")
        self.micro.hd |should| equal_to(500)
        self.micro.memoria |should| equal_to(4)
      
        
    def testeArmazenaMicros(self):
        self.testeAdicionaUmMicro()
        self.micro.todosMicros[0].codPatrimonio |should| equal_to("001")
        self.micro.todosMicros[0].descricao |should| equal_to("Micro ultra veloz")
        self.micro.todosMicros[0].hd |should| equal_to(500)
        self.micro.todosMicros[0].memoria |should| equal_to(4)
        
if __name__ == "__main__":
    unittest.main()
