# Escreva um programa que receba um arquivo JSON com o gabarito da prova e com as respostas dos alunos e gere um novo arquivo JSON adicionando um campo com o número de acertos de cada aluno. Exemplo do arquivo JSON:

import json

with open("programacao_p_ciencia_d_dados/listas_de_exercicios/lista3/gabarito.json", encoding='utf-8') as meu_json:
    dados = json.load(meu_json)

gabarito = dados['gabarito']
alunos = dados['alunos']

for aluno in alunos:
    i = 0
    acertos = 0
    while i < len(aluno['repostas']):
        if(aluno['repostas'][i]['reposta'] == gabarito[i]['reposta']):
            acertos += 1
        i += 1
    aluno["acertos"] = acertos

with open('programacao_p_ciencia_d_dados/listas_de_exercicios/lista3/resposta_gabarito.json', "w") as arq:
    json.dump(dados, arq)

print("Arquivo gerado com sucesso")
