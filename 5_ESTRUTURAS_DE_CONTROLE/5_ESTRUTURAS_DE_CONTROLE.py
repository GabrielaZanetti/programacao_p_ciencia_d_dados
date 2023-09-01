# Arquivo de leitura
arq = open("programacao_p_ciencia_d_dados/5_ESTRUTURAS_DE_CONTROLE/arq_exemplo.txt")

# Ler todo o arquivo
# print(arq.read())

# Leitura de arquivo por linha
# print(arq.readline())
# print(arq.readline())
# print(arq.readline())

# Leitura de arquivo por posicao de caracter
# print(arq.read(5))
# print(arq.read(3))

# Exemplo multiplo
# print(arq.read(5)) # leitura do arquivo posicao 5
# print("Posicao atual do arquivo: ", arq.tell()) # posicao atual do cursor
# arq.seek(6, 1) # vai pra posicao atual e retorna a nova posicao
# print(arq.read(7))
# arq.seek(11, 8)
# print(arq.read(7))

# Leitura em modo de lista
# l = list(arq.read())
# print(l)

# Leitura do caracter por string
# for c in arq:
#     print(c)

# texto = 'escrevendo no arquivo'
# arq_novo = open("programacao_p_ciencia_d_dados/5_ESTRUTURAS_DE_CONTROLE/arq_exemplo.txt", 'w') # abrir o arquivo para reescrever
# arq_novo.write(texto)
# arq_novo.close()

# arq_novo = open("programacao_p_ciencia_d_dados/5_ESTRUTURAS_DE_CONTROLE/arq_exemplo.txt", 'r') # abre o arquivo
# print(arq_novo.read())

# texto = input("Digite o texto do arquivo: ") # escrevendo o texto pelo terminal 
# arq_edit = open("programacao_p_ciencia_d_dados/5_ESTRUTURAS_DE_CONTROLE/arq_exemplo.txt", "w") # abrir o arquivo para reescrever
# arq_edit.write(texto) # inclui texto digitado no input ao arquivo
# arq_edit.close() # fechamento do arquivo
# arq_edit = open("programacao_p_ciencia_d_dados/5_ESTRUTURAS_DE_CONTROLE/arq_exemplo.txt", "r") # leitura padrao do arquivo
# print(arq_edit.read())

# texto = input("Digite o texto do arquivo: ") # escrevendo o texto pelo terminal 
# arq_new = open("programacao_p_ciencia_d_dados/5_ESTRUTURAS_DE_CONTROLE/arq_exemplo.txt", "a") # abrir o arquivo para adicionar novo texto
# arq_new.write(texto) # inclui texto digitado no input ao arquivo
# arq_new.close() # fechamento do arquivo
# arq_new = open("programacao_p_ciencia_d_dados/5_ESTRUTURAS_DE_CONTROLE/arq_exemplo.txt", "r") # leitura padrao do arquivo
# print(arq_new.read())

# lista = ['Lista 1\n', 'Lista 2\n', 'Lista 3\n'] # inclusao do texto em lista
# arq_edit_new = open("programacao_p_ciencia_d_dados/5_ESTRUTURAS_DE_CONTROLE/arq_exemplo.txt", "w") # abrir o arquivo para reescrever
# arq_edit_new.writelines(lista)
# arq_edit_new.close()
# arq_edit_new = open("programacao_p_ciencia_d_dados/5_ESTRUTURAS_DE_CONTROLE/arq_exemplo.txt", "r") # leitura padrao do arquivo
# print(arq_edit_new.read())
