import csv

lista = [
    ["nome", "idade"],
    ["joao", 20],
    ["maria", 20],
]
arq = open('programacao_p_ciencia_d_dados/atividades_aula/csv/novo.csv', "w")
#   cria o objeto de gravacao
w = csv.writer(arq)

#   grava as linhas
for i in lista:
    w.writerow(i)

arq.close()