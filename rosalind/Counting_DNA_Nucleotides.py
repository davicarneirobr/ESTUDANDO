# lembrando!!! 
# No ROSALIND vc deve upar apenas a SAIDA do codigo, e nao o codigo em si
def count_nt (seq):
    num_A = seq.count ("A")
    num_C = seq.count ("C")
    num_G = seq.count ("G")
    num_T = seq.count ("T")
    return print (num_A, num_C, num_G, num_T)

seq = "CGCAAGGCGAGCACGTAGTATCCCCATTAGTCACGAGGGGAAGATGGTCAAAACGGCAGGATTCACTCCCCAGGCCATTGTTCAAGTCTGGGGTCATAAACTTAGCCGGGAATGAAAGGCCGGTACGGATATACTAGTTAGGACATATTATTCAAGGCCACCGTCACTACAGATACCGCTGGTAGTGAACTGATGTAGTACTAAGGCTAGCGTCAGTCGGACATTAAGATCTAGGTAGGATAGTGATGAGCAACCTTGGCTTTAACTTTGAAGGGATTCAATATGCCATTTAAGGGTGGCATGGCGAAGTCCACTATGGGGATTGTTATAGTACGAACACTTAAGCAAGCCTACTACGATAGCAAAAGCCTAACGTGAGCTCTTCGAGTAGTGCTGGTCAGGACCCATTATACCATCCCCGCTTACTCTCCCTCTGTGCAAGTGTTACCTCAGTTGTCATGCGGCGGATAGGGATACGGGGAACGATTGCCTAAATTTAAACGGTGAGGCCATAACCATCCCAATGTTGGGTTCGAAAGAATTTGACTTGAACAAATAATTGTTGCAAATTGGCTGAATTGAGGTCTATAGCCAACCCAGGATTCTCGCTAAATTAGAAAGCCAGTGTCTGGACGGAGCCCACCTATGCCTTGCGACATGAATCCCTTGGAAAATGTAAAATATGCACAGGACGTCCACCTCTCGCGACCTCGATATGGCGGCCGAGCGGTTGCATGACGGCTGGGCGAGGGACCTAACCCGATTATCCACGCAGAAGAAAAGCCCCTTCGCTCGGGAATAAAGGCATGACTGTCCGCCGCGCGGCTCAGCGCCAAGCACCAGCGGGCCCACCATCGACAAAATCTCCGTAGAGTTTAGGGCGAGCCAGTCCTGAGTCGCGCACGACTGTGTTG"

count_nt (seq)