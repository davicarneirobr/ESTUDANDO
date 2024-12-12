n = int(input("Digite um número inteiro:"))
x = n - 1
while x>1:
    if n % x == 0:
        print ("não primo")
        x = 0
    else:
        x = x - 1
if n == 1:
    print ("não primo")
if x == 1:
    print ("primo")