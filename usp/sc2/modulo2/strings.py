"amora"
'amora'
# ambas notacoes estao certas
print(type (""))
# "15" + 2  esta incorreta
# para corrigir ai de cima
print(int ("15") + 2) # coverte para inteiro
# ou
print ("15" + str (2))

print ("Legal!" * 3)

time = "Íbis"
print (time [0])
print (time [1])
print (time [2])
print (time [3])
print (time[-1])

# métodos da classe string

print (time.upper()) # converte para letra maiuscula 
print (time.lower()) # converte todos caracteres para minusculo

frase = "ana gosta de banana"

print (frase.capitalize()) # coloca a primeira letra maiuscula

print ("BRAZIL".capitalize()) #deixa só a primeira letra em maiuscula

print (" davicarneiroge@hotmail.com ".strip ()) # retira os espacos em branco do inicio e do fim

print ("ana gosta de banana".count("a"))
print ("ana gosta de banana".count("n")) # count conta quantas vezes apareceu algo

print ("Eu torco para o gremio".replace ("gremio", "flamengo")) # troca algo dentro do string

print ("ana gosta de banana!".capitalize().center(80)) # o center centraliza mas precisa colocar a quantidade de caracteres da linha que vc quer

texto = "Minha terra tem palmeiras onde canta o sabia"

print (texto.find("m"))
print (texto.find("sab"))
print (texto.find("bom"))
print (len(texto))

fruta = "amora"

print (fruta[:4]) 
print (fruta[1:])
print (fruta[2:4])

# EXERCICIO
# escrever uma funcao que recebe uma lista de strings contendo nome de pessoas
# como o parametro e devolve o nome mais curto
# Obs1: a funcao deve ignorar espacos antes e depois dos nomes
# Obs2: a funcao deve capitalizar o nome devolvido


def tirando_espacos (lista_de_nomes):
    lista_de_nome_sem_espacos_em_braco = []
    for nome in lista_de_nomes:
        nome_sem_espacos = nome.strip ()
        lista_de_nome_sem_espacos_em_braco.append (nome_sem_espacos)
    return lista_de_nome_sem_espacos_em_braco

def tirando_espacos_mais_simple(lista_de_nomes):
    return [nome.strip() for nome in lista_de_nomes]

def maior_nome (lista_de_nomes):
    lista_de_nome_sem_espaco = tirando_espacos (lista_de_nomes)
    tamanho = 0
    salvando_nome = " "
    for nome_without_espaco in lista_de_nome_sem_espaco:
        tamanho_do_nome = len (nome_without_espaco)
        if tamanho_do_nome > tamanho:
            tamanho = tamanho_do_nome
            salvando_nome = nome_without_espaco
    return salvando_nome.capitalize ()

listando_nomes = ["Maria", "   Davidson", "Me  ", "Jose", "Otorrinolaringologisson  "]

print (len(maior_nome(listando_nomes)))

