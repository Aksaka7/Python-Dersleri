# numbers = []
# for i in range(20):
#     numbers.append(i**2)
# print(numbers)

# numbers = [i*5 for i in range(20) if i % 3 == 0]
# print(numbers)

isim = "Mehmet ASKER"

# listem = []

# for harf in isim:
#     listem.append(harf)

# print(listem)
# listem = [harf.upper() for harf in isim]
# print(listem)
# isimler = ["Layane","Mehmet","Ayşe","Enver"]
# dogum__yillari = [2000,1988,1999,1950]

# tarih = 2023

# yaslar = [tarih - yil for yil in dogum__yillari]
# print(yaslar)


# ABS mutlak değer işlemidir. Negatif sayıları pozitife çevririr ( * -1)
# results = [sayi if sayi % 2 == 0 else abs(sayi) for sayi in range(-10,10)]
# print(results)

liste = []

for i in range(3):
    for j in range(3):
        liste.append((i, j))
        print(str(liste) + " * ")


numbers = [(i, j) for i in range(3) for j in range(3)]

print(numbers)
