# Sıcak Soguk oyunu ile sayı tahmini oyunu
import random

sicak, soguk, tahmin, hak = 0, 0, 0, 0

can = int(input("Kaç Hak kullanmak istersiniz: "))

sayi = random.randint(1, 100)
sayac = 0
hak = can

print(sayi)
while hak > 0:
    hak -= 1
    sayac += 1
    tahmin = int(input("Tahmin: "))

    if sayi == tahmin:
        print(
            f"Tebrikler {sayac}. defada Bildiniz. Toplam Puan {100 - (100/can) * (sayac-1)}")
        break
    elif sayi > tahmin:
        print("Yukarı ")
    else:
        print("Aşagı")

    if hak == 0:
        print(f"Tahmin Hakkınız bitmiştir. Tutulan sayı: {sayi}")
