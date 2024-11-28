#escrever função n_primos
# receber como argumento (n), tal que n>=2 
# devolve quantos números primos tem de 2 até n

#vamos definir a funcao éPrimo, que vamos sempre chamar para verificar
#se o número dentro de um laço e verificar se é primo:

def éPrimo (x):
    fator = 2
    if x == 2:
        return 1
    else:
        while (x % fator != 0) and (fator <= x/2):
            fator = fator + 1
        if x % fator == 0:
            return 0
        else:
            return 1

def n_primos (n):
    indice = 0
    while n > 1:
        x = éPrimo (n)
        indice = indice + x
        n = n - 1
    return indice
