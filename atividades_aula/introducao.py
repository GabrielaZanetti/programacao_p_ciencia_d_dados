print('Texto')
print('')
print("Texto")
print('')
print("'Texto'")
print('')
print("""
Texto
com
quebra
de
linha
""")

####################################################################################################

print("Texto \ncom \nquebra \nde \nlinha")
print('')
print("Texto \n" * 3 +"com \nquebra \nde \nlinha") # repete 3x a primeira linha

a = "texto"
b = 5
c = 5.5 
print(type(a))
print(type(b))
print(type(c))
print("")
d, e, f = "texto", 5, 5.5  # inicia as variaveis em linha (ordenada 1 = 1)
print(type(d))
print(type(e))
print(type(f))

####################################################################################################

l = []
print(type(l))
print(l)
print("")

####################################################################################################

l = [10, 15, 20, 25, 30]
print(l)
print(l[0])
print(l[1])
print(len(l)) # tamanho do array

# print(l[5]) # erro localizacao nao definida

####################################################################################################

l1 = [10, 15]
l2 = [2] * 3
l3 = [1, 2] * 3 * 3

print(l1)
print(l2)
print(l3)

l = [1, 2, 5, 7, 4, 9]
print(l[0:3]) # busca do as 3 primeiras posicoes

print(l[5:]) # busca apartir do indice 5

####################################################################################################

l = [1, 2, 5, 7, 4, 9]

print(4 in l)
print(3 in l)

####################################################################################################

a = [1, 2, 5, 7, 4, 9]
b = a
c = a.copy()

print(a)
print(b)
print(c)

b[0] = 888
c[0] = 999

print(a)
print(b)
print(c)

####################################################################################################

t1 = (1, 2, 3) # tupla -> tipo de lista mas e imutável
t2 = 1, 2, 3

print(t1)
print(t2)
print(type(t1))