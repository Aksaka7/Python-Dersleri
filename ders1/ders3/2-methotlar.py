# Classlara Fonction(Metod) Ekleme

# class C_sinifi:

#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#         self.kalemleri = []

#     def hangi_Kalem(self, bu_Kalem):
#         self.kalemleri.append(bu_Kalem)

#     def yasini_hesapla(self):
#         return 2023 - self.age


# zoeNisa = C_sinifi(name='Zoe Nisa', age=2020)
# zoeNisa.hangi_Kalem("Kırmızı")
# zoeNisa.hangi_Kalem("Yeşil")
# zoeNisa.hangi_Kalem("Sarı")
# zoeNisa.hangi_Kalem("Mavi")

# print(
#     f"Müşterimiz {zoeNisa.name} {zoeNisa.yasini_hesapla()} yaşında ve Kullandıgı Kalem rengi {zoeNisa.kalemleri}")


# class K14_Sinifi():
#     def __init__(self, canta_varmi):
#         self.canta_varmi = canta_varmi
#         self.ayakkabi = []
#         self.uniforma = []

#     def ayakkabi_Yaz(self, ayakkabi_Rengi):
#         return self.ayakkabi.append(ayakkabi_Rengi)

#     def yazlik_Kislik_Uniform(self, uniform):
#         self.uniforma.append(uniform)


# zoeNisa = K14_Sinifi('Evet')
# zoeNisa.ayakkabi_Yaz('Siyah')
# zoeNisa.ayakkabi_Yaz('Beyaz')
# zoeNisa.ayakkabi_Yaz('Penbe')

# zoeNisa.yazlik_Kislik_Uniform('Yazlik VAR')
# zoeNisa.yazlik_Kislik_Uniform('Kışlık VAR')

# print(f"{zoeNisa.ayakkabi}")
# print(f"{zoeNisa.uniforma}")


# class Personel:
#     def __init__(self):
#         self.personel_Name = []
#         self.bilgisayarlar = []
#         self.personel_ID = []

#     def isimleri_Al(self, isim):
#         self.personel_Name.append(isim)

#     def computers(self, computer):
#         self.bilgisayarlar.append(computer)

#     def kimlikleri_Yaz(self, kimlik):
#         self.personel_ID.append(kimlik)


# user = Personel()

# user.isimleri_Al("Melike")
# user.isimleri_Al("Burak")
# user.isimleri_Al("Alev")
# user.isimleri_Al("Efe")
# user.isimleri_Al("Dorukhan")
# user.isimleri_Al("Hüseyin")
# user.isimleri_Al("Derya")
# user.isimleri_Al("Melih")
# user.isimleri_Al("Ecem")

# print(user.personel_Name)
# print("<------------------------------->")
# user.kimlikleri_Yaz("23156165")
# user.kimlikleri_Yaz("165155613")
# user.kimlikleri_Yaz("448998498")
# user.kimlikleri_Yaz("897749865")
# user.kimlikleri_Yaz("6511566558")
# user.kimlikleri_Yaz("9849894861")
# user.kimlikleri_Yaz("8944419854")
# user.kimlikleri_Yaz("132651651")

# print(user.personel_ID)
# print("<------------------------------->")

# user.computers("İntel")
# user.computers("Levona")
# user.computers("Toshiba")

# print(user.bilgisayarlar)
# print("<------------------------------->")
