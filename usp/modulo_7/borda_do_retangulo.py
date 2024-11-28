largura = int(input("digite a largura:"))
largura_i = largura
altura = int(input("digite a altura:"))
altura_i = altura

while altura > 0:
    if altura == altura_i or altura == 1:
        while largura > 0:
            print ("#", end="")
            largura = largura - 1
        print ()
        largura = largura_i
    else:
        while largura > 0:
            if largura == largura_i or largura == 1:
                print ("#", end="")
            else:
                print (" ", end="")
            largura = largura - 1
        print ()
        largura = largura_i
    altura = altura - 1
