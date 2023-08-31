# 1. Faça um programa que receba um número inteiro. Se esse número for positivo, calcule a raiz quadrada do número. Senão, informe que o número é inválido.
"""
import math
a = int(input('Informe um valor: '))
if a > 0:
    raiz = math.sqrt(a)
    print(raiz)
else:
    print("número é inválido5")
"""

# 2. Faça um programa que receba um número inteiro e mostre se este número é par ou ímpar.
"""
b = int(input('Informe um valor: '))
if b % 2 == 0:
    print("Valor é par")
else:
    print("Valor é impar")
"""

# 3. Escreva um programa que receba dois números inteiros. Mostre qual é o maior número e a diferença existente entre ambos. Se os dois números forem iguais, exiba a mensagem “Números Iguais”.
"""
c = int(input('Informe um valor: '))
d = int(input('Informe outro valor: '))
if c == d:
    print("Números Iguais")
else:
    if c > d:
        print("O primeiro número e maior, sendo: ", c)
    else:
        print("O segundo número e maior, sendo: ", d)
    calc = c - d
    print("a diferença existente entre ambos é: ", calc)
"""

# 4. Escreva um programa que receba um gabarito, as respostas dos alunos e informe o número de acertos de cada aluno.
#   As respostas das questões podem ser de “A” até “E”.
#   Exemplo de entrada das respostas e do gabarito “A-B-C-A-B-C-E-D”
#   O número de questões pode ser variável (obtenha a informação do usuário)
#   Deve permitir verificar os acertos de mais de um aluno.


# 5. Escreva um programa que faz o registro da venda de produtos. Para isso, é preciso:
#   Armazenar as informações dos produtos, contendo: Código, nome e valor.
#   Defina de forma fixa o conjunto de produtos.
#   Adicionar produtos na venda, onde o usuário informa o produto e a quantidade. A informação do produto pode ser pelo código.
#   O programa deve apresentar os itens da venda contendo as informações do item (código, nome e valor), quantidade e valor total do produto.
#   O programa deve apresentar o valor total da venda
produto = []
venda = []
e = 1
while e > 0:
    cod = input('Informe o Código do produto: ')
    name = input('Informe o nome do produto: ')
    value = input('Informe o valor do produto: ')
    produto.append({
        "codigo": cod,
        "nome": name,
        "valor": value,
    })

    addProd = input('Deseja adicionar mais um produto? (S/N)')
    if addProd == 'S' or addProd == 's':
        e += 1
    else:
        e = 0
        addVenda = input('Deseja adicionar produtos a venda? (S/N)')
        if addVenda == 'S' or addVenda == 's':
            print("Os produtos a adicionar a venda sao:")
            sumProd = 0
            for x in produto:
                sumProd += 1
                print("Produto ",sumProd,' codigo: ',x['codigo'],' nome: ',x['nome'],' valor: ',x['valor'])
            f = 1
            while f > 0:
            addVendaProd = input('Informe o codigo do produto: ')
            for x in produto:
                if x['codigo'] == addVendaProd:
                    addVendaQuant = input('Informe a quantidade do produto: ')
                    venda.append({
                        "codigo": x['codigo'],
                        "nome": x['nome'],
                        "valor": x['valor'],
                        "quant": addVendaQuant,
                    })
                    f += 1
                else:
                    addNewProd = input('O produto nao esta na lista, deseja inserir outro produto? (S/N)')
                    if addNewProd == "S" or addNewProd == "s":
                        f += 1
                    else:
                        f = 0
    else:
        print("Fim do programa!")
