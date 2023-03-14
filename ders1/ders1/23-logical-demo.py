
# 1- Girilen bir sayının 0-100 arasında olup olmadığını kontrol ediniz.
# number = int(input("Sayi gir: "))

# if number < 100 and number >= 0:
#     print(str(number) + " : Bu sayi 0-100 arasındadır. ")
# if number < 0:
#     print("Bu sayi 0 dan küçüktür.")
# if number > 100:
#     print("Bu sayi 100 den büyüktür. ")

# 2- Girilen bir sayının pozitif çift sayı olup olmadığını kontrol ediniz.
# number = int(input("Sayi gir: "))

# if number >= 0 and number % 2 == 0:
#     print("Bu sayi Pozitif ve Çiftir " + str(number))
# else:
#     print("Bu sayi arama kriterlerine uymuyor.")


# 3- Email ve parola bilgileri ile giriş kontrolü yapınız.

# mail = "besir@mehmet.com"
# parola = "abc123"

# check_Mail = input("Mail Adresinizi giriniz: ")
# check_Parola = input("Parolanızı giriniz Lütfen: ")

# if mail == check_Mail and parola == check_Parola:
#     print("Sisteme Şuanda Giriş yaptınız")
# else:
#     print("Bilgileriniz Yanlış tekrar deneyiniz.")


# # 4- Girilen 3 sayıyı büyüklük olarak karşılaştırınız.
# # birinci_sayi = int(input("Bir sayı giriniz: "))
# # ikinci_sayi = int(input("Bir sayı giriniz: "))
# # ucuncu_sayi = int(input("Bir sayı giriniz: "))

# # if birinci_sayi > ikinci_sayi and birinci_sayi > ucuncu_sayi:
# #     print(f"Girilen birinci sayi Buyuktur: {birinci_sayi}")

# # if ikinci_sayi > birinci_sayi and ikinci_sayi > ucuncu_sayi:
# #     print(f"Girilen İkinci sayi buyuktur: {ikinci_sayi}")

# # else:
# #     print(f"girilen üçüncü sayi büyüktür: {ucuncu_sayi}")

# 5- Kullanıcıdan 2 vize (%60) ve final (%40) notunu alıp ortalama hesaplayınız.

# # vize = float(input("Vize notunu giriniz: "))
# # final = float(input("Final notunu giriniz: "))

# # result = (vize*0.6)+(final*0.4)

# # print(result)


# 6- Kişinin ad, kilo ve boy bilgilerini alıp kilo indekslerini hesaplayınız.

# name = input("Lütfen Adınızı giriniz: ")
# boy = float(input("Lütfen boyunuzu giriniz: "))
# kilo = float(input("Lütfen Kilonunu giriniz: "))

# vucut_Kitle_Endeksi = kilo / (boy*boy)

# if vucut_Kitle_Endeksi <= 18.5:
#     print("İdeal Kilonun altındasınız...")
# if vucut_Kitle_Endeksi > 18.5 and vucut_Kitle_Endeksi < 24.9:
#     print("İdeal Kilodasın...")
# if vucut_Kitle_Endeksi > 24.9 and vucut_Kitle_Endeksi <29.9:
#     print("ideal Kilonun üstündesin")
# if vucut_Kitle_Endeksi > 29.9 and vucut_Kitle_Endeksi < 39.9:
#     print("İdeal Kilonun üstündesin a.q (OBEZSİN a.q çocugu az ye)")
# if vucut_Kitle_Endeksi > 40:
#     print("Az yeeee Spor yap")


# num = int(input("Sayı giriniz: "))

# if num > 0 and num < 100:
#     print(str(num) + " : Bu sayı 0-100 arasındadır. ")
# else:
#     print("Bu sayı 0 ile 100 arasında degildir...")


# num = int(input("Sayı giriniz: "))

# if num % 2 == 0 and num > 0:
#     print(f"Bu sayı: {num} pozitif çift sayıdır.")
# else:
#     print(f"Bu sayı: {num} arama kriterlerine uymuyor.")

