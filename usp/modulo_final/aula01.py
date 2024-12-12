def MinMax (temperaturas):
    print ("A menor temperatura do mês foi", minima(temperaturas), "oC")
    print ("A maior temperatura do mês foi", maxima(temperaturas), "oC")

def minima(temps):
    min = 0
    i = 0
    while i < len(temps):
        if temps[i] < min:
            min = temps[i]
        i = i + 1
    return min