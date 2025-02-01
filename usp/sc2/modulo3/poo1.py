# criando uma classe vazia
class Carro:
    pass

# criar uma instância / um objeto da classe Carro
meu_carro = Carro()

# vamos criar outra instância/objeto da classe Carro
carro_do_ime = Carro() # agora tenho dois objetos do tipo Carro

# atribuindo atributos as variáveis meu_carro e carro_do_ime
meu_carro.ano = 1968
meu_carro.modelo = "Fusca"
meu_carro.cor = "azul"

print (meu_carro.ano)
print (meu_carro.cor)

carro_do_ime.ano = 1981
carro_do_ime.modelo = "Brasília"
carro_do_ime.cor = "amarela"

print (carro_do_ime.ano)
print (carro_do_ime.cor)

# duas variáveis apontando para o mesmo objeto
novo_fusca = meu_carro
novo_fusca.ano += 10
print (novo_fusca.ano)
print (meu_carro.ano) # agoram apontam para o mesmo ano

# logo, podemos definir
# classes
# criar instâncias de classes que são os objetos
# as classes podem ter atributos -> atribuir e resgatar valores a esses atributos

# metodo construtor __init__
# chamado automaticamente quando um objeto é criado

class Carro: # definindo classe carro
    def __init__(self, modelo, ano, cor): # a classe carro tem um método (no init self é o próprio objeto)
        self.modelo = modelo 
        self.ano = ano
        self.cor = cor

carro_do_meu_avo = Carro ("Ferrari", 1980, "vermelha") # criando um objeto carro
print (carro_do_meu_avo.cor)