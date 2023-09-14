import csv

arq = (open('programacao_p_ciencia_d_dados/atividades_aula/csv/teste.csv'))
dados = csv.reader(arq)
print(dados)
print(type(dados))
print()

for item in dados:
    print(item)
    print(type(item))