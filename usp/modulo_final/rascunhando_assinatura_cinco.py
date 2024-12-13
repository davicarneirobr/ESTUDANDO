# [5] = soma do número de caracteres em cada frase dividida pelo número de frases no texto

def assinatura_cinco (texto):
    lista_de_sentencas = separa_sentencas (texto)
    lista_de_frases = []
    for sentenca in lista_de_sentencas:
        frases = separa_frases(sentenca)
        lista_de_frases.extend (frases)
    soma_de_caracteres_da_frase = sum(len(frase) for frase in lista_de_frases)
    numero_de_frases = len (lista_de_frases)
    valor_assinatura_cinco = soma_de_caracteres_da_frase / numero_de_frases
    return valor_assinatura_cinco