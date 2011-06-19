'''
Created on 16/02/2011

@author: Karolyne
'''
from should_dsl.dsl import should
from should_dsl.matchers import equal_to
import unittest
from Impressao import Impressao

class Teste_Impressao(unittest.TestCase):
    
    def testeAdicionaUmaImpressao(self):
        self.impressao = Impressao("Documento do Word", "Michael", "HP 2300", 5)
        self.impressao.arquivo |should| equal_to("Documento do Word")
        self.impressao.usuario |should| equal_to("Michael")
        self.impressao.impressora |should| equal_to("HP 2300")
        self.impressao.numeroCopias |should| equal_to(5)
        self.impressao.todasImpressoes[0].arquivo |should| equal_to("Documento do Word")
