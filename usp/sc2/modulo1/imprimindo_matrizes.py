def imprime_matriz(matriz):
    for linha in matriz:
        for coluna in linha:
            print (coluna, end=" ")
        print ("")

minha_matriz = [[1, 2, 3], [4, 5, 6]]
imprime_matriz(minha_matriz)
