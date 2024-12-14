def imprime_matriz(matriz):
    for linha in matriz:
        for coluna in linha:
            print (coluna, end="\t")
            print ("", end="")

minha_matriz = [[1, 2, 3], [4, 5, 6]]
imprime_matriz(minha_matriz)

def imprime_matriz_bonita (matriz_linear):
    for linha in matriz_linear:
        print (linha)
        print ("", end="")