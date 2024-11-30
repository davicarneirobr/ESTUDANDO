def éPrimo (x):
    fator = 2
    if x == 2:
        return True
    while x % fator != 0 and fator <= x/2:
        fator = fator + 1
    if x % fator == 0:
        return False
    else:
        return True

limite = int(input("Limite máximo: "))

n = 2
while n < limite:
    if éPrimo (n):
        print (n, end=", ")
    n = n + 1

primos_menores_cem = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]