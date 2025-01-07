def contando_c_g (seq):
    gc_contado = seq.count("G") + seq.count("C")
    return gc_contado / len (seq) * 100

def processando_fasta (caminho_arquivo):
    # abrindo o arquivo passado no caminho, no modo leitura "r"
    with open(caminho_arquivo, 'r') as f:
        seqs = {}  # Dicionário para armazenar as sequências
        identificador = ''  # Variável para armazenar o identificador da sequência
        dna_seq = ''  # Variável para armazenar a sequência de DNA
        for linha in f:  # Lê o arquivo linha por linha
            linha = linha.strip()  # Remove espaços em branco e quebras de linha no início e no fim
            if linha.startswith('>'):  # Se a linha começar com '>', é um cabeçalho
                if identificador:  # Se já há um identificador registrado
                    seqs[identificador] = dna_seq  # Armazena a sequência anterior no dicionário
                identificador = linha[1:]  # A linha é o cabeçalho, mas sem o '>', então começa a partir do índice 1
                dna_seq = ''  # Limpa a sequência de DNA para começar a armazenar a nova sequência
            else:  # Se não for um cabeçalho, então é uma parte da sequência de DNA
                dna_seq += linha  # Adiciona essa linha à sequência de DNA que estamos montando
        # Ao final, adiciona a última sequência que foi lida no arquivo
        if identificador:
            seqs[identificador] = dna_seq
    return seqs
    
def encontrar_maior_gc (seqs):
    maior_gc = 0
    id_maior_gc = ""
    for id_seq, seq in seqs.items():
        gc = contando_c_g(seq)
        if gc > maior_gc:
            maior_gc = gc
            id_maior_gc = id_seq
    return id_maior_gc, maior_gc

caminho_arquivo = "/Users/davicarneiro.br/Downloads/rosalind_gc-2.txt"
seqs = processando_fasta(caminho_arquivo)
id_maior_gc, maior_gc = encontrar_maior_gc(seqs)

print(f"{id_maior_gc}\n{maior_gc:.3f}")