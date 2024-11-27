def éPrimo (x):
    fator = 2
    if x == 2:
        return True
    else:
        while (x % fator != 0) and (fator <= x/2):
            fator = fator + 1
        if x % fator == 0:
            return False
        else:
            return True


n = int(input("Digite um número inteiro maior que 1:"))
while n > 0:
    if éPrimo (n):
        print (n, "É Primo!")
    else:
        print (n, "Não é Primo!")
    n = int(input("Digite um número inteiro maior que 1:"))
