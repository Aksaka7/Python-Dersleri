# 1-  "Bmw, Mercedes, Opel, Mazda" elemanlarına sahip bir liste oluşturunuz.
arabalar = ["bmw","mercedes","opel","mazda"]
# 2-  Liste Kaç elemanlıdır ?
result = len(arabalar)
# 3-  Listenin ilk ve son elemanı nedir ?
ilkEleman = arabalar[0]
sonEleman = arabalar[-1]
# print(ilkEleman)
# print(sonEleman)
# 4-  Mazda değerini Toyota ile değiştirin.
arabalar[-1]= 'Toyota'
# print(arabalar)
# 5-  Mercedes listenin bir elemanı mıdır ?
# result = arabalar.count("mercedes")
result = "mercedes" in arabalar
# 6-  Listenin -2 indeksindeki değer nedir ?
result = arabalar[-2]
# 7-  Listenin ilk 3 elemanını alın.
result = arabalar[:3]
# 8-  Listenin son 2 elemanı yerine "Totoya" ve "Renault" değerlerini ekleyin.
# print(arabalar)
arabalar[-2:] = ["Toyota","Renault"]
# print(arabalar)
# 9-  Listenin üzerine "Audi" ve "Nissan" değerlerini ekleyin.
result = arabalar + ["Audi","Nissan"]
# arabalar.append("Audi")
# arabalar.append("Nissan")
# 10- Listenin son elemanını silin.
del arabalar[-1]
# 11- Liste elemanlarını tersten yazdırınız.
result = arabalar[::-1]
# print(result)
# 12- Aşağıdaki verileri bir liste içinde saklayınız. 

      # studentA: Eren Sunar 1999, (70,60,70)
      # studentB: Batu Bozkurt  1997, (80,80,70)
      # studentC: Ayşe Burhan 2000, (80,70,90) 
studentA = ["Eren","Sunar",1999,(70,60,70)]
students = [studentA]


# 13- Liste elemanlarını ekrana yazdırınız.
ogrenci_adi = students[0][0]
ogrenci_soyadi = students[0][1]
ogrenci_yas = 2023-students[0][2]
ogrenci_notlar = students[0][3]
result = f"Öğrencinin adı {ogrenci_adi} soyadi {ogrenci_soyadi} ve yaşı {ogrenci_yas}. Notları ise -> {ogrenci_notlar}"
print(result)