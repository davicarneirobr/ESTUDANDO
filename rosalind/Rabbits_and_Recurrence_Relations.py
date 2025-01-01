def total_de_coelhos(n, k):
    assert n <= 40
    assert k <= 5
    if n <= 0:
        return "Error"
    elif n == 1:
        return 1
    elif n == 2:
        return 1
    sequencia_de_geracoes = [1, 1]
    for i in range (2, n):
        novo_termo = sequencia_de_geracoes[-1] + k * sequencia_de_geracoes[-2]
        sequencia_de_geracoes.append(novo_termo)
    return sequencia_de_geracoes[-1]


print (total_de_coelhos(32,3))