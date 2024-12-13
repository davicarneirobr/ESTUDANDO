def calcula_primeira_assinatura(texto):
    texto_sem_espacos = texto.replace(" ", "")
    numero_de_caracteres = len(texto_sem_espacos)
    lista_de_palavras_do_texto = separa_palavras(texto)
    quantidade_de_palavras = len (lista_de_palavras_do_texto)
    assinatura0 = numero_de_caracteres / quantidade_de_palavras
    return assinatura0

def calcula_segunda_assinatura (texto):
    lista_de_palavras_do_texto = separa_palavras(texto)
    quantidade_de_palavras = len (lista_de_palavras_do_texto)
    numero_de_palavras_diferentes = n_palavras_unicas (lista_de_palavras_do_texto)
    assinatura1 = numero_de_palavras_diferentes / quantidade_de_palavras
    return assinatura1
    

def calcula_assinatura(texto):
    assinatura = []
    assinatura.append (calcula_primeira_assinatura(texto))
    assinatura.append (calcula_segunda_assinatura(texto))


# [0] = Tamanho médio de palavra é a soma dos tamanhos das palavras dividida pelo número total de palavras

# [1] = Relação Type-Token é o número de palavras diferentes dividido pelo número total de palavras

# [2] = Razão Hapax Legomana é o número de palavras que aparecem uma única vez dividido pelo total de palavras

# [3] = Tamanho médio de sentença é a soma dos números de caracteres em todas as sentenças dividida pelo número de sentenças

# [4] = Complexidade de sentença é o número total de frases divido pelo número de sentenças

# [5] = Tamanho médio de frase é a soma do número de caracteres em cada frase dividida pelo número de frases no texto