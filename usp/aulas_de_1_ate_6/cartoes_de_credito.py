MeuCartao = int(input("Digite o número do seu cartão de crédito:"))
CartaoLido = 1
EncontreiMeuCartaoNaLista = False
while CartaoLido != 0 and not EncontreiMeuCartaoNaLista:
    CartaoLido = int(input("Digite o número do próximo cartão de crédito:"))
    if CartaoLido == MeuCartao:
        EncontreiMeuCartaoNaLista = True
if EncontreiMeuCartaoNaLista:
    print("Seu cartão de crédito está na lista.")
else:
    print("Seu cartão de crédito não está na lista.")