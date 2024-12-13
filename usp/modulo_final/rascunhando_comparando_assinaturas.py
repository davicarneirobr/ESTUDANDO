def avalia_textos(textos, ass_cp):
    ass_cp = le_assinatura()
    textos = le_textos()
    lista_de_assinaturas_de_cada_texto_inserido = []
    lista_de_valores_de_similaridade = []
    for texto in textos:
        assinatura = calcula_assinatura(texto)
        lista_de_assinaturas_de_cada_texto_inserido.extend (assinatura)
    for assinaturas in lista_de_assinaturas_de_cada_texto_inserido:
        valor_de_similaridade = compara_assinatura (assinaturas, ass_cp)
        lista_de_valores_de_similaridade.extend (valor_de_similaridade)
    maior_similaridade = min(lista_de_valores_de_similaridade)
    posicao_na_lista_de_valores_de_similaridade = lista_de_valores_de_similaridade.index(maior_similaridade) + 1
    return posicao_na_lista_de_valores_de_similaridade
    