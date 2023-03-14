# name = "Mehmet Asker"

# for harf in name:
#     if harf == "u":
#         break
#     print(harf)

x = 0

# while x < 5:
#     x += 1
#     if x % 2 == 0:
#         continue
#     print(x)

x = 1
result = 0
while x < 100:
    x += 1
    if x % 2 == 0:
        continue
    else:
        result += x
        print(result)


# password = "1234567"
# hak = 3
# hesap_blokeli_mi = False

# while hak > 0:
#     check_password = input("Şifre giriniz: ")
#     if password == check_password:
#         print("Giriş başarılı")
#         break
#     else:
#         hak -= 1
#         print(f"Girdiğiniz şifre yanlış. Hakkınız: {hak}")
#         if hak == 0:
#             hesap_blokeli_mi = True


password = '123456'
giris_Denemesi = 3
hesap_blokeli_mi = False

while giris_Denemesi > 0:
    sifre_Parola = input("Şifrenizi giriniz: ")
    if password == sifre_Parola:
        print("Sisteminize hoşgeldiniz")
        giris_Denemesi = 3
        break
    else:
        giris_Denemesi -= 1
        print(
            f"Girmiş oldugunuz Şifre yanlıştır: Kalan Anahtar giriş sayınız: {giris_Denemesi}")
        if giris_Denemesi == 0:
            hesap_blokeli_mi = True
