#criar primeiro uma funcao é_hipotenusa (que testa se n é hipotenusa ou não)

def é_hipotenusa (n):
    a = 1
    b = 1
    while (a*a) + (b*b) <= (n*n):
        while b<n and a<=b:
            if ((a*a) + (b*b)) == n*n:
                return n
            else:
                b = b + 1
        a = a + 1
        b = a + 1
    return 0

#agr temos que pensar numa forma (provavel um loop) de ir testando os "n" que servem (até 5, que é o menor):

def soma_hipotenusas (n):
    indice = 0
    soma = 0
    while n >= 5:
        indice = é_hipotenusa (n)
        soma = soma + indice
        n = n - 1
    return soma