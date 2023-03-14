# import random

# sayi_Uret = random.randint(1, 10)

# hak = 5
# sayac = 0
# while hak > 0:
#     hak -= 1
#     sayac += 1
#     tahmin = int(input("Tahmin: "))

#     if sayi_Uret == tahmin:
#         print(
#             f"Teprikler {sayac}. defada Bildiniz. Başarı puanı: {100 - (20)*(sayac-1)} ")
#         break
#     elif sayi_Uret > tahmin:
#         print("Lütfen Tahmin sayısını Yükseltin")
#     else:
#         print("Lütfen tahmin sayısını Düşürün")


# Soru Girilen bir sayının Asal sayı olup olmadıgını bulun.
# Asal sayi 1 ve kendisi hariç tam böleni olmayan sayılara denir

sayi = int(input("Sayi Gir: "))
asalMi = True
if sayi == 1:
    print("1 Sayısı Asal degildir.")

for i in range(2, sayi):
    if (sayi % i == 0):
        asalMi = False
        break
if asalMi:
    print("Sayı Asal sayıdır. ")
else:
    print("Sayı Asal sayı degildir.")
