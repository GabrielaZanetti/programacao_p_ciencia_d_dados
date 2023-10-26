"""
Com base no arquivo do censo “Prévia da população calculada com base nos resultados do Censo Demográfico 2022 até 25 de dezembro de 2022” (arquivo xls), crie um arquivo .csv com os dados “UF”, “COD. UF”, “COD. MUNIC”, “NOME DO MUNICÍPIO” e “POPULAÇÃO” removendo os demais dados desnecessários do arquivo. Feito isso, crie um programa em Python que leia o arquivo .csv e gere um arquivo .json com a seguinte estrutura de exemplo:
[
    {
        "uf": "RS",
        "cod_uf": 43,
        "municipios": [
            {
                "cod_municipio": 10207,
                "nome_municipio": "Ijuí",
                "populacao": 85135
            }, {
                "cod_municipio": 10306,
                "nome_municipio": "Ilópolis",
                "populacao": 4094
            }
        ]
    }
]
"""

import csv
import json

arq = (open('programacao_p_ciencia_d_dados/estudos_independentes/estudo3/POP2022_Municipios_20230622.csv'))
dados = csv.reader(arq) 

estados_sem_duplicado = []
estados = []
municipios = []
for item in dados:
    municipios.append({
        'uf': item[0],
        'municipios': {
            'cod_municipio': item[2],
            'nome_municipio': item[3],
            'populacao': item[4].strip()
        }
    })
    if not item[0] in estados_sem_duplicado:
        estados_sem_duplicado.append(item[0])
        estados.append({
            'uf': item[0],
            'ucod_uff': item[1],
        })

conjunto_municipios = []
for estado in estados:
    municipio = []
    for muni in municipios:
        if muni['uf'] == estado['uf']:
            municipio.append(muni['municipios'])
    estado['municipios'] = municipio


with open('programacao_p_ciencia_d_dados/estudos_independentes/estudo3/POP2022_Municipios_20230622.json', "w") as arq_novo:
    json.dump(estados, arq_novo)