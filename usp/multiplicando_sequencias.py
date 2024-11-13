tamanho=int(input("Digite o tamanho de uma sequência de número:"))
i = 0
produto = 1
while i<tamanho:
    valor = int(input("Digite um valor a ser multiplicado:"))
    produto = produto * valor
    i = i + 1
print ("O valor do produto é", produto)