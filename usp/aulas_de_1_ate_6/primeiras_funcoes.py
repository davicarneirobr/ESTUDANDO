def soma (x, y):
    return x + y
print (soma(10, 20))
print (soma(-20, 100))
print (soma(20*32, soma(3,4)))

def multiplica (w,m,n):
    return w * m * n

print (multiplica(10, 20, soma(2,3)))

def nome_do_seu_time ():
    return "FLAMENGO"

#nao devolve nada

def quieta ():
    x = 10 + 20
    print("O valor calculado é", x)
quieta