username = "Mehmet"
password = "123456"

check_username = input("username giriniz: ")
check_password = input("password giriniz: ")

# if username == check_username and password == check_password:
#     print("Hoş geldiniz.")
# else:
#     print("Hatalı giriş")

# if username == check_username:
#     if password == check_password:
#         print("Giriş başarılı.")
#     else:
#         print("Parola yanlış.")
# else:
#     if password != check_password:
#         print("Username ve parola yanlış.")
#     else:
#         print("Username yanlış.")


if username == check_username:
    if password == check_password:
        print("Hoş geldiniz.")
    else:
        print("Parola yanlış.")
else:
    if password != check_password:
        print("Username veya Password Yanlış.")
    else:
        print("Username Yanlış...")
