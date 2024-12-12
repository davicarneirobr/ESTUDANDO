n = int(input("Digite um número que deseje testar se é primo:"))
x = n - 1
while x>1:
    if n % x == 0:
        print ("não é primo")
        x = 0
    else:
        x = x - 1
if n == 1:
    print ("não é primo")
if x == 1:
    print ("é primo")