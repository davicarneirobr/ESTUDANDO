#pensamentos avulsos:
#podemos escreever a hipotenusa "c" como c = m^2 + n^2, onde m e n são primos entre si
#logo, qualquer dupla de primo entre si dá c

import math

def primo_entre_si(m, n):
    return math.gcd(m, n) == 1

#pensamentos avulsos 2:
#os ternos primitivos são sempre formados por 
#a = impares na sequencia (3,5,7,9,11,13,...)
#com b e c sendo consecutivos (c = b+1)
#e todo a (impar) vai ter um terno!
#outra coisa q todos esses ternos primitivos vao ter secundarios na forma (a*k, b*k, c*k) (OBVIAMENTE)
