import re

def le_assinatura():
    '''A funcao le os valores dos tracos linguisticos do modelo e devolve uma assinatura a ser comparada com os textos fornecidos'''
    print("Bem-vindo ao detector automático de COH-PIAH.")
    print("Informe a assinatura típica de um aluno infectado:")

    wal = float(input("Entre o tamanho médio de palavra:"))
    ttr = float(input("Entre a relação Type-Token:"))
    hlr = float(input("Entre a Razão Hapax Legomana:"))
    sal = float(input("Entre o tamanho médio de sentença:"))
    sac = float(input("Entre a complexidade média da sentença:"))
    pal = float(input("Entre o tamanho medio de frase:"))

    return [wal, ttr, hlr, sal, sac, pal]

def le_textos():
    '''A funcao le todos os textos a serem comparados e devolve uma lista contendo cada texto como um elemento'''
    i = 1
    textos = []
    texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")
    while texto:
        textos.append(texto)
        i += 1
        texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")

    return textos

def separa_sentencas(texto):
    '''A funcao recebe um texto e devolve uma lista das sentencas dentro do texto'''
    sentencas = re.split(r'[.!?]+', texto)
    if sentencas[-1] == '':
        del sentencas[-1]
    return sentencas

def separa_frases(sentenca):
    '''A funcao recebe uma sentenca e devolve uma lista das frases dentro da sentenca'''
    return re.split(r'[,:;]+', sentenca)

def separa_palavras(frase):
    '''A funcao recebe uma frase e devolve uma lista das palavras dentro da frase'''
    return frase.split()

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

def listando_palavras(texto):
    '''A função recebe um texto e devolve uma lista de todas as palavras do texto.'''
    lista_de_sentencas = separa_sentencas(texto)
    lista_de_palavras = []
    for sentenca in lista_de_sentencas:
        frases = separa_frases(sentenca)
        for frase in frases:
            palavras = separa_palavras(frase)
            lista_de_palavras.extend(palavras)  # Adiciona diretamente as palavras na lista plana
    return lista_de_palavras

def soma_de_caracteres_de_uma_lista_de_palavras (lista_de_palavras):
    soma_de_caracteres = 0
    for palavra in lista_de_palavras:
        soma_de_caracteres = len (palavra) + soma_de_caracteres
    return soma_de_caracteres

def assinatura_zero (lista_de_palavras):
    numero_de_caracteres = soma_de_caracteres_de_uma_lista_de_palavras (lista_de_palavras)
    soma_de_palavras = len (lista_de_palavras)
    valor_assinatura_zero = numero_de_caracteres / soma_de_palavras
    return valor_assinatura_zero

def assinatura_um (lista_de_palavras):
    numero_de_palavras_diferentes = n_palavras_diferentes (lista_de_palavras)
    soma_de_palavras = len (lista_de_palavras)
    valor_assinatura_um = numero_de_palavras_diferentes / soma_de_palavras
    return valor_assinatura_um

def assinatura_dois (lista_de_palavras):
    numero_de_palavras_unicas = n_palavras_unicas (lista_de_palavras)
    soma_de_palavras = len (lista_de_palavras)
    valor_assinatura_dois = numero_de_palavras_unicas / soma_de_palavras
    return valor_assinatura_dois

def assinatura_tres(texto):
    # Parte 1 - Lista de sentenças
    lista_de_sentencas = separa_sentencas(texto)
    
    # Parte 2 - Soma dos caracteres das sentenças (sem os caracteres de separação)
    soma_de_caracteres_da_sentenca = sum(len(sentenca.strip()) for sentenca in lista_de_sentencas)
    
    # Parte 3 - Número de sentenças
    numero_de_sentencas = len(lista_de_sentencas)
    
    # Calcula o valor da assinatura três
    valor_assinatura_tres = soma_de_caracteres_da_sentenca / numero_de_sentencas
    return valor_assinatura_tres

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

