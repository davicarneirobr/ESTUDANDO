n = 0
while n == 0:
    n = int(input("Digite o valor de n:"))
    fatorial = 1
    if n < 0:
        print ("Não existe fatorial de número negativo! Tente de novo!")
    if n == 0:
        fatorial = 1
        print (fatorial)
    if n > 0:
        while n>0:
            fatorial = fatorial * n
            n = n - 1
        print (fatorial)
    n = 0