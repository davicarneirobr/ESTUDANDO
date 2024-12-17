def tirando_espacos (lista_de_nomes):
    lista_de_nome_sem_espacos_em_braco = []
    for nome in lista_de_nomes:
        nome_sem_espacos = nome.strip ()
        lista_de_nome_sem_espacos_em_braco.append (nome_sem_espacos)
    return lista_de_nome_sem_espacos_em_braco

def menor_nome (nomes):
    lista_de_nome_sem_espaco = tirando_espacos (nomes)
    tamanho = len(lista_de_nome_sem_espaco[0])
    salvando_nome = lista_de_nome_sem_espaco[0]
    for nome_without_espaco in lista_de_nome_sem_espaco:
        tamanho_do_nome = len (nome_without_espaco)
        if tamanho_do_nome < tamanho:
            tamanho = tamanho_do_nome
            salvando_nome = nome_without_espaco
    return salvando_nome.capitalize ()