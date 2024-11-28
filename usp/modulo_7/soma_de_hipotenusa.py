#criar primeiro uma funcao é_hipotenusa (que testa se n é hipotenusa ou não)

def é_hipotenusa (n):
    a = 1
    b = 1
    while (a*a) + (b*b) <= (n*n):
        while b<n and a<=b:
            if ((a*a) + (b*b)) == n*n:
                return True
            else:
                b = b + 1
        a = a + 1
        b = a + 1
    return False
