# 1-  "Bmw, Mercedes, Opel, Mazda" elemanlarına sahip bir liste oluşturunuz.

arabalar = ["BMW", "Mercedes", "Opel", "Mazda"]


# 2-  Liste Kaç elemanlıdır ?
result = len(arabalar)

# 3-  Listenin ilk ve son elemanı nedir ?
listenin_ilk_Elemani = arabalar[0]
son_Eleman = arabalar[-1]


# 4-  Mazda değerini Toyota ile değiştirin.
arabalar[-1] = "Toyota"

# 5-  Mercedes listenin bir elemanı mıdır ?
result = arabalar.count("Mercedes")


# 6-  Listenin -2 indeksindeki değer nedir ?
result = arabalar[-2]


# 7-  Listenin ilk 3 elemanını alın.
result = arabalar[:3]


# 8-  Listenin son 2 elemanı yerine "Toyota" ve "Renault" değerlerini ekleyin.
arabalar[-1] = "Renault"
arabalar[-2] = "Toyota"


# 9-  Listenin üzerine "Audi" ve "Nissan" değerlerini ekleyin.
arabalar.append("Audi")
arabalar.append("Nissan")

print(arabalar)

# # 10- Listenin son elemanını silin.
arabalar.remove("Audi")
print(arabalar)

# 11 - Liste elemanlarını tersten yazdırınız.
result = arabalar[::-1]
# print(result)
# sonuc = cars[::-1]


# 12- Aşağıdaki verileri bir liste içinde saklayınız.

# studentA: Layane Asker 1992, (70,60,70)
# studentB: Nisa Bozkurt  2023, (80,80,70)
# studentC: Tim Mango 1993, (80,70,90)

studentA = ["Layane Asker", 1992, (70, "Mehmet Asker", 70)]
studentB = ["Nisa Bozkurt", 2023, (80, 80, 70)]
studentC = ["Tim Mango", 1993, (80, 70, 90)]
studentD = ["Millie Mango", 1995, (70, 80, 80)]
studentE = ["Mehmet Asker", 1988, (90, 90, 90)]

student = [studentA, studentB, studentC, studentD, studentE]


# fullname = input("Fullname giriniz: ")
# birth_Day = int(input("Dogum Yılınızı giriniz: "))
# tuble_Degeri1 = int(input("Puan giriniz: "))
# tuble_Degeri2 = int(input("Puan giriniz: "))
# tuble_Degeri3 = int(input("Puan giriniz: "))

# ogrenciler = [fullname, birth_Day,
#               (tuble_Degeri1, tuble_Degeri2, tuble_Degeri3)]
# print(ogrenciler)

# 13- Liste elemanlarını ekrana yazdırınız.

print(f"student: {student}")
