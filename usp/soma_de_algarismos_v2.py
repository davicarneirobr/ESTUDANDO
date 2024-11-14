x = int(input("Digite um número inteiro:"))
soma = 0
while ((x // 10)!=0) or ((x % 10)!=0):
   n = x % 10
   soma = soma + n
   x = (x//10)
print (soma)