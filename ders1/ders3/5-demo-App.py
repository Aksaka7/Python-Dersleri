import datetime


class Karakter():
    def __init__(self, can, guc):
        self.can = can
        self.guc = guc

    def vur(self, rakip):
        rakip.can -= self.guc


x = Karakter(70, 40)
y = Karakter(100, 50)

print(f"Bİrinci Durum {x.can}")

y.vur(x)

print("<-----Bu Konu Geliştirile bilir----->")

print(f"Ikinci Durum {x.can}")


class Kitap():
    def __init__(self, yazar, isim, basimTarihi: datetime, sayfaSayisi):
        self.yazar = yazar
        self.basimTarihi = basimTarihi
        self.isim = isim
        self.sayfaSayisi = sayfaSayisi


xx = Kitap("Paulo Coelho", "Simyacı", datetime.date(2018, 3, 21), 140)


print(xx.basimTarihi)
