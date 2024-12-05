lista = []
novo_inteiro = 1
while novo_inteiro != 0:
    novo_inteiro = int(input("Digite um número:"))
    if novo_inteiro != 0:
        lista.append (novo_inteiro)

lista.sort (reverse=True)

for inteiro in lista:
    print (inteiro)