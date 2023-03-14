# x = float(input("Bir sayı giriniz: "))
# y = float(input("Bir sayı giriniz: "))

# if x > y:
#     print("x y'den büyüktür.")
# elif x == y:
#     print(" x y'ye eşittir.")
# else:
#     print("x y'den küçüktür")


# num = int(input("Sayi giriniz: "))

# if num > 0:
#     print(num, " bu sayı sıfırdan büyüktür.")
#     if num % 2 == 0:
#         print("Bu sayi Çifttir.")
#     else:
#         print("Bu sayi Tektir.")
# elif num < 0:
#     print(num, " bu sayı sıfırdan küçüktür.")
#     if num % 2 == 0:
#         print("Bu sayi Çifttir.")
#     else:
#         print("Bu sayi Tektir.")
# else:
#     print(num, " bu sayı sıfıra Eşittir.")


num = int(input("Sayi giriniz: "))

if num > 0:
    print(str(num) + " bu sayı Pozitif")
elif num < 0:
    print(str(num) + " bu sayı Negatif")
else:
    print("Bu sayı Nötür bir sayı")
