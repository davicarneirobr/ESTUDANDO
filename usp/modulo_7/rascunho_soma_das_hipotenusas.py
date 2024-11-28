#pensamentos avulsos:
#podemos escreever a hipotenusa "c" como c = m^2 + n^2, onde m e n são primos entre si
#logo, qualquer dupla de primo entre si dá c

import math

def primo_entre_si(m, n):
    return math.gcd(m, n) == 1
