#   heranca
import Pessoa

class Aluno(Pessoa.Pessoa):
    def __init__(self, nome, idade, matricula):
        # metodo construtor de Pessoas 
        super().__init__(nome, idade)

    def getMatricula(self):
        return self.matricula
    
#   cria um objeto da classe aluno
a = Aluno("Joao", 30, 9999)

#   chama os metodos da classe aluno
print(a.getNome())
print(a.getIdade())
print(a.getMatricula())
