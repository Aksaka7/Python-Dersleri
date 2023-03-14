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

# #Formated string x numaralı öğrencinin ismi budur soyadı şudur, yaş, teletgon
# print(ogrenciler)

ogrenciler = {}

student_Numbers = int(input("Lütfen Öğrenci numarasını giriniz: "))
student_Name = input("Lütfen Adınızı giriniz: ")
student_Surname = input("Lütfen Soyadınızı giriniz: ")
phone_Numbers = input("Lütfen Telefon numarasını giriniz: ")

ogrenciler.update({
    student_Numbers: {
        'name': student_Name,
        'surname': student_Surname,
        'phone': phone_Numbers,
    },
})

print("-------------------------------------------\n")

student_Numbers = int(input("Lütfen Öğrenci numarasını giriniz: "))
student_Name = input("Lütfen Adınızı giriniz: ")
student_Surname = input("Lütfen Soyadınızı giriniz: ")
phone_Numbers = input("Lütfen Telefon numarasını giriniz: ")

ogrenciler.update({
    student_Numbers: {
        'name': student_Name,
        'surname': student_Surname,
        'phone': phone_Numbers,
    },
})

print("-------------------------------------------\n")


student_Numbers = int(input("Lütfen Öğrenci numarasını giriniz: "))
student_Name = input("Lütfen Adınızı giriniz: ")
student_Surname = input("Lütfen Soyadınızı giriniz: ")
phone_Numbers = input("Lütfen Telefon numarasını giriniz: ")

ogrenciler.update({
    student_Numbers: {
        'name': student_Name,
        'surname': student_Surname,
        'phone': phone_Numbers,
    },
})

print("-------------------------------------------\n")


ogrenci_number = int(input("İstenilen ögrencinin Numarası giriniz: "))

aranan_ogrenci = ogrenciler[ogrenci_number]

print(
    f"Aradıgınız {ogrenci_number} nolu ögrencinin Adı Soyadı: {aranan_ogrenci['name']} {aranan_ogrenci['surname']} telefon numarsı: {aranan_ogrenci['phone']}")
