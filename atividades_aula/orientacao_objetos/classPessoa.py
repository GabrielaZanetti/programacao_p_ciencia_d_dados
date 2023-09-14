#   definicao da classe pessoas
class Pessoa:
    #   metodo construtor __init__
    #   self referencia o proprio objeto
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    
    #   metodos
    def getNome(self):
        return self.nome
    
    def getIdade(self):
        return self.idade

#   cria um objeto da classe pessoas
p = Pessoa('Joao', 30)

#   chama os metodos da classe pessoas
print(p.getNome())
print(p.getIdade())
        