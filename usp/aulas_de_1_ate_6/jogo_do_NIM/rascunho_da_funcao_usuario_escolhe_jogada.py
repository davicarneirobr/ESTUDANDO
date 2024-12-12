#rascunho da funcao usuario_escolhe_jogada

def  usuario_escolhe_jogada (n, m):
    y = int(input("Quantas peças você vai tirar?"))
    while y > m or y > n or y == 0:
        print("Oops! Jogada inválida! Tente de novo.")
        y = int(input("Quantas peças você vai tirar?"))
    return y