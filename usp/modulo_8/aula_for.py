frutas_exoticas = ["jabuticaba", "cupuacu", "graviola"]

for fruta in frutas_exoticas:
    print ("Eu adoro " + fruta)

print ("")

def éPrimo (x):
    fator = 2
    if x == 2:
        return True
    while x % fator != 0 and fator <= x/2:
        fator = fator + 1
    if x % fator == 0:
        return False
    else:
        return True

primos = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]

for x in primos:
    print (x*x)
print ("")
for i in range(20):
    print (i*i)
print ("")
for i in range(-2,5):
    print (i*i)
print ("")
for i in range(-10,10,2):
    print (i*i)

#lembre-se que pro Python o início é 0, logo, nao imprime o quadrado de +10, é meio que aberto no 10

#to mudando agora o primos para cubo dos primos
for i in range(len(primos)):
    primos[i] = primos [i]**3
cubo_dos_primos = primos
print (cubo_dos_primos)