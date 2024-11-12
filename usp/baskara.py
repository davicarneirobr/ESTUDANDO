import math
a=float(input("Qual o valor de a?"))
b=float(input("Qual o valor de b?"))
c=float(input("Qual o valor de c?"))
delta=b*b-(4*a*c)
if delta<0:
    print("Essa equacao nao tem soluções reais, apenas imaginárias.")
else:
    if delta==0:
        x=-b/2*a
        print("A solução dessa equacao é x igual a", x)
    else:
        x1=-b+(math.sqrt(delta))
        x2=-b-(math.sqrt(delta))
        print("A solucoes dessa equação são x1 igual a", x1, "e x2 igual a ", x2)