def conta_letras(frase, contar="vogais"):
    frase = frase.lower ()
    indice = 0
    vogais = 0
    consoantes = 0
    frase_sem_espaco = frase.strip ()
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