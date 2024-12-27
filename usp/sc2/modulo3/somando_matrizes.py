def cria_matriz (num_linhas, num_colunas, valor):
    '''(int, int, valor) -> matriz (lista de listas)
    Cria e retorna uma matriz com um num_linhas linhas e num_colunas colunas
    em que cada elemento é igual ao valor dado
    '''
    matriz = [] # lista vazia
    for i in range (num_linhas):
        # cria linha i
        linha = [] # lista vazia
        for j in range (num_colunas):
            linha.append (valor)
    
        # adiciona linha à matriz
        matriz.append (linha)
    return matriz

def soma_matrizes (A, B):
    # criando matriz zerada
    num_lin = len (A)
    num_col = len (A[0])
    C = cria_matriz(num_lin, num_col, 0)
    # agora fazendo um vetor que percorar as matrizes
    for lin in range (num_lin): # percorre as linhas da matriz
        for col in range (num_col): # percorre as colunas da matriz (para cada linha)
            C[lin][col] = A [lin][col] + B [lin][col]
    return C

A = [[1,2,3], [4,5,6], [7,8,9]]
B = [[10,20,30], [40,50,60], [70,80,90]]


print(soma_matrizes(A, B))

