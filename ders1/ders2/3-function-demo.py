# 1- Gönderilen bir Kelimeyi belirtilen kez ekranda Gösteren Fonksiyon yazın.

# def ekrandaYaz(a, b):
#     for i in range(b):
#         print(f"{i} => {a}")


# ekrandaYaz("Merhaba", 7)

def ekranaYaz(a, b):
    print(a * b)


ekranaYaz("Merhaba ", 5)

# 2- Kendine gönderilen sınırsız sayıdaki Parametreyi bir Listeye ceviren Fonksiyon yazınız.


# def changeList(*parametreler):
#     list = []
#     for parametre in parametreler:
#         list.append(parametre)
#     return list


# result = changeList(10, 23, 5, 6, 8, 56, (36, 352), 'Mehmet')

# print(result)

# 3- Gönderilen 2 sayı arasındaki Tüm asal sayıları bulun.

# def asalSayiBul(num1, num2):
#     for sayi in range(num1, num2+1):
#         if sayi > 1:
#             for i in range(2, sayi):
#                 if sayi % i == 0:
#                     break
#             else:
#                 print(sayi)


# num1 = int(input("Hangi Sayıdan Başlasın: "))
# num2 = int(input("Hangi sayıya kadar geçerli olsun: "))

# asalSayiBul(num1,num2)

# Kendisine gönderilen bir sayının TAm bölenlerini bir liste şeklinde geriye yollayan bir fonksiyon yazınız.

# def tamBolenleriBul(sayi):
#     tamBolenler = []

#     for i in range(2, sayi):
#         if sayi % i == 0:
#             tamBolenler.append(i)
#     return tamBolenler


# result = (tamBolenleriBul(20))

# print(result)
