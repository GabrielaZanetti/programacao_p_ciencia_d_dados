import json

arq = open('programacao_p_ciencia_d_dados/atividades_aula/json/teste.json')
dados = json.load(arq)
print(dados)
print(type(dados))
print()
for item in dados:
    print(item)
    print(type(item))
