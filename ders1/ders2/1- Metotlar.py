# # Methodlar

# list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# list.append(10)
# print(list)
# list.pop()
# print(list)
# print(type(list))


# myString = 'Hello, world'

# print(myString.upper())


# # Fonksiyon

# def sayHello():
#     print("Merhaba Dunya")

# sayHello()

# def total(num1, num2):
#     return num1 + num2


# result = total(12, 15)
# sonuc = total(22, 1)

# print(result,sonuc)


def yasHesapla(dogumyili):
    return 2023 - dogumyili


yasMehmet = yasHesapla(1988)
yasLayane = yasHesapla(1992)
yasZoeNisa = yasHesapla(2020)

print(yasMehmet, yasLayane, yasZoeNisa)


def EmekliligeKacYilKaldi(dogumyili, isim):
    yas = yasHesapla(dogumyili)
    emekli = 65 - yas
    if emekli > 0:
        print(
            f'Merhaba {isim} Emekliliginize yaklasik olarak {emekli} yil kaldi')
    else:
        print("Zaten Emekli oldunuz.")


EmekliligeKacYilKaldi(1988, 'Mehmet')
EmekliligeKacYilKaldi(1963, 'Mehmet')
