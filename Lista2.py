# 1 Escreva um programa que receba um arquivo de texto com o gabarito da prova e outro arquivo com as respostas dos alunos e gere um novo arquivo com o número de acertos de cada aluno.
#   Modelo do gabarito (somente 1 linha): A-B-C-A-B-C-E-D
#   Modelo das respostas (uma linha por aluno, com campos separados por “;”): 
#        ANA;A-B-C-A-B-C-E-D;
#        PAULO;A-B-C-A-B-C-E-D;
#   Modelo do arquivo de saída (uma linha por aluno, com campos separados por “;”):
#         ANA;A-B-C-A-B-C-E-D;8;
#         PAULO;A-B-C-A-B-C-E-D;8;
#   As respostas das questões podem ser de “A” até “E”.
#   O número de questões pode ser variável.
#   Deve permitir verificar os acertos de mais de um aluno.
"""
gabarito = input('Informe o gabarito(exemplo: “A-B-C-A-B-C-E-D”): ')
alunos = []
alunosSoma = []
somaAluno = 1
while somaAluno > 0:
    respAluno = input('Informe o nome do aluno e a resposta(exemplo: “ANA;A-B-C-A-B-C-E-D;”)')
    aluno = respAluno.split(';')
    alunos.append({
        "nome": aluno[0],
        "resposta": aluno[1],
    })
    novoAluno = input('Deseja informar mais um aluno(S/N): ')
    if novoAluno == 'S' or novoAluno == 's':
        somaAluno += 1
    else:
        somaAluno = 0
for a in alunos:
    respAluno = a["resposta"].split('-')
    respGabarito = gabarito.split('-')
    i = 0
    valor = 0
    while i < len(respAluno):
        if respAluno[i] == respGabarito[i]:
            valor = valor + 1
        i += 1
    alunosSoma.append({
        "nome": a["nome"],
        'resposta': a["resposta"],
        'acertos': valor
    })
for alu in alunosSoma:
    print(alu['nome'],";",alu['resposta'],";",alu['acertos'],";",)
"""
#   2. Escreva um programa que faz o registro da venda de produtos. Para isso, é preciso:
#       Obter um arquivo com as informações dos produtos, contendo: Código, nome e valor. Defina o formato do arquivo.
#       Adicionar produtos na venda, onde o usuário informa o produto e a quantidade. A informação do produto pode ser pelo código.
#       O programa deve apresentar os itens da venda contendo as informações do item (código, nome e valor), quantidade e valor total do produto.
#       O programa deve apresentar o valor total da venda.
#       O programa deve gerar um arquivo de saída contendo os dados apresentados nos dois itens anteriores.