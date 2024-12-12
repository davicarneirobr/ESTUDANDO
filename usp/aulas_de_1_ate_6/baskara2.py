import math
a=float(input("Qual o valor de a?"))
b=float(input("Qual o valor de b?"))
c=float(input("Qual o valor de c?"))
delta=b*b-(4*a*c)
if delta<0:
    print("esta equação não possui raízes reais")
else:
    if delta==0:
        x=-b/2*a
        print("a raiz desta equação é", x)
    else:
        x1=(-b+(math.sqrt(delta)))/2*a
        x2=(-b-(math.sqrt(delta)))/2*a
        print("as raízes da equação são", x2, "e", x1)