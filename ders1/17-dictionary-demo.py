'''
    ogrenciler = {
        '120': {
            'ad': 'Ali',
            'soyad': 'Yılmaz',
            'telefon': '532 000 00 01'
        },
        '125': {
            'ad': 'Can',
            'soyad': 'Korkmaz',
            'telefon': '532 000 00 02'
        },
        '128': {
            'ad': 'Volkan',
            'soyad': 'Yükselen',
            'telefon': '532 000 00 03'
        },
    }

    1- Bilgileri verilen öğrencileri kullanıcıdan aldığınız bilgilerle
       dictionary içinde saklayınız.

    2- Öğrenci numarasını kullanıcıdan alıp ilgili öğrenci bilgisini gösterin.
'''


ogrenciler = {}

number = input("Öğrenci no: ")
name = input("Öğrenci adı: ")
surname = input("Öğrenci saoyad: ")
phone = int(input("Öğrenci telefon: "))

ogrenciler.update({
    number:{
        "ad":name,
        "soyad":surname,
        "telefon":phone,
        "dogumYılı":2001


    }
})
# sorgulanacak_no = input()
# #Formated string x numaralı öğrencinin ismi budur soyadı şudur, yaş, teletgon 
# print(ogrenciler)