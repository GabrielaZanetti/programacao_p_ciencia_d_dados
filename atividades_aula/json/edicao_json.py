import json

dados = [
    {
        "nome": "Joao",
        "idade": 30
    }, {
        "nome": "Ana",
        "idade": 35
    }
]
with open('programacao_p_ciencia_d_dados/atividades_aula/json/novo.json', "w") as arq:
    json.dump(dados, arq)