def dimensoes (matriz):
    lin = 0
    col = 0
    lin = len (matriz)
    for linha in matriz:
        lista_da_linha = linha
        col = len (lista_da_linha)
    return (lin,col)

def soma_matrizes (m1, m2):
    dimensao_m1 = dimensoes (m1)
    dimensao_m2 = dimensoes (m2)
    if dimensao_m1 != dimensao_m2:
        return False
    else:
        