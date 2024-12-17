# a mesma notação x == y 

x = "teoria"
y = "pratica"
print (x == y)
print (x != y)

z =  "teoria"

print (x == z)

print (x is z) # string é imutavel, logo x e z apontam para o mesmo lugar da memoria

print (x > y) # na ordem lexicográfica teoria vem depois de pratica
# lexicográfica é a ordem caracter por caracter
# logo, compara a codigo para cada string

print (ord("a")) # codigo da letra a minuscula
print (ord("A")) # codigo da letra A maiuscula