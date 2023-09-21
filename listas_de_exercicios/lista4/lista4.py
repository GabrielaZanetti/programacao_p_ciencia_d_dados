#   Crie uma classe para implementar uma conta corrente. A classe deve possuir os seguintes atributos:
#       número da conta
#       nome do correntista
#       saldo
#   Crie métodos para as seguintes operações:
#       Método construtor
#       Alterar o nome do correntista
#       Efetuar depósito
#       Efetuar saque
#       Efetuar transferência entre contas
#       Retornar os dados da conta (atributos)
#   No construtor, o saldo é opcional, podendo iniciar com valor zero (default) e os demais atributos são obrigatórios.
#   Crie pelo menos 3 objetos (contas correntes) e efetue transações nas contas (depósitos, saques e transferências).
#   No final, gere um arquivo CSV com o relatório da situação das contas (dados de cada conta).
import csv

class ContaCorrente():
    def __init__(self, numeroConta, nomeCorrentista, saldo):
        self.numeroConta = numeroConta
        self.nomeCorrentista = nomeCorrentista
        self.saldo = saldo

    def alterNameCorrentista(self, novoNome):
        self.nomeCorrentista = novoNome

    def efetuarDeposito(self, deposito):
        self.saldo += deposito
        
    def efetuarSaque(self, saque):
        self.saldo = self.saldo - saque
        
    def transferenciaContas(self, valor, destino):
        self.efetuarSaque(valor)
        destino.efetuarDeposito(valor)
    
    def getnumeroConta(self):
        return self.numeroConta

    def getnomeCorrentista(self):
        return self.nomeCorrentista

    def getsaldo(self):
        return self.saldo

conta1 = ContaCorrente(123, 'nome correntista', 20)
conta2 = ContaCorrente(456, 'nome correntista', 40)
conta3 = ContaCorrente(789, 'nome correntista', 39)

conta1.alterNameCorrentista('Paulo')
conta1.efetuarDeposito(50)
conta1.efetuarSaque(30)

conta2.alterNameCorrentista('Ana')
conta2.efetuarDeposito(50)
conta2.efetuarSaque(30)

conta3.alterNameCorrentista('Julia')
conta3.efetuarDeposito(100)
conta3.efetuarSaque(20)

conta1.transferenciaContas(40, conta2)
conta1.transferenciaContas(50, conta3)

conta2.transferenciaContas(30, conta1)
conta2.transferenciaContas(60, conta3)

conta3.transferenciaContas(90, conta1)
conta3.transferenciaContas(10, conta2)

lista = [
    ["número da conta", conta1.getnumeroConta()],
    ["nome do correntista", conta1.getnomeCorrentista()],
    ["saldo", conta1.getsaldo()],
    ["número da conta", conta2.getnumeroConta()],
    ["nome do correntista", conta2.getnomeCorrentista()],
    ["saldo", conta2.getsaldo()],
    ["número da conta", conta3.getnumeroConta()],
    ["nome do correntista", conta3.getnomeCorrentista()],
    ["saldo", conta3.getsaldo()],
]

arq = open('C:/Users/gabriela.zanetti/Documents/GitHub/programacao_p_ciencia_d_dados/listas_de_exercicios/lista4/relatorio.csv', "w")
w = csv.writer(arq)

for i in lista:
    w.writerow(i)

arq.close()