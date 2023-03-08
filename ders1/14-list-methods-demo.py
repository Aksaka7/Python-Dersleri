names = ['Ali', 'Yağmur', 'Hakan', 'Deniz']
years = [1998, 2000, 1995, 1987, 1571, 1998, 2023, 1988, 1998]

# 1-  "Cenk" ismini listenin sonuna ekleyiniz.
names.append("Cenk")


# 2-  "Sena" değerini listenin başına ekleyiniz.
names.insert(0, "Sena")
names.insert(5, "Seda")
names.insert(3, "Nisa")
names.insert(2, "Layane")

# 3-  "Deniz" ismini listeden siliniz.
names.pop(1)
# names.pop(4)
# names.remove("Deniz")
# names.remove("Eren")
# print(names)


# 4-  "Deniz" isminin indeksi nedir

value = names.index("Deniz")

# value = names.index("Deniz")
# silinen_oge = names.pop(value)
# print(silinen_oge)

# 5-  "Ali" listenin bir elemanı mıdır ?

# evet = names.count("Ali")
# print(evet)
# # print(result)


# 6-  Liste elemanlarını ters çevirin.
# names.reverse()
names.reverse()


# 7-  Liste elemanlarını alfabetik olarak sıralayınız.

names.sort()
print(names)

# print(names)

# 8-  years listesini rakamsal büyüklüğe göre sıralayınız.

years.sort()
years.reverse()
print(years)
# print(years)

# 9-  str = "Chevrolet,Dacia" karakter dizisini listeye çeviriniz.

cars = []
str = "Chevrolet,Dacia"
cars = str.split(",")
print(cars)


# 10- years dizisinin en büyük ve en küçük elemanı nedir ?
en_Buyuk = max(years)
en_kucuk = min(years)

# print(min(years))
# print(max(years))

# 11- years dizisinde kaç tane 1998 değeri vardır ?
result = years.count(1998)
print(result)
# result = years.count(1998)
# print(result)

# 12- years dizisinin tüm elemanlarını siliniz.
years.clear()
# years.clear()

# 13- Kullanıcıdan alacağınız 3 tane marka bilgisini bir listede saklayınız.
# marka1 = input("Bir araba markası giriniz: ")
# marka2 = input("Bir araba markası giriniz: ")
# marka3 = input("Bir araba markası giriniz: ")

# markalar = [marka1,marka2,marka3]

marka1 = input("Bir araba markası giriniz")
marka2 = input("Bir araba markası giriniz")
marka3 = input("Bir araba markası giriniz")

cars.append(marka1)
cars.append(marka2)
cars.append(marka3)

print(cars)
