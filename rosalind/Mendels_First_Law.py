def recessivos(k, m, n):
    total = k + m + n  # Total de indivíduos
    
    # Probabilidade de cruzamento entre recessivos
    prob_aa_aa = (n / total) * ((n - 1) / (total - 1))
    prob_Aa_aa = (m / total) * (n / (total - 1)) * 0.5 + (n / total) * (m / (total - 1)) * 0.5
    prob_Aa_Aa = (m / total) * ((m - 1) / (total - 1)) * 0.25
    
    # Soma de todas as probabilidades de fenótipo recessivo
    prob_recessivo = prob_aa_aa + prob_Aa_aa + prob_Aa_Aa
    
    # Complemento: probabilidade de não ser recessivo
    prob_nao_recessivo = 1 - prob_recessivo
    
    return prob_nao_recessivo

# Testando a função
print(recessivos(30, 22, 18))  # Exemplo
    