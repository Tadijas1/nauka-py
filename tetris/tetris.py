class Blok:
    def __init__(self, typ, wysokosc, miejsce):
        self.typ = typ
        self.jakaWysokosc = wysokosc
        self.jakieMiejsce = miejsce

wysokosc = 10
dlugosc = 20
blok = Blok(1, wysokosc, dlugosc/2)

def pokaz(y, x):
    if(y>=blok.jakaWysokosc):
        if(x<=blok.jakieMiejsce+6):
            print('-')
    elif(y==blok.jakaWysokosc-1):
        if(x==blok.jakieMiejsce):
            print('|')
        if(x==blok.jakaWysokosc+4):
            print('|')
    else: print(' ', end='')

for d in range(wysokosc, 0, -1):
    print('|', end='')
    for i in range(dlugosc):
        if(d==1): print('_', end='')
        else: pokaz(d, i)
    print('|')



# print('---')
# print('| |')
# print('| |')
# print('---')

# print('------')
# print('|    |')
# print('------')