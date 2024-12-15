import re

def imprime_matriz2(matriz):
    for linha in matriz:
        linha = str(linha)
        remover = "[],"
        for caractere in remover:
            linha = linha.replace(caractere, "")
        print (linha)