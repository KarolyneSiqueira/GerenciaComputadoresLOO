'''
Created on 12/02/2011

@author: Karolyne
'''
from should_dsl.dsl import should
from should_dsl.matchers import be, equal_to
import unittest
from Usuario import Usuario

class Teste_Usuario(unittest.TestCase):

    def testeAdicionaUmUsuario(self):
        self.usuario = Usuario("Michael", 123456)
        self.usuario.nomeGuerra |should| equal_to("Michael")
        self.usuario.senha |should| equal_to(123456)
        #self.usuario.todosUsuarios[0].nomeGuerra |should| equal_to("Michael")  
        
    def testaArmazenaUsuarios(self):
        self.testeAdicionaUmUsuario()
        self.usuario.todosUsuarios[0].nomeGuerra |should| equal_to("Michael")
        self.usuario.todosUsuarios[0].senha |should| equal_to(123456)


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()