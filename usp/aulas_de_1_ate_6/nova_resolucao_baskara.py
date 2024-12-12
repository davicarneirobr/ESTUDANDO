import math
def delta (a, b, c):
    return b*b-(4*a*c)
def main():
    a=float(input("Qual o valor de a?"))
    b=float(input("Qual o valor de b?"))
    c=float(input("Qual o valor de c?"))
    imprime_raizes(a, b, c)

def imprime_raizes (a,b,c):
    d = delta (a, b, c)
    if d == 0:
        raiz1 = (-b + math.sqrt(d))/(2*a)
        print ("A única raiz é", raiz1)
    else:
        if d<0:
            print ("Essa equação não possui raízes reais.")
        else:
            raiz1 = (-b + math.sqrt(d))/(2*a)
            raiz2 = (-b - math.sqrt(d))/(2*a)
            print ("A primeira raíz é", raiz1)
            print ("A segunda raíz é", raiz2)

main ()