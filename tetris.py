class Blok:
    def __init__(self, typ):
        self.typ = typ

dlugosc = 6

for d in range(dlugosc):
    print('|', end='')
    for i in range(20):
        if(d==dlugosc-1): print('_', end='')
        else: print(' ', end='')
    print('|')