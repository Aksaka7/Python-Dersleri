"""
    1- Bir müşterinin aşağıdaki bilgileri için değişken oluşturunuz.

    Müşteri adı
    Müşteri soyadı
    Müşteri ad + soyad
    Müşteri cinsiyet
    Müşteri tc kimlik
    Müşteri doğum yılı
    Müşteri adres bilgisi
    Müşteri yaşı
"""

customer_Name = "Mehmet"
customer_Surname = "Asker"
fullname = customer_Name + " " + customer_Surname
sex = "male"
ıD_Number = 1651651611
birth_Date = 1988
adress = "Kıbrıs"
customer_Age = 2023 - birth_Date


"""
    2- Aşağıdaki siparişlerin toplam bilgisini hesaplayınız.

    Sipariş 1 => 110    TL
    Sipariş 2 => 1100.5 TL
    Sipariş 3 => 356.95 TL

"""
siparis_1 = 152
siparis_2 = 1100.5
siparis_3 = 356.95


indirimOrani = 35


toplam_Tutar = siparis_1 + siparis_2 + siparis_3
print(
    f"Toplam ödenecek Miktar: {toplam_Tutar}, Almiş oldugunuz Yıl sonu indirimi {int(toplam_Tutar / indirimOrani * 100)} TLdir.")
