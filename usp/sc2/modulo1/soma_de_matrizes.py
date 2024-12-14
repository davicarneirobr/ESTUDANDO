def dimensoes (matriz):
    lin = 0
    col = 0
    lin = len (matriz)
    for linha in matriz:
        lista_da_linha = linha
        col = len (lista_da_linha)
    return lin,col

def soma_matrizes (m1, m2):
    dimensao_m1 = dimensoes (m1)
    dimensao_m2 = dimensoes (m2)
    num_lin = dimensao_m1 [0]
    num_col = dimensao_m1 [1]
    if dimensao_m1 != dimensao_m2:
        return False
    else:
        matriz_somada = []
        for i in range (num_lin):
            linha = []
            for j in range (num_col):
                valor1 = m1[i][j]
                valor2 = m2[i][j]
                valor = valor1 + valor2
                linha.append (valor)
            matriz_somada.append (linha)
        return matriz_somada