# # Class

# class Personel():

#     def __init__(self, name, surname, year) -> None:
#         pass
#         self.name = name
#         self.surname = surname
#         self.year = year
#         self.sql = "Evet"
#         print("Kayıtlar Yapıldı.")

# # Object, İnstance


# p1 = Personel("Mehmet", "Asker", 1988)
# p2 = Personel("Layane", "Asker", 1992)
# p3 = Personel("Zoe Nisa", "Asker", 2023)


# print(f"Personel Isim Soyisim {p1.name} {p1.surname} Dogum yılı {p1.year}")
# print(f"Personel Isim Soyisim {p2.name} {p2.surname} Dogum yılı {p2.year}")
# print(f"Personel Isim Soyisim {p3.name} {p3.surname} Dogum yılı {p3.year}")


# Class Özellikleri
class Asinif():
    bildigi_diller = ["İngilizce", "Fransizca", "İtalyanca", "Portekizce"]
    bolum = 'Ateş'
    sql = ''
    deneyim_yili = 0

    def __init__(self) -> None:
        self.bildigi_diller = []
        self.bolum = ''
        self.sql = ''


mehmet = Asinif()
mehmet.bildigi_diller.append('Danca')
mehmet.bildigi_diller.append('Arapca')


layane = Asinif()
layane.sql = 'Evet'
layane.bolum = 'Ateş'
layane.bildigi_diller.append('Portekizce')
mehmet.sql = 'hayır'
mehmet.bolum = 'Su'
print(mehmet.bildigi_diller)
print(layane.bildigi_diller)
print('<----------------->')
print(mehmet.sql)
print(layane.sql)
print('<----------------->')
print(mehmet.bolum)
print(layane.bolum)
print('<----------------->')
