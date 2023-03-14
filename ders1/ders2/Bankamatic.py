# Bankamatik Uygulaması

MehmetHesap = {
    'name': 'Mehmet Asker',
    'accountNo': '456456123',
    'balance': 5000,
    'ekHesap': 2852
}


LayaneHesap = {
    'name': 'Layane Asker',
    'accountNo': '8544611564',
    'balance': 8000,
    'ekHesap': 2000
}


def paraCek(hesap, miktar):
    print(f"Merhaba {hesap['name']}")

    if (hesap['balance'] >= miktar):
        hesap['balance'] -= miktar
        print("Paranızı çekiniz")
    else:
        toplam = hesap['balance'] + hesap['ekHesap']

        if (toplam >= miktar):
            ek_Hesabi_Kullanalim_mi = input("Ek hesap kullan (e/h): ")

            if ek_Hesabi_Kullanalim_mi == 'e':
                ek_Hesab_Kullanilacak_Miktar = miktar - hesap['balance']
                hesap['ekHesap'] -= ek_Hesab_Kullanilacak_Miktar
                print("Ek hesap kullanılarak paranız ödenmiştir.")
            else:
                print(
                    f"{hesap['accountNo']} nolu hesabınızda {hesap['balance']} para bulunmaktadır")
        else:
            print("Üzgünüz Yetersiz Bakiye")


def bakiyeSorgula(hesap):
    print(f"{hesap['accountNo']} nolu hesabınızda {hesap['balance']} TL bulunmaktadır. Ek hesap bakiyeniz: {hesap['ekHesap']}")


paraCek(LayaneHesap, 8000)
paraCek(LayaneHesap, 2000)

print("<--------------------------------->")
paraCek(LayaneHesap, 2000)
bakiyeSorgula(LayaneHesap)
