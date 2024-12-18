def primeiro_lex(lista):
    menor = lista[0]
    valor_menor = 1000
    for string in lista:
        valor_lex = ord (string[0])
        if valor_lex < valor_menor:
            valor_menor = valor_lex
            menor = string
    return menor