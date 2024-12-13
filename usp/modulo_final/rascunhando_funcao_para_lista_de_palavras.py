# quero criar um funcao que pegue um texto (em linha unica) e separe ele ate criar uma lista [] das palavras dele
# funcao que ira pegar um texto bruto e levar ate a lista de palavras
# 1o passo - separando as sentenças do texto
# 2o passo - separando as frases de cada sentença
# 3o passo - separando as palavras de cada frase

import re

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
