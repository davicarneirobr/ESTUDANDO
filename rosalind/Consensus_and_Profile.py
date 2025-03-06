from Bio import SeqIO

arquivo_fasta = "/Users/davicarneiro.br/Downloads/rosalind_cons.txt"

# Lista para armazenar as sequências de DNA
matriz_DNA = []

# Itera pelas sequências de DNA do arquivo FASTA
# e as salva na matriz_DNA
for record in SeqIO.parse(arquivo_fasta, "fasta"):
    matriz_DNA.append(record.seq)

# Cria uma matriz de zeros com 4 linhas e o tamanho da sequência
matriz_perfil = [[0 for i in range(len(matriz_DNA[0]))] for j in range(4)]

# Dicionário para armazenar os nucleotídeos
nucleotideos = {'A': 0, 'C': 1, 'G': 2, 'T': 3}

# Percorre cada coluna (posicao) das sequencias
for i in range(len(matriz_DNA[0])):
    # Contar os nucleotídeos na coluna i
    contador = {'A': 0, 'C': 0, 'G': 0, 'T': 0}

    for seq in matriz_DNA:
        contador[seq[i]] += 1
    
    # Atualizar a matriz de perfil com os contadores
    matriz_perfil[0][i] = contador['A']
    matriz_perfil[1][i] = contador['C']
    matriz_perfil[2][i] = contador['G']
    matriz_perfil[3][i] = contador['T']

# Nomes das linhas da matriz de perfil
nucleotideos_lista = ['A', 'C', 'G', 'T']

fita_consenso = ''
for i in range(len(matriz_DNA[0])):
    coluna = [matriz_perfil[j][i] for j in range(4)]
    indice_max = coluna.index(max(coluna))
    fita_consenso += nucleotideos_lista[indice_max]

# Monta a string formatada da matriz de perfil
matriz_perfil_str = '\n'.join(
    f"{nucleotideos_lista[i]}: {' '.join(map(str, matriz_perfil[i]))}"
    for i in range(4)
)

print(fita_consenso)
print(matriz_perfil_str)