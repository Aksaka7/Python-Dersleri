class Birey:
    def __init__(self, isim: str, soyisim: str, tcno: int):
        self.isim = isim
        self.soyisim = soyisim
        self.tcno = tcno


class Calismayan(Birey):
    pass


class Calisan(Birey):
    def __init__(self, isim: str, soyisim: str, tcno: int, idno: int, maas: int):
        Birey.__init__(self, isim, soyisim, tcno)
        self.idno = idno
        self.maas = maas

    def zam(self, deger):
        self.maas += deger


class Muhendis(Calisan):
    def __init__(self, isim: str, soyisim: str, tcno: int, idno: int, maas: int, yazilimDilleri: tuple, yabanci_Diller: tuple, bilinenProgrmlar: tuple
                 ):
        Calisan.__init__(self, isim, soyisim, tcno, idno, maas)
        self.yazilimDilleri = yazilimDilleri
        self.yabanci_Diller = yabanci_Diller
        self.bilinenProgrmlar = bilinenProgrmlar

# yazılım dilleri
# yabanci dilleri
# bilinen programlar


class Muhasebeci(Calisan):
    def __init__(self, isim: str, soyisim: str, tcno: int, idno: int, maas: int, bilinen_programlar: tuple):
        Calisan.__init__(self, isim, soyisim, tcno, idno, maas)
        self.bilinen_programlar = bilinen_programlar

# bilinen programlar


x = Muhendis('Mehmet', 'asker', 151521565, 216, 3000, ("Python",
             "Javascript", 'C++',), ('ingilizce', 'Türkçe', 'Portekizce',), ('VS Code',))

y = Muhasebeci('Layane', 'Asker', 5465151665, 542, 1000, ('VS Code',))


print(x.yazilimDilleri)
print(x.maas)
x.zam(560)
print(x.maas)
