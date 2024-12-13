def n_palavras_unicas(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras que aparecem uma unica vez'''
    freq = dict()
    unicas = 0
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            if freq[p] == 1:
                unicas -= 1
            freq[p] += 1
        else:
            freq[p] = 1
            unicas += 1

    return unicas

def assinatura_dois (lista_de_palavras):
    numero_de_palavras_unicas = n_palavras_unicas (lista_de_palavras)
    soma_de_palavras = len (lista_de_palavras)
    valor_assinatura_dois = numero_de_palavras_unicas / soma_de_palavras
    return valor_assinatura_dois
