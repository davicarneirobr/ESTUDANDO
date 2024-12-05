def remove_repetidos (lista):
    lista.sort ()
    lista_sem_repetidos = []
    for i in lista:
        if i not in lista_sem_repetidos:
            lista_sem_repetidos.append (i)
    return lista_sem_repetidos

lista = [1,2,3,3,3,4,5,6,0,2,5,7,10,10,20,30]

print (remove_repetidos(lista))