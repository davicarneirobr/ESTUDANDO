# conceito 1:
# atribuicao a lista de valores

x = 10
x, y = 10, 20
print (y)

def peso_e_altura ():
    return 77, 1.83

peso, altura = peso_e_altura()
print (peso)
print (altura)

a = 10
b = 20
a, b = b, a 
print (a)
print (b) # essa caracteristica de trocar a atribuicao pode ser util para vaser o complemento de dna rna
# pq pode tentar nao precisar fazer uma variavel intermediaria

# conceito 2:
# Atribuicao aumentada

x = 10
x = x + 10
# forma abreviada para fazer a mesma coisa:
x += 10 # faz a mesma coisa da linha anterior da anterior
x *= 2 
x = 2
x **=10 # seria 2^10, ou seja, serve para varios operadores

# conceito 3:
# Valores padrao para parametros (parametros opcionais e obrigatorios)

def pagamento_semanal (valor_hora, num_horas):
    return valor_hora * num_horas

pagamento_semanal (100, 36)

# vamos supor que eu quase sempre chame essa funcao com 40h semanais (num_horas = 40)
# o que podemos fazer é usar o conceito de valor padrao para um parametro

def pagamento_semanal2 (valor_hora, num_horas=40):
    return valor_hora * num_horas

print (pagamento_semanal2 (100, 36))
print (pagamento_semanal2 (200)) # ou seja, ele toma o 40 como padrao, caso eu nao coloque nada
# por regra, o parametro opcional tem que fical no fim da listra de parametro
# ou seja, os opicionais sempre no final

# conceito 4:
# Assercao de invariantes (comando assert)

def pagamento_semanal (valor_hora, num_horas):
    # ambas variaveis tem que ser positivas, pq nao existe hora negativ
    # se alguem inserir valor negativo, seria bom que a funcao travasse, desse erro
    # para isso podemos fazer:
    assert valor_hora >= 0 and num_horas >= 0 # ele ta conferindo
    return valor_hora * num_horas

# se eu colocasse pagamento_semanal (-10, 20) ele vai dar mensagem no terminal de AssertionError