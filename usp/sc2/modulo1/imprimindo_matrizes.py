import re

def imprime_matriz2(matriz):
    for linha in matriz:
        linha = str(linha)
        remover = "[],"
        for caractere in remover:
            linha = linha.replace(caractere, "")
        print (linha)

minha_matriz = [[1, 2, 3], [4, 5, 6]]
imprime_matriz2(minha_matriz)