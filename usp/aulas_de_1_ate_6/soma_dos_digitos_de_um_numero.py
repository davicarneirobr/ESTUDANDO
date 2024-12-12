x = int(input("Digite um número inteiro que você deseja que se some os algarismos:"))
soma = 0
while ((x // 10)!=0) or ((x % 10)!=0):
   n = x % 10
   soma = soma + n
   x = (x//10)
print ("A soma dos algarismos do número digitado é", soma)