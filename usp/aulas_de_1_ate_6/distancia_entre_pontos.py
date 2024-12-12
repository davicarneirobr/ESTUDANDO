import math
x=float(input("Digite a coordenada x do primeiro ponto:"))
y=float(input("Digite a coordenada y do primeiro ponto:"))
z=float(input("Digite a coordenada x do segundo ponto:"))
w=float(input("Digite a coordenada y do segundo ponto:"))
d0=(x-z)**2+(y-w)**2
d=math.sqrt(d0)
if d>=10:
    print("longe")
else:
    print("perto")