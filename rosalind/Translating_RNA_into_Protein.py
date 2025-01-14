amino_acids = {
    'F': ["UUU", "UUC"],
    'L': ["CUU", "CUC", "UUA", "CUA", "UUG", "CUG"],
    'I': ["AUU", "AUC", "AUA"],
    'V': ["GUU", "GUC", "GUA", "GUG"],
    'M': ["AUG"],
    'S': ["UCU", "UCC", "UCA", "UCG", "AGU", "AGC"],
    'P': ["CCU", "CCC", "CCA", "CCG"],
    'T': ["ACU", "ACC", "ACA", "ACG"],
    'A': ["GCU", "GCC", "GCA", "GCG"],
    'Y': ["UAU", "UAC"],
    'H': ["CAU", "CAC"],
    'N': ["AAU", "AAC"],
    'D': ["GAU", "GAC"],
    'Stop': ["UAA", "UAG", "UGA"],
    'Q': ["CAA", "CAG"],
    'K': ["AAA", "AAG"],
    'E': ["GAA", "GAG"],
    'C': ["UGU", "UGC"],
    'R': ["CGU", "CGC", "CGA", "CGG", "AGA", "AGG"],
    'G': ["GGU", "GGC", "GGA", "GGG"],
    'W': ["UGG"]
}

def traduzindo (seq_RNA):
    seq_proteina = ''
    for i in range(0, len(seq_RNA), 3):
        codon = seq_RNA[i:i+3]
        for amino_acid in amino_acids:
            if codon in amino_acids[amino_acid]:
                if amino_acid == 'Stop':
                    break
                seq_proteina += amino_acid
                break
    return seq_proteina

def traduzindo(seq_RNA):
    seq_proteina = ''
    for i in range(0, len(seq_RNA), 3):
        codon = seq_RNA[i:i+3]
        for amino_acid in amino_acids:
            if codon in amino_acids[amino_acid]:
                if amino_acid == 'Stop':
                    return seq_proteina
                seq_proteina += amino_acid
                break
    return seq_proteina

def ler_arquivo(filepath):
    with open(filepath, 'r') as file:
        seq_RNA = file.read().strip()
    return seq_RNA

# Caminho para o arquivo de texto na pasta Downloads
filepath = '/Users/davicarneiro.br/Downloads/rosalind_prot.txt'

# Lendo a sequência de RNA do arquivo
seq_RNA = ler_arquivo(filepath)

# Traduzindo a sequência de RNA em proteína
seq_proteina = traduzindo(seq_RNA)

print(seq_proteina)


