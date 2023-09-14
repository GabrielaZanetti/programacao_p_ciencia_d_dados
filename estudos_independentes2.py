#   1. Escreva um programa que leia do teclado dois conjuntos de nomes de frutas. Os conjuntos podem ter tamanhos variáveis. Em seguida, apresente na tela a união, a interseção e a diferença entre os conjuntos. Apresente também a diferença de número de elementos contidos entre os dois conjuntos.
"""
array_frutas = []
uniao_frutas = ''
soma_fruta = []
fruta = input('Informe um conjunto de frutas:(ex: abacaxi, banana) ')
for frutas in fruta.split(', '):
    array_frutas.append({'nome': frutas})
    soma_fruta.append(len(frutas))


for arrays in array_frutas: #   uniao
    uniao_frutas += str(arrays['nome'])
    print('Nome fruta: '+ str(arrays['nome']))


print('Uniao das frutas: '+ str(uniao_frutas))


def calculaDiferenca(tamanho):
    maxTamanho = max(tamanho)
    minTamanho = min(tamanho)
    return maxTamanho - minTamanho


direfencaFrutas = calculaDiferenca(soma_fruta)
print('Diferenca das frutas: '+ str(direfencaFrutas))
"""


#   2. Escreva um programa que permaneça em um laço de repetição lendo números inteiros do teclado. Esse laço termina quando for digitado zero ou qualquer valor negativo. O programa deve contar quantas vezes cada valor positivo foi digitado. Ao término do laço de leitura, o programa deve mostrar quais valores foram digitados e quantas vezes cada um. Use um dicionário para resolver esse problema.
"""
numero = int(input('Informe um numero: '))
soma_numeros_p = []
soma_numeros_p.append(numero)
while numero > 0:
    numero = int(input('Informe um numero: '))
    if(numero > 0):
        soma_numeros_p.append(numero)


print('Soma dos valores positivos digitados: '+ str(len(soma_numeros_p)))


quant_num = {}


for elemento in soma_numeros_p:
    if elemento in quant_num:
        quant_num[elemento] += 1
    else:
        quant_num[elemento] = 1
print(quant_num)
"""


#   3. Escreva um programa que receba os nomes dos alunos e suas respectivas notas. Cada aluno possui duas notas de 0 (zero) até 100. Tais informações devem ser armazenadas em uma estrutura de dados. A quantidade de alunos para leitura deve ser informada no início do programa. Após a leitura dos dados, exiba as informações do aluno, contendo: Nome, Nota 1, Nota 2, Média (média entre Nota 1 e Nota 2) e a Situação do Aluno. A situação do aluno será ?Aprovado(a)? se atingir a média 60. Caso contrário, estará ?Reprovado(a)?. Exiba ainda, o número de alunos aprovados, o número de alunos reprovados, percentual de aprovação, percentual de reprovação e a média de notas da turma para Nota 1, Nota 2 e Média.
"""
qnt_alunos = int(input('Informe a quantidade de alunos: '))
num = 0
alunos = []
alunos_aprovados = 0
alunos_reprovados = 0
nota1_alunos = 0
nota2_alunos = 0
media_alunos = 0
while num < qnt_alunos:
    nome = input('Informe o nome do alunos: ')
    nota1 = int(input('Informe o a primeira nota:(1 ate 100) '))
    nota2 = int(input('Informe o a segunda nota:(1 ate 100) '))
    media = (nota1 + nota2)/2
    if media >= 60:
        situacao = 'Aprovado(a)'  
        alunos_aprovados += 1
    else:
        situacao = 'Reprovado(a)'
        alunos_reprovados += 1
    alunos.append({
        'nome': nome,
        'nota1': nota1,
        'nota2': nota2,
        'media': media,
        'situacao': situacao,
    })
    nota1_alunos += nota1
    nota2_alunos += nota2
    media_alunos += media
    num += 1


for aluno in alunos:
    print('Nome: '+ aluno['nome'] +', Nota 1'+ str(aluno['nota1']) +', Nota 2'+ str(aluno['nota2']) +', Media: '+ str(aluno['media']) +', Situacao do Aluno: '+ aluno['situacao'])


print('Total de alunos aprovados: '+ str(alunos_aprovados))
print('Total de alunos reprovados: '+ str(alunos_reprovados))
print('Media de notas da turma: ')


percent_aprov = (alunos_aprovados/qnt_alunos)*100
percent_repro = (alunos_reprovados/qnt_alunos)*100


print('Percentual de aprovação: '+ str(percent_aprov))
print('Percentual de reprovação: '+ str(percent_repro))


media_nota1 = nota1_alunos/qnt_alunos
media_nota2 = nota2_alunos/qnt_alunos
media_media = media_alunos/qnt_alunos


print('Nota 1: '+ str(media_nota1))
print('Nota 2: '+ str(media_nota2))
print('Media: '+ str(media_media))
"""
