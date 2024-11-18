n = int(input("Digite um número inteiro:"))
resto_1 = -1
resto_2 = -2
while resto_1 != resto_2 and n!= 0:
    resto_1 = n % 10
    divisao_1 = n // 10
    resto_2 = divisao_1 % 10
    divisao_2 = divisao_1 // 10
    n = divisao_1
if resto_1 == resto_2:
    print ("sim")
if resto_1 != resto_2 and n == 0:
    print ("não")
