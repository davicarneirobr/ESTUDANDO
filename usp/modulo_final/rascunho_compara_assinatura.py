def compara_assinatura(as_a, as_b):
    valor0 = abs(as_a[0] - as_b[0])
    valor1 = abs(as_a[1] - as_b[1])
    valor2 = abs(as_a[2] - as_b[2])
    valor3 = abs(as_a[3] - as_b[3])
    valor4 = abs(as_a[4] - as_b[4])
    valor5 = abs(as_a[5] - as_b[5])
    valor_similar = (valor0 + valor1 + valor2 + valor3 + valor4 + valor5) / 6
    return valor_similar