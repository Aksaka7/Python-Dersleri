names = ['Ali','Yağmur','Hakan','Deniz']
years = [1998, 2000, 1998, 1987]

# 1-  "Cenk" ismini listenin sonuna ekleyiniz.
names.append("Cenk")
# 2-  "Sena" değerini listenin başına ekleyiniz.
names.insert(0,"Sena")

# 3-  "Deniz" ismini listeden siliniz.
# names.pop(4)
# names.remove("Deniz")
# names.remove("Eren")
# print(names)

# 4-  "Deniz" isminin indeksi nedir ?
# value = names.index("Deniz")
# silinen_oge = names.pop(value)
# print(silinen_oge)

# 5-  "Ali" listenin bir elemanı mıdır ?
result = names.count("Ali")
result = "Ali" in names
# print(result)


# 6-  Liste elemanlarını ters çevirin.
# names.reverse()

# 7-  Liste elemanlarını alfabetik olarak sıralayınız.
names.sort()
# print(names)

# 8-  years listesini rakamsal büyüklüğe göre sıralayınız.
years.sort()
years.reverse()
# print(years)

# 9-  str = "Chevrolet,Dacia" karakter dizisini listeye çeviriniz.
strs = "Chevrolet,Dacia"
yeni_liste = strs.split(",")
# print(yeni_liste)

# 10- years dizisinin en büyük ve en küçük elemanı nedir ?
# print(min(years))
# print(max(years))
# 11- years dizisinde kaç tane 1998 değeri vardır ?
# result = years.count(1998)
# print(result)
# 12- years dizisinin tüm elemanlarını siliniz.
# years.clear()
# print(years)

# 13- Kullanıcıdan alacağınız 3 tane marka bilgisini bir listede saklayınız.
marka1 = input("Bir araba markası giriniz: ")
marka2 = input("Bir araba markası giriniz: ")
marka3 = input("Bir araba markası giriniz: ")

markalar = [marka1,marka2,marka3]

print(markalar)

