class Zwierze:
    def __init__(self, nazwa, gatunek, waga):
        self.nazwa=nazwa
        self.gatunek=gatunek
        self.waga=waga
    
    def zbadaj(self):
        print('Nazwa:', self.nazwa)
        print('Gatunek:', self.gatunek)
        print('Waga:', self.waga, 'gram')


z1=Zwierze('pimpek', 'kot', '1500')
z1.zbadaj()