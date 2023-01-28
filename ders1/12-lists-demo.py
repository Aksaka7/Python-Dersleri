# 1-  "Bmw, Mercedes, Opel, Mazda" elemanlarına sahip bir liste oluşturunuz.

cars = ["Bmw", "Mercedes", "Opel", "Mazda"]

# 2-  Liste Kaç elemanlıdır ?
# print(len(cars)) #4Eleman


# 3-  Listenin ilk ve son elemanı nedir ?

# print(cars[0])
# print(cars[-1])


# 4-  Mazda değerini Toyota ile değiştirin.
# arabalar[-1]= 'Toyota'

cars[-1] = "Toyota"
# print(dir(cars))

# 5-  Mercedes listenin bir elemanı mıdır ?

result = cars.count("Mercedes")
# result = "Mercedes" in cars

# 6-  Listenin -2 indeksindeki değer nedir ?
# print(cars[-2])

# 7-  Listenin ilk 3 elemanını alın.

ilk_Uc = cars[0:3]


# 8-  Listenin son 2 elemanı yerine "Toyota" ve "Renault" değerlerini ekleyin.
cars[-1] = "Toyota"
cars[-2] = "Renault"

# result = [-2:]

# 9-  Listenin üzerine "Audi" ve "Nissan" değerlerini ekleyin.
result = cars + ["Audi", "Nissan"]

cars.append("Audi")
cars.append("Nissan")

# print(cars)
# # 10- Listenin son elemanını silin.

# cars.remove("Audi")
# print(cars)


# 11 - Liste elemanlarını tersten yazdırınız.

# sonuc = cars[::-1]
# print(sonuc)

# 12- Aşağıdaki verileri bir liste içinde saklayınız.

# studentA: Eren Sunar 1999, (70,60,70)
# studentB: Batu Bozkurt  1997, (80,80,70)
# studentC: Ayşe Burhan 2000, (80,70,90)

student_A = ["Eren", "Sunar", 1999, (70, 60, 70)]
student_B = ["Batu", "Bozkurt", 1997, (80, 80, 70)]
student_C = ["Layane", "Asker", 2000, (50, 60, 90)]

students = [student_A, student_B, student_C]

# 13- Liste elemanlarını ekrana yazdırınız.
print(students)
