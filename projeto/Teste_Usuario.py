from should_dsl import should
import unittest
from Usuario import Usuario

class Teste_Usuario(unittest.TestCase):

    def testeAdicionaUmUsuario(self):
        self.usuario = Usuario("Karol", 123456)
        self.usuario.nomeGuerra |should| equal_to("Karol")
        self.usuario.senha |should| equal_to(123456)
               
    def testaArmazenaUsuarios(self):
        self.testeAdicionaUmUsuario()
        self.usuario.todosUsuarios[0].nomeGuerra |should| equal_to("Karol")
        self.usuario.todosUsuarios[0].senha |should| equal_to(123456)


if __name__ == "__main__":
    unittest.main()
