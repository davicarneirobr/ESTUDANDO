# primeiro definindo as funções

#definindo a função usuario_escolhe_jogada
def  usuario_escolhe_jogada (n, m):
    y = int(input("Quantas peças você vai tirar?"))
    while y > m or y > n or y <= 0:
        print("Oops! Jogada inválida! Tente de novo.")
        y = int(input("Quantas peças você vai tirar?"))
    return y

#definindo a função computador_escolhe_jogada
def  computador_escolhe_jogada (n, m):
    if n > m:
        x = 1
        while (n - x) % (m + 1) != 0:
            x = x + 1
        return x
    else:
        x = n
        return x

#definindo a função partida
def partida ():
    n = 0
    x = 0
    y = 0
    if n == 0:
        n = int(input("Quantas peças?"))
        m = int(input("Limite de peças por jogada?"))
        if n % (m + 1) == 0:
            print ("Você começa!")
            y = usuario_escolhe_jogada (n, m)
            n = n - y
            if y == 1:
                    print ("Voce tirou", y, "peça.")
            else:
                    print ("Voce tirou", y, "peças.")
            if n == 1:
                    print ("Agora resta apenas", n, "peça no tabuleiro.")
            else:
                    print ("Agora restam", n, "peças no tabuleiro.")
        if n % (m + 1) != 0:
            print ("Computador começa!")
            x = computador_escolhe_jogada (n, m)
            if x == 1:
                print ("O computador tirou", x, "peça.")
            else:
                print ("O computador tirou", x, "peças.")
            n = n - x
            if n == 1:
                print ("Agora resta apenas", n, "peça no tabuleiro.")
            else:
                print ("Agora restam", n, "peças no tabuleiro.")
    while n != 0:
        if n % (m + 1) == 0:
            y = usuario_escolhe_jogada (n, m)
            if y == 1:
                print ("Voce tirou", y, "peça.")
            else:
                print ("Voce tirou", y, "peças.")
            n = n - y
            if n == 1:
                print ("Agora resta apenas", n, "peça no tabuleiro.")
            else:
                print ("Agora restam", n, "peças no tabuleiro.")
        if n % (m + 1) != 0:
            x = computador_escolhe_jogada (n, m)
            if x == 1:
                print ("O computador tirou", x, "peça.")
            else:
                print ("O computador tirou", x, "peças.")
            n = n - x
            if n == 1:
                print ("Agora resta apenas", n, "peça no tabuleiro.")
            else:
                print ("Agora restam", n, "peças no tabuleiro.")
    if n == 0:
        print ("Fim do jogo! O computador ganhou!")

#definindo a função campeonato
def campeonato():
    print ("**** Rodada 1 ****")
    partida ()
    print ("**** Rodada 2 ****")
    partida ()
    print ("**** Rodada 3 ****")
    partida ()
    print ("**** Final do campeonato! ****")
    print ("Placar: Você 0 X 3 Computador")

#INICIALIZANDO O JOGO:
print ("Bem-vindo ao jogo do NIM! Escolha:")
print ("1 - para jogar uma partida isolada")
print ("2 - para jogar um campeonato")

#ESCOLHENDO JOGO ÚNICO OU CAMPEONATO
escolha = int(input())
if escolha == 1:
    partida()
if escolha == 2:
    campeonato()