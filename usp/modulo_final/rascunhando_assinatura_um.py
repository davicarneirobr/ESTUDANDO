# [1] = Relação Type-Token é o número de palavras diferentes dividido pelo número total de palavras
# temos que criar uma funcao para calcular o valor da assinatura um
# essa funcao recebe como parametro a lista de palavras
# e devolver o valor da relacao type-token (vamos chamar de rtt)
# para isso vou chamar a funcao n_palavras_diferentes dentro dessa funcao
# a funcao n_palavras_diferentes recebe como parametro uma lista de palavras
# e devolve o numero de palavras diferentes em um texto (sera o numerador da rtt)
# o numerador da rtt é o len (lista_de_palavras)

def n_palavras_diferentes(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras diferentes utilizadas'''
    freq = dict()
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            freq[p] += 1
        else:
            freq[p] = 1

    return len(freq)


