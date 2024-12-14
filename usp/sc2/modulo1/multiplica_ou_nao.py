def dimensoes (matriz):
    lin = 0
    col = 0
    lin = len (matriz)
    for linha in matriz:
        lista_da_linha = linha
        col = len (lista_da_linha)
    return lin,col

def sao_multiplicaveis(m1, m2):
    dimensao_m1 = dimensoes (m1)
    dimensao_m2 = dimensoes (m2)
    num_col_m1 = dimensao_m1 [1]
    num_lin_m2 = dimensao_m2 [0]
    if num_col_m1 == num_lin_m2:
        return True
    else:
        return False