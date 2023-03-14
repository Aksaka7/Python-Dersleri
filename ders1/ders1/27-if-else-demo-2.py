# 1- Girilen bir sayının 0-100 arasında olup olmadığını kontrol ediniz.

# num = float(input("sayı giriniz: "))

# if num > 0 and num <= 100:
#     print(f"Girlen Sayı: {num} 0 ile 100 Arasındadır")


# # 2- Girilen bir sayının pozitif çift sayı olup olmadığını kontrol ediniz.

# num = float(input("litfen sayi giriniz: "))

# if num > 0 and num % 2 == 0:
#     print(f"Girilen Sayı: {num} pozitif çift sayıdır")
# else:
#     print(f"Girilen sayı Kriterler dısındadır. ")


# 3- Email ve parola bilgileri ile giriş kontrolü yapınız.

# email = 'nisazoe@asker.com'
# password = "1234567"

# gelen_Mail = input("Email giriniz: ")
# gelen_Password = input("Parola giriniz: ")

# if gelen_Mail == email:
#     if gelen_Password == password:
#         print("Giriş Başarılı Sisteminize Hoşgeldiniz.")
#     else:
#         print("Giriş Başarısız. Parola yanlış")
# else:
#     print("Giriş Başarısız. Şifre bilgilerini Kontrol ediniz.")


# 4- Girilen 3 sayıyı büyüklük olarak karşılaştırınız.

# a = int(input("sayi giriniz: "))
# b = int(input("sayi giriniz: "))
# c = int(input("sayi giriniz: "))

# if a > b and a > c:
#     print(f"{a} Büyüktür {b} ve {c}'den")
# elif b > a and b > c:
#     print(f"{b} Büyüktür {a} ve {c}'den")
# elif c > a and c > b:
#     print(f"{c} Büyüktür {a} ve {b}'den")
# else:
#     print(f"{a} = {b} = {c} => Eşit sayıdırlar")

    # 5- Kullanıcıdan 2 vize (%60) ve final (%40) notunu alıp ortalama hesaplayınız.
    #    Eğer ortalama 50 ve üstündeyse geçti değilse kaldı yazdırın.
    #    a-) Ortamalama 50 olsa bile final notu en az 50 olmalıdır.
    #    b-) Finalden 70 alındığında ortalamanın önemi olmasın.

    # vize_1 = float(input("Vize 1: "))
    # vize_2 = float(input("Vize 2: "))
    # finally_1 = float(input("Finally 1: "))

    # ortalama = ((vize_1 + vize_2)/2)*0.6 + (finally_1*0.4)

    # if ortalama >= 50:
    #     print(f"Ögrencinin ortalama: {ortalama} ve geçme durumu Başarılı")
    # elif finally_1 >= 70:
    #     print(
    #         f"Ögrencinin ortalama: {ortalama} ve geçme durumu Başarılı. Final Notu :{finally_1} oldugu için sınıfı Geçtiniz.")
    # else:
    #     print(
    #         f"Ögrencinin ortalama: {ortalama} ve Final Notu :{finally_1} oldugu için sınıfta kaldınız.")

    # 6- Kişinin ad, kilo ve boy bilgilerini alıp kilo indekslerini hesaplayınız.
    #    Formül: (Kilo / boy uzunluğunun karesi)
    #    Aşağıdaki tabloya göre kişi hangi gruba girmektedir.
    #    0-18.4    => Zayıf
    #    18.5-24.9 => Normal
    #    25.0-29.9 => Fazla Kilolu
    #    30.0-34.9 => Şişman (Obez)

    # adi = input("Adınızı giriniz: ")
    # kilo = float(input("Kilo değeri giriniz: "))
    # boy = float(input("Boy değeri giriniz: "))

    # index = kilo / (boy**2)
    # if index >= 0 and index <= 18.4:
    #     print(f"Merhaba {adi} kilo index degeriniz : {index} Kilonun degerlendirmenin altında kaldı Lütfen ilgili degerlerin üzerine çıkınız.")
    # elif index >= 18.5 and index <= 24.9:
    #     print(f"Merhaba {adi} kilo index degerin: {index} Kilo degerlerin Gayet Normal Boyle devam et.")
    # elif index >= 25.0 and index <=29.9:
    #     print(f"Merhaba {adi} kilo index degerin: {index} Kilolu oldugun bir gerçek ve bu gerçekle yüzleşmelisin.")
    # elif index >= 30.0 and index <= 34.9:
    #     print(f"Merhaba {adi} kilo index degerin: {index} Kilolu degilsin Obezsiz A.Q Derhal kilo için kendini Hazırla.")
    # else:
    #     print(f"MErhaba {adi} Kilo degerlerini ölçen alet patladı Artık Salona başlamak için bir nedenin var dünyanın buna ihtiyacı var.")
