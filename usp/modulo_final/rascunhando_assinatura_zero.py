# quero criar uma funcao para calcular o valor da assinatura zero [0]
# a funcao vai receber como parametro uma lista de palavras
# e vai devolver = Tamanho médio de palavra 
# é a soma dos tamanhos das palavras dividida pelo número total de palavras
# temos que ver o tamanho de cada elemento da lista_de_palavras, ir somando em um for
# soma_de_caracteres = o valor total da soma é o número de caracteres
# len (lista_de_palavras) é o total / número de palavras de um texto
# [0] vai ser dado pela divisão de soma_de_caracteres / len (lista_de_palavras)

def assinatura_zero (lista_de_palavras):
    soma_de_caracteres = 0
    for palavra in lista_de_palavras:
        soma_de_caracteres = len (palavra) + soma_de_caracteres
    soma_de_palavras = len (lista_de_palavras)
    valor_assinatura_zero = soma_de_caracteres / soma_de_palavras
    return valor_assinatura_zero
