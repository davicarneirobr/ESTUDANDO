#rascunho da funcao computador_escolhe_jogada

def  computador_escolhe_jogada (n, m):
    if n > m:
        x = 1
        while n - x % m + 1 != 0:
            x = x + 1
        maior_divisor_de_x = m // x
        x = maior_divisor_de_x * x
        return x
    else:
        x = n
        return x


