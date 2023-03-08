sayilar = [1, 15, 3, 4, 6, 5, 7, 9, 12, 19, 21]

# 1: sayilar listesini while ile ekrana yazdırın.

# 2: Başlangıç ve bitiş değerlerini kullanıcıdan alıp aradaki tüm tek sayıları yazdırınız.

# 3: 1-100 arasındaki sayıları azalan şekilde yazdırın.


# 4: Kullanıcıdan alacağınız 5 sayıyı ekranda sıralı bir şekilde
#    yazdırın.


# 5: Kullanıcıdan alacağınız sınırsız ürün bilgisini urunler listesi içinde saklayınız.
#    ** ürün sayısını kullanıcıya sorun.
#    ** dictionary listesi yapısı (name, price) şeklinde olsun.
#    ** ürün ekleme işlemi bittiğinde ürünleri ekranda while ile listeleyin.
# urun_adedi = int(input("Kaç adet ürün eklemek istiyorsunuz?: "))
# i = 0
# urunler = []

# while i < urun_adedi:
#     name = input("Ürün ismini giriniz: ")
#     price = input("Ürün fiyatını giriniz: ")
#     urun_sozlugu = {"name": name, "price":price}
#     urunler.append(urun_sozlugu)
#     i += 1

# for urun in urunler:
#     print("---------------------")
#     print(f'Ürün ismi: {urun["name"]} ve ürün fiyatı: {urun["price"]}')
#     print("---------------------")


# <***********************************************************>
# uzunluk = len(sayilar)

# i = 0
# while i < uzunluk:
#     print(sayilar[i])
#     i += 1

# baslangic = int(input("Sayi giriniz: "))
# bitis = int(input("Sayi giriniz: "))

# i = baslangic

# while i < bitis:
#     if (i % 2 != 0):
#         print(i)
#     i += 1

# i = 100
# while i > 0:
#     i -= 1
#     print(i)

# liste = []
# i = 0
# while i < 5:
#     num = int(input("Sayı gir: "))
#     liste.append(num)
#     liste.sort()
#     i += 1

# print(liste)


eklenecek_Urun_Sayisi = int(input("eklenecek_Urun_Sayisini Giriniz: "))
dongu_sayisi = eklenecek_Urun_Sayisi
products = []
i = 0

while i < dongu_sayisi:
    i += 1
    product = input("Ürünleri Ekleyiniz: ")
    price = int(input("Ürün fiyatını Belirtiniz: "))
    urunlerin_rafi = {"name": product, "price": price}
    products.append(urunlerin_rafi)

print(products)


for i in products:
    print(f"Ürünün Adı: {i['name']} ürünün Fiyatı: {i['price']}")
