# criando primeira funcao para calculo do fatorial de um numero
def fatorial (n):
    fat = 1
    while (n>1):
        fat = fat * n
        n = n - 1
    return fat

# criando segunda funcao para calculo do binomio de Newton

def numero_binomial (n,k):
    return fatorial (n) / (fatorial (k) * fatorial (n-k))