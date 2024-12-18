def maiusculas(frase):
    devolve = ""
    indice = 0
    while indice <= len (frase):
        if ord(frase[indice]) >= 65 and ord(frase[indice]) <= 90:
            devolve = devolve + frase[indice]
        indice = indice + 1
    return devolve
