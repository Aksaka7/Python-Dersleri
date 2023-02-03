
# 1- Girilen 2 sayıdan hangisi büyüktür ?

# number1 = int(input("Sayı gir: "))
# number2 = int(input("Sayı gir: "))

# if number1 > number2:
#     print("bu sayi büyüktür : " + str(number1))
# if number1 < number2:
#     print("Bu sayi daha büyüktür  " + str(number2))



# 2- Kullanıcıdan 2 vize (%60) ve final (%40) notunu alıp ortalama hesaplayınız.
#    Eğer ortalama 50 ve üstündeyse geçti değilse kaldı yazdırın.

# vize = float(input("Vize Notu: "))
# final = float(input("Final Notu: "))

# result = ((vize*0.6)+(final*0.4))
# print(result)
# if result > 50:
#     print("Sınıfı Geçtiniz")
# if result < 50:
#     print("Sınıfta Kaldınız")

# 3- Girilen bir sayının tek mi çift mi olduğunu yazdırın.

# sayi = float(input("Sayı gir: "))

# if sayi % 2 == 0:
#     print("Bu sayi Çifttir : " + str(sayi))
# else:
#     print("Bu sayi Tektir : " + str(sayi))   


# 4- Girilen bir sayının negatif pozitif durumunu yazdırın. 

# sayi = int(input("Sayı gir: "))

# if sayi > 0:
#     print("Bu sayi Pozitif Bir sayıdır")
# if sayi < 0:
#     print("Bu sayi Negatif Bir sayidir.")
# if sayi == 0: 
#     print("Sıfır nötür bir sayıdır")

# 5- Parola ve email bilgisini isteyip doğruluğunu kontrol ediniz.
#    (email: email@erensunar.com parola:abc123)

# mail = "email@erensunar.com"
# parola = "abc123"

# check_Mail = input("Mail Adresinizi giriniz: ")
# check_Parola = input("Parolanızı giriniz Lütfen: ")

# if mail == check_Mail and parola == check_Parola:
#     print("Sisteme Şuanda Giriş yaptınız")
# else:
#     print("Bilgileriniz Yanlış tekrar deneyiniz.")