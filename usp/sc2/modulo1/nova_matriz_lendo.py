def le_matriz ():
    num_lin = int(input ("Digite o número de linhas da matriz:"))
    num_col = int(input ("Digite o número de colunas da matriz:"))
    return cria_matriz (num_lin, num_col)


def cria_matriz (num_linhas, num_colunas):
    '''(int, int) -> matriz (lista de lista)
    Cria e retorna uma matriz com num_linhas linhas e
    num_colunas colunas em que cada elemento é digite pelo usuário.'''
    matriz = []     # lista vazia
    for i in range (num_linhas):
        # cria linha "i"
        linha = []  # lista vazia
        for j in range (num_colunas):
            valor = int(input("Digite o elemento [" + str(i) + "][" + str (j) + "]"))
            linha.append (valor)
        
        # adiciona linha a matriz
        matriz.append (linha)

    return matriz

def imprime_matriz_bonita (matriz_linear):
    for linha in matriz_linear:
        print (linha)
        print ("", end="")

m = le_matriz()
print (imprime_matriz_bonita (m))