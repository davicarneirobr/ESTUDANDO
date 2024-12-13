def assinatura_tres(texto):
    # Parte 1 - Lista de sentenças
    lista_de_sentencas = separa_sentencas(texto)
    
    # Parte 2 - Soma dos caracteres das sentenças (sem os caracteres de separação)
    soma_de_caracteres_da_sentenca = sum(len(sentenca.strip()) for sentenca in lista_de_sentencas)
    
    # Parte 3 - Número de sentenças
    numero_de_sentencas = len(lista_de_sentencas)
    
    # Calcula o valor da assinatura três
    valor_assinatura_tres = soma_de_caracteres_da_sentenca / numero_de_sentencas
    return valor_assinatura_tres


