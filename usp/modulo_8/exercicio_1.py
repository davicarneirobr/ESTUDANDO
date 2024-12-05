def remove_repetidos (lista):
    lista.sort ()
    lista_sem_repetidos = []
    for i in lista:
        if i not in lista_sem_repetidos:
            lista_sem_repetidos.append (i)
    return lista_sem_repetidos