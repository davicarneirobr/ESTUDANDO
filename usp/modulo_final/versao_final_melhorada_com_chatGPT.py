import re

# Funções que você pediu para não mexer:

def le_assinatura():
    '''A funcao le os valores dos tracos linguisticos do modelo e devolve uma assinatura a ser comparada com os textos fornecidos'''
    print("Bem-vindo ao detector automático de COH-PIAH.")
    print("Informe a assinatura típica de um aluno infectado:")

    wal = float(input("Entre o tamanho médio de palavra:"))
    ttr = float(input("Entre a relação Type-Token:"))
    hlr = float(input("Entre a Razão Hapax Legomena:"))
    sal = float(input("Entre o tamanho médio de sentença:"))
    sac = float(input("Entre a complexidade média da sentença:"))
    pal = float(input("Entre o tamanho médio de frase:"))

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


# Funções melhoradas a partir daqui

# Funções Auxiliares para evitar repetição
def calcula_valor_assinatura(lista_palavras, texto, tipo_assinatura):
    '''Calcula valores para diferentes assinaturas, agrupando o código semelhante.'''
    if tipo_assinatura == 0:
        return soma_de_caracteres_de_uma_lista_de_palavras(lista_palavras) / len(lista_palavras)
    elif tipo_assinatura == 1:
        return n_palavras_diferentes(lista_palavras) / len(lista_palavras)
    elif tipo_assinatura == 2:
        return n_palavras_unicas(lista_palavras) / len(lista_palavras)
    elif tipo_assinatura == 3:
        lista_de_sentencas = separa_sentencas(texto)
        soma_de_caracteres_da_sentenca = sum(len(sentenca) for sentenca in lista_de_sentencas)
        return soma_de_caracteres_da_sentenca / len(lista_de_sentencas)
    elif tipo_assinatura == 4:
        lista_de_sentencas = separa_sentencas(texto)
        lista_de_frases = [frase for sentenca in lista_de_sentencas for frase in separa_frases(sentenca)]
        return len(lista_de_frases) / len(lista_de_sentencas)
    elif tipo_assinatura == 5:
        lista_de_sentencas = separa_sentencas(texto)
        lista_de_frases = [frase for sentenca in lista_de_sentencas for frase in separa_frases(sentenca)]
        soma_de_caracteres_da_frase = sum(len(frase) for frase in lista_de_frases)
        return soma_de_caracteres_da_frase / len(lista_de_frases)
    else:
        return None

# Função para calcular a assinatura de um texto
def calcula_assinatura(texto):
    '''Calcula a assinatura de um texto com base nos traços linguísticos.'''
    lista_de_palavras_do_texto = listando_palavras(texto)
    assinatura = [
        calcula_valor_assinatura(lista_de_palavras_do_texto, texto, i) for i in range(6)
    ]
    return assinatura

# Função para comparar duas assinaturas
def compara_assinatura(as_a, as_b):
    '''Compara duas assinaturas baseando-se na diferença de valores.'''
    return sum(abs(a - b) for a, b in zip(as_a, as_b)) / len(as_a)

# Função para avaliar os textos com base na assinatura fornecida
def avalia_textos(textos, ass_cp):
    '''Avalia uma lista de textos comparando com uma assinatura de COH-PIAH.'''
    lista_de_valores_de_similaridade = [
        compara_assinatura(calcula_assinatura(texto), ass_cp) for texto in textos
    ]
    # Encontra o texto com a menor similaridade
    maior_similaridade = min(lista_de_valores_de_similaridade)
    posicao_na_lista_de_valores_de_similaridade = lista_de_valores_de_similaridade.index(maior_similaridade) + 1
    return posicao_na_lista_de_valores_de_similaridade


# Funções auxiliares que não foram alteradas

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

def soma_de_caracteres_de_uma_lista_de_palavras(lista_de_palavras):
    soma_de_caracteres = 0
    for palavra in lista_de_palavras:
        soma_de_caracteres = len(palavra) + soma_de_caracteres
    return soma_de_caracteres
