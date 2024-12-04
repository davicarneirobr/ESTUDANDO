#fatias de listas

primos_cem = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

print (primos_cem [1:2])

print (primos_cem [2:7])

print (primos_cem [:12])

print (primos_cem [4:])

#clonando listas

lista1 = ["vermelho", "verde", "azul"]

lista2 = lista1

print (lista2)

lista2 [0] = "rosa"

print (lista2)

print (lista1)

def clone (lista):
    clone = []
    for objeto in lista:
        clone.append (objeto)
    return clone

lista2 = clone (lista1)

print (lista2)

lista2[0] = "amarelo"

print (lista2)

print (lista1)

clone2 = lista2 [:]

print (clone2)

#pertinencia a uma lista (se determinado elemento pertence ou nao a lista)

print ("rosa" in lista1)

print ("rosa" in lista2)

#Concatenacao de listas

print ([1,2] + [3,4])


#listas por repeticao

a = [1,2,3]

a_triplicado = a * 3

print (a_triplicado)

#remocao de elementos em listas

del a[1]

print (a)

listinha = ["a", "b", "c", "d", "e", "f"]

print (listinha)

del listinha[2:5]

print (listinha)