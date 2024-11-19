def maximo (x,y,z):
    if x>y or x>z>y:
        return x
    if y>x>z or y>z>x:
        return y
    else:
        return z