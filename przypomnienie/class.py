class Zwierze:
    def __init__(self, nazwa, gatunek, waga):
        self.nazwa=nazwa
        self.gatunek=gatunek
        self.waga=waga
    
    def zbadaj(self):
        print('Nazwa:', self.nazwa)
        print('Gatunek:', self.gatunek)
        if(self.waga>=1000000): print('Waga:', self.waga/1000000, 'ton')
        elif(self.waga>=1000): print('Waga:', self.waga/1000, 'kilogram')
        else: print('Waga:', self.waga, 'gram')



Farma = [Zwierze('puszek', 'pies', 1500), Zwierze('antonina', 'krowa', 1000000), Zwierze('ben', 'chomik', 100)]

Farma[0].zbadaj()

print('-----------------------------------------------------')

for i in Farma:
    i.zbadaj()

print('-----------------------------------------------------')

tab = []

for i in range(len(Farma)):
    tab.append(Farma[i].nazwa) #MOŻNA WSTAWIĆ TEŻ GATUNEK I WAGA

print(tab)
tab=sorted(tab)
print(tab)

print('-----------------------------------------------------')

