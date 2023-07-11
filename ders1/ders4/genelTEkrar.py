# # name = input("Adinizi Giriniz: ")
# # surname = input("Soyadını Giriniz: ")
# # age = int(input("Yaşınızı Giriniz: "))
# # okul = input("Okulunuzu Giriniz: ")
# # sinif = input("Sınıfınızı Giriniz: ")

# # print(
# #     f"Merhaba Ben {name} {surname}, {age} yaşında, {okul} okulu {sinif} sınıfında Okudum")


# # ahmet, ayse, fatma, hayriye = 155, 160, 140, 145

# # ortalama = (ahmet + ayse + fatma + hayriye) / 4

# # print(ortalama)

# # mac1 = int(input(" 1 Mac score: "))
# # mac2 = int(input(" 2 Mac score: "))
# # mac3 = int(input(" 3 Mac score: "))
# # mac4 = int(input(" 4 Mac score: "))
# # mac5 = int(input(" 5 Mac score: "))

# # ortama = (mac1 + mac2 + mac3 + mac4 + mac5) / 5

# # print(ortama)

# # Dikdorgenin Alanı

# # alan = int(input("uzun Kenar Gir: "))
# # h = int(input("yükseklik Gir: "))

# # result = alan * h

# # print(result)

# # Daire Alanı

# # pi = 3.14

# # r = int(input("Lütfen Yarıçapı giriniz:  "))

# # alan = pi * r*r
# # cevre = 2*pi*r

# # print(f"Girilen dairenin Alanı: {alan},  Cevresi: {cevre}")

# # TEkmi Çiftmi
# # num = int(input("Sayı Gir: "))

# # kalan = num % 2

# # if kalan == 0:
# #     print("Bu sayi cifttir: " + str(num))
# # else:
# #     print("Bu sayi tektir: " + str(num))


# # servisbedeli = 200
# # ogrencisayi = 30

# # gun = int(input("Hafta için: 1 -  Hafta sonu: 2"))

# # if (gun == 1):
# #     ticketPrice = 8
# # else:
# #     ticketPrice = 12.5

# # genelToplam = ogrencisayi * ticketPrice + servisbedeli

# # print(f" Genel Toplam: {genelToplam}")


# # # Askerlik örnegi
# # age = int(input("Yaşınızı Giriniz: "))
# # genger = input("Cinsiyetiniz Giriniz: ")

# # if genger == "Kadın":
# #     print("Kadınlar için Zorunlu Askerlik gorevi yoktur")
# # elif age >= 20 and genger == 'Erkek':
# #     print("Askere gitmelisin")
# # elif age < 20 and genger == 'Erkek':
# #     print("Henüz Askerlik Yaşın gelmedi")

# # İETT Otobüs Kimlere Ücretsiz

# # age = int(input("Lütfen Yaşınızı giriniz: "))

# # if age <= 6 or age >= 65:
# #     print("İETT Otobüslerinden Ücretsiz Faydalanabilirsiniz. ")
# # else:
# #     print("Ücret ödemeniz gerekmektedir.")

# # Sayi Tahmini
# # import random

# # randomsayi = random.randint(1, 100)

# # tahminim = 0

# # while tahminim != randomsayi:
# #     tahminim = int(input("Sayi gir: "))

# #     if tahminim > randomsayi:
# #         print("Tutulan sayi Daha küçük")

# #     if tahminim < randomsayi:
# #         print("Tutulan sayi daha büyük")


# # print(f"Tebrikler Sayıyı buldun {randomsayi}")


# # Hesap Makinesi

# while (True):
#     print("-"*30)
#     print("(1) Topla \n(2)Çıkar \n(3) Çarp \n(4) Böl")
#     print("(0) Çık")
#     print("-" * 30)

#     islem = int(input("Lütfen İşlem numarasını belirtiniz: "))

#     if islem == 0:
#         print("İşlemler Bitmiştir.")
#         break
#     elif islem == 1:
#         sayi1 = int(input("Sayi gir: "))
#         sayi2 = int(input("Sayi gir: "))
#         sonuc = sayi1 + sayi2
#         print(f"{sayi1} + {sayi2} = {sonuc}")
#     elif islem == 2:
#         sayi1 = int(input("Sayi gir: "))
#         sayi2 = int(input("Sayi gir: "))
#         sonuc = sayi1 - sayi2
#         print(f"{sayi1} - {sayi2} = {sonuc}")
#     elif islem == 3:
#         sayi1 = int(input("Sayi gir: "))
#         sayi2 = int(input("Sayi gir: "))
#         sonuc = sayi1 * sayi2
#         print(f"{sayi1} * {sayi2} = {sonuc}")
#     elif islem == 4:
#         sayi1 = int(input("Sayi gir: "))
#         sayi2 = int(input("Sayi gir: "))
#         sonuc = sayi1 / sayi2
#         print(f"{sayi1} / {sayi2} = {sonuc}")
#     else:
#         print("Yanlış işlem numarası girdiniz")

# # Daire çiz

# # import turtle

# # turtle.pensize(7)
# # turtle.bgcolor('blue')
# # turtle.pencolor('white')

# # for i in range(360):
# #     turtle.forward(1)
# #     turtle.left(2)


# class Kitap:
#     def __init__(self, yazar, isim, sayfaSayisi: int):
#         self.__yazar = yazar
#         self.__isim = isim
#         self.__sayfaSayisi = sayfaSayisi

#     def getyazar(self):
#         return self.__yazar

#     def getIsim(self):
#         return self.__isim

#     def getSayfaSayisi(self):
#         return self.__sayfaSayisi

#     def __str__(self):
#         return f"Yazarın Adı Soyadı: {self.__yazar}, Kitap Adı: {self.__isim}, Sayfa sayısı: {self.__sayfaSayisi} "


# x = Kitap("Paulo Coelho", "Aldatmak", 250)

# print(str(x))

