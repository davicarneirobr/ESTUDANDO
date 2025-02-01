def finding_motif (strand, motif):
    motif_positions = []
    for i in range(len(strand)):
        if strand[i:i+len(motif)] == motif:
            motif_positions.append(i+1)
    return motif_positions


