# número total de frases / número de sentenças

def assinatura_quatro (texto):
    # primeiramente, ele separa o texto em sentenças e cria um lista de sentencas
    lista_de_sentencas = separa_sentencas (texto)
    # agora preciso criar uma lista de frases a partir de uma lista de sentencas
    # a funcao já dada anteriormente separa_frases (sentença), pega um string, uma frase
    # e devolve uma lista de frases dessa sentença
    # para isso, vou ter que correr um for na lista de senteça para criar uma lista de frases
    lista_de_frases = []
    for sentenca in lista_de_sentencas:
        frases = separa_frases(sentenca)
        lista_de_frases.extend (frases) # criando a lista de frases
    numero_total_de_frases = len (lista_de_frases)
    numero_total_de_sentencas = len (lista_de_sentencas)
    valor_assinatura_quatro = numero_total_de_frases / numero_total_de_sentencas
    return valor_assinatura_quatro
