#criando função para testar se é primo
def éPrimo (n):
    x = n - 1
    while x>1:
        if n % x == 0:
            x = 0
            return False
        else:
            x = x - 1
    if n == 1:
        return False
    if x == 1:
        return True

#criando função para encontrar o maior primo
def maior_primo (y):
    while not éPrimo (y):
        y = y - 1
    return y