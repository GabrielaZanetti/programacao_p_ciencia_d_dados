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
import banco

con = banco.getConexao()
cursor = con.cursor(prepared=True)

arq = (open('C:/Users/gabriela.zanetti/Documents/GitHub/programacao_p_ciencia_d_dados/estudos_independentes/estudo4/POP2022_Municipios_20230622.csv'))
dados = csv.reader(arq) 

estados_sem_duplicado = []
estados = []
municipios = []
for item in dados:
    municipios.append(( item[2], item[3], int(item[4].replace('.', '')), int(item[1]) ))
    if not item[0] in estados_sem_duplicado:
        estados_sem_duplicado.append(item[0])
        estados.append(( item[0], int(item[1]) ))

sql_estados = "INSERT INTO estado (uf, cod_uf) VALUES (?, ?)"

cursor.executemany(sql_estados, estados)
con.commit()

print(cursor.rowcount, "registros inseridos")

sql_municipios = "INSERT INTO municipios (num_muni, cod_municipio, nome_municipio, populacao, cod_uf) VALUES (default, ?, ?, ?, ?)"

cursor.executemany(sql_municipios, municipios)
con.commit()

print(cursor.rowcount, "registros inseridos")

con.close
