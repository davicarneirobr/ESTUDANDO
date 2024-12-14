# matrizes em python sao listas de listas 
# estrutura de dados bidimensional com linhas e colunas
# vamos armazenar dados nessas linhas e colunas

A = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]

def cria_matriz (num_linhas, num_colunas, valor):
    '''(int, int, valor) -> matriz (lista de lista)
    Cria e retorna uma matriz com num_linhas linhas e
    num_colunas colunas em que cada elemento é igual ao valor dado.'''
    matriz = []     # lista vazia
    for i in range (num_linhas):
        # cria linha "i"
        linha = []  # lista vazia
        for j in range (num_colunas):
            linha.append (valor)
        
        # adiciona linha a matriz
        matriz.append (linha)

    return matriz

print (cria_matriz(3,3,0))


def imprime_matriz_bonita (matriz_linear):
    for linha in matriz_linear:
        print (linha)
        print ("", end="")

