def tirando_espacos (lista_de_nomes):
    lista_de_nome_sem_espacos_em_braco = []
    for nome in lista_de_nomes:
        nome_sem_espacos = nome.strip ()
        lista_de_nome_sem_espacos_em_braco.append (nome_sem_espacos)
    return lista_de_nome_sem_espacos_em_braco

def conta_letras(frase, contar="vogais"):
    frase = frase.lower ()
    indice = 0
    vogais = 0
    consoantes = 0
    frase_sem_espaco = tirando_espacos (frase)
    while indice < len (frase_sem_espaco):
        if frase_sem_espaco[indice] == "a" or frase_sem_espaco[indice] == "e" or frase_sem_espaco[indice] == "i" or frase_sem_espaco[indice] == "o" or frase_sem_espaco[indice] == "u":
            vogais = vogais + 1
        else:
            consoantes = consoantes + 1
        indice = indice + 1
    if contar == "consoantes":
        return consoantes
    else:
        return vogais

print (conta_letras("programamos em python", "consoantes"))