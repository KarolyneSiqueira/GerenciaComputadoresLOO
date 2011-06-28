class Micro():  
    todosMicros = []
    
    def __init__(self, codPatrimonio, descricao, hd, memoria):
        self.codPatrimonio = codPatrimonio
        self.descricao = descricao
        self.hd = hd
        self.memoria = memoria
        self.armazenaMicros(self)
    
    def armazenaMicros(self, micro):
        self.todosMicros.append(micro)
