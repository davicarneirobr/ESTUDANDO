from Bio import SeqIO

def contando_c_g(seq):
    # Conta o número de G's e C's e calcula a porcentagem
    gc_contado = seq.count("G") + seq.count("C")
    return gc_contado / len(seq) * 100

def processando_fasta(caminho_arquivo):
    # Usando SeqIO para ler o arquivo FASTA
    seqs = {}
    for record in SeqIO.parse(caminho_arquivo, "fasta"):
        seqs[record.id] = str(record.seq)  # Armazena o ID e a sequência
    return seqs

def encontrar_maior_gc(seqs):
    maior_gc = 0
    id_maior_gc = ""
    for id_seq, seq in seqs.items():
        gc = contando_c_g(seq)
        if gc > maior_gc:
            maior_gc = gc
            id_maior_gc = id_seq
    return id_maior_gc, maior_gc

# Caminho do arquivo FASTA
caminho_arquivo = "/Users/davicarneiro.br/Downloads/rosalind_gc.txt"

# Processa o arquivo FASTA
seqs = processando_fasta(caminho_arquivo)

# Encontra a sequência com maior GC
id_maior_gc, maior_gc = encontrar_maior_gc(seqs)

# Exibe o resultado
print(f"{id_maior_gc}\n{maior_gc:.3f}")
