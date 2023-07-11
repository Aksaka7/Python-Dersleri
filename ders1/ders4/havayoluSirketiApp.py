from datetime import datetime
import random


# "==========================CLASSES============================"


class City:
    def __init__(self, isim):
        self.__isim = isim
        self.__sicaklik = random.randint(18, 25)
        self.__havaDurumu = ['Açık', 'Kapalı', 'Yağmurlu',
                             'Sağank Yağışlı'][random.randint(0, 3)]

    def getIsim(self):
        return self.__isim

    def getSicaklik(self):
        return self.__sicaklik

    def getHavaDurumu(self):
        return self.__havaDurumu

    def setSicaklik(self, sicaklik: int):
        self.__sicaklik = sicaklik

    def setHavaDurum(self, durum):
        if durum not in ['Açık', 'Kapalı', 'Yağmurlu', 'Sağank Yağışlı']:
            pass
        else:
            self.__havaDurumu = durum

    def __str__(self):
        return self.__isim


class Ucus:
    def __init__(self, nereden: City, nereye: City, tarih: datetime):
        self.__nereden = nereden
        self.__nereye = nereye
        self.__tarih = tarih

    # Buraya GElecek olan VEri Dakika verisidir.

    def rotar(self, neKadar: int):
        day = self.__tarih.day
        hour = self.__tarih.hour  # 7
        minute = self.__tarih.minute  # 40

        if (minute + neKadar) >= 60:
            hour += int((minute + neKadar) / 60)
            minute = (minute + neKadar) % 60

            if (hour >= 24):
                day += int(hour / 24)
                hour = hour % 24

        newDate = datetime(self.__tarih.year,
                           self.__tarih.month, day, hour, minute)
        self.__tarih = newDate

    def getTarih(self):
        return self.__tarih

    def getNereden(self):
        return self.__nereden

    def getNereye(self):
        return self.__nereye


class Yolcu:
    def __init__(self, isim: str, soyisim: str, tcno: int):
        self.__isim = isim
        self.__soyisim = soyisim
        self.__tcno = tcno

    def getIsim(self):
        return self.__isim

    def getSoyisim(self):
        return self.__soyisim

    def getTc(self):
        return self.__tcno


class Bilet:

    def __init__(self, yolcu: Yolcu, ucus: Ucus, koltukNumarasi: str):
        self.__yolcu = yolcu
        self.__ucus = ucus
        self.__koltukNo = koltukNumarasi

    def __str__(self):
        str_ = """
        isim:       \t{}
        Soyisim:    \t{}
        T.C:        \t{}
        Uçus Tarihi:\t{}
        Uçus Saati: \t{}
        Nereden:    \t{}
        Nereye:     \t{}
        Koltuk No:  \t{}
        """.format(self.__yolcu.getIsim(), self.__yolcu.getSoyisim(), self.__yolcu.getTc(), self.__ucus.getTarih().date(), self.__ucus.getTarih().time(), self.__ucus.getNereden(), self.__ucus.getNereye(), self.__koltukNo)

        return str_

    def getUcus(self):
        return self.__ucus


class Pegasus:
    def __init__(self):
        self.__aktifBiletler = []
        self.__gecmisBiletler = []
        self.__aktifUcuslar = []
        self.__gecmisUcuslar = []

    def biletAl(self, yolcu: Yolcu, ucus: Ucus, koltukNumarasi: str):
        if ucus in self.__aktifUcuslar:
            bilet = Bilet(yolcu, ucus, koltukNumarasi)
            self.__aktifBiletler.append(bilet)
            return bilet

    def ucusOlustur(self, nereden: City, nereye: City, tarih: datetime):
        ucus = Ucus(nereden, nereye, tarih)
        self.__aktifUcuslar.append(ucus)
        return ucus

    def biletIptal(self, bilet: Bilet):  # PEki Aktif biletler içerisinde biletler varmı ?
        if bilet in self.__aktifBiletler:
            self.__aktifBiletler.remove(bilet)

    def ucusGerceklesti(self, ucus: Ucus):  # Hangi Uçuş?
        for bilet in self.__aktifBiletler:
            if bilet.getUcus() == ucus:  # Bu uçuşa alınmış ise bu biletler aşagıdaki işlmeleri yap
                self.__aktifBiletler.remove(bilet)
                self.__gecmisBiletler.append(bilet)

        self.__aktifUcuslar.remove(ucus)
        self.__gecmisUcuslar.append(ucus)

    def rotar(self, ucus: Ucus, dakika: int):
        return ucus.rotar(dakika)

# ==================================================================


def Main():
    s = """ADANA
    ADIYAMAN
    AFYONKARAHİSAR
    AĞRI
    AMASYA
    ANKARA
    ANTALYA
    ARTVİN
    AYDIN
    BALIKESİR
    BİLECİK
    BİNGÖL
    BİTLİS
    BOLU
    BURDUR
    BURSA
    ÇANAKKALE
    ÇANKIRI
    ÇORUM
    DENİZLİ
    DİYARBAKIR
    EDİRNE
    ELAZIĞ
    ERZİNCAN
    ERZURUM
    ESKİŞEHİR
    GAZİANTEP
    GİRESUN
    GÜMÜŞHANE
    HAKKARİ
    HATAY
    ISPARTA
    MERSİN
    İSTANBUL
    İZMİR
    KARS
    KASTAMONU
    KAYSERİ
    KIRKLARELİ
    KIRŞEHİR
    KOCAELİ
    KONYA
    KÜTAHYA
    MALATYA
    MANİSA
    KAHRAMANMARAŞ
    MARDİN
    MUĞLA
    MUŞ
    NEVŞEHİR
    NİĞDE
    ORDU
    RİZE
    SAKARYA
    SAMSUN
    SİİRT
    SİNOP
    SİVAS
    TEKİRDAĞ
    TOKAT
    TRABZON
    TUNCELİ
    ŞANLIURFA
    UŞAK
    VAN
    YOZGAT
    ZONGULDAK
    AKSARAY
    BAYBURT
    KARAMAN
    KIRIKKALE
    BATMAN
    ŞIRNAK
    BARTIN
    ARDAHAN
    IĞDIR
    YALOVA
    KARABÜK
    KİLİS
    OSMANİYE
    DÜZCE"""
    sehir = []
    for i in s.split('\n'):
        sehir.append(City(i))

    mehmet = Yolcu('Mehmet', 'Asker', 51665165415)
    pegasus = Pegasus()
    ucus1 = pegasus.ucusOlustur(
        sehir[5], sehir[30], datetime(2023, 4, 20, 5, 45))
    bilet = pegasus.biletAl(mehmet, ucus1, '24E')

    print(bilet)
    pegasus.rotar(ucus1,45)
    print(bilet)


# Bu istemde İmport oldugunda yapılan işlem kopyalanmasın diye MAİN fonksiyonu yapılandırıldı.
if __name__ == '__main__':
    Main()


# bilet1 = Bilet(Yolcu('Mehmet', 'Aşker', 15164212023), Ucus(
#     'Malta', 'Amsterdam', datetime(2023, 4, 20, 5, 45)), '45E')

# print(bilet1)
