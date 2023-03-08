# 1- Kullanıcıdan isim, yaş ve eğitim bilgilerini isteyip ehliyet alabilme

# name = input("isim Giriniz: ")
# age = int(input("yaş Giriniz: "))
# education = input("eğitim bilgilerini giriniz: ")

# if age >= 18:
#     print(f"Kullanıcı {name} 18 yaşından Büyüktür")
#     if (education == "Lise" or education == "University"):
#         print(f" Tester {education} mezunu oldugu için Ehliyet alabilir...")
#     else:
#         print(f" Tester {education} mezunu oldugu için Ehliyet alamaz....")
# else:
#     print(f" Tester {name} 18 yaşından küçük oldugu için Ehliyet alamaz...")


# 2- Bir öğrencinin 2 yazılı bir sözlü notunu alıp hesaplanan ortalamaya göre

# birinci_yazili_Notu = float(input("Birinci yazılı Notunu giriniz: "))
# ikinci_yazili_Notu = float(input("İkinci yazılı Notunu giriniz: "))
# sozlu_yazili_Notu = float(input("Sözlü Notunu giriniz: "))

# ortalama = (birinci_yazili_Notu + ikinci_yazili_Notu + sozlu_yazili_Notu) / 3

# if (ortalama >= 0) and (ortalama <= 25):
#     print(f"Ortalamanız: ({ortalama}) notunu<: 0")
# elif (ortalama >= 25) and (ortalama <= 45):
#     print(f"Ortalamanız: {ortalama} notunu<: 1")
# elif (ortalama >= 45) and (ortalama <= 55):
#     print(f"Ortalamanız: {ortalama} Notunuz: 2")
# elif (ortalama >= 55) and (ortalama <= 69):
#     print(f"Ortalamanız: {ortalama} Notunuz: 3")
# elif (ortalama >= 70) and (ortalama <= 85):
#     print(f"Ortalamanız: {ortalama} Notunuz: 4")
# elif (ortalama >= 85) and (ortalama <= 100):
#     print(f"Ortalamanız: {ortalama} Notunuz: 5")
# else:
#     print(f"Yanlış bilgi girdiniz...")

# 3- Trafiğe çıkış tarihi alınan bir aracın servis zamanını aşağıdaki bilgilere
#    göre hesaplayınız.
#    1. Bakım => 1. yıl
#    2. Bakım => 2. yıl
#    3. Bakım => 3. yıl
#    ** Süre hesabını alınan gün, ay, yıl bilgisine göre gün bazlı hesaplayınız..
#    *** datetime modülünü kullanmanız gerekiyor.
#    (simdi) - (2022/11/1) => gü

import datetime

tarih = input("Araç hangi tarihte Trafige çıktı (2019/8/9): ")
tarih = tarih.split("/")

trafige_Cikis = datetime.datetime(int(tarih[0]), int(tarih[1]), int(tarih[2]))
simdi = datetime.datetime.now()

fark = simdi - trafige_Cikis
print(fark)
days = fark.days


if days <= 365:
    print("1. Servis aralıgı")
elif days > 365 and days <= 365*2:
    print("2. Servis aralıgı")
elif days > 365*2 and days <= 365*3:
    print("3. Servis aralıgı")
else:
    print("Hataylı Süre Bilgisi")
