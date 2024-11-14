n = int(input("Digite um valor inteiro 'n':"))
k = int(input("Digite um valor inteiro 'k', que deve ser menor ou igual ao valor dado a 'n':"))

def fatorial (n):
    fat = 1
    if n == 0:
        fat = 1
    else:
        while n>0:
            fat = fat * n
            n = n - 1
    return fat