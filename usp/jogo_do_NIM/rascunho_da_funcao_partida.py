#rascunho da funcao partida do jogo do NIM
#LEMBRANDO:

#1o - ela pergunta quem é n e m
#2o - ela decide quem começa o jogo
#3o - ela é responsável por chamar as função computador_escolhe_jogada ou usuario (COM WHILE)
#4o - ela é quem atualiza o valor de "n"
#5o - ela identifica n == 0 e vê que o jogo acabou

def partida ():
    n = 0
    if n == 0:
        n = int(input("Quantas peças?"))
        m = int(input("Limite de peças por jogada?"))
        if n % (m + 1) == 0:
            print ("Você começa!")
            usuario_escolhe_jogada (n, m)
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
            print ("Computador começa!")
            computador_escolhe_jogada (n, m)
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
            usuario_escolhe_jogada (n, m)
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
            computador_escolhe_jogada (n, m)
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
        print ("Fim do jogo!")