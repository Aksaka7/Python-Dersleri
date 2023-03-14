sayilar = [1, 3, 5, 7, 9, 12, 19, 21]

# 1- Sayilar listesindeki hangi sayılar 3'ün katıdır ?
# for i in sayilar:
#     if i % 3 == 0:
#         print(i)

# 2- Sayilar listesinde sayıların toplamı kaçtır ?
sonuc = 0
# for i in sayilar:
#     toplam += i
#     print(toplam)

# 3- Sayilar listesindeki tek sayıların karesini alınız.
# for i in sayilar:
#     if i % 2 != 0:
#         print(f"{i} = {sonuc} = {i ** 2}")
#         sonuc = i ** 2


sehirler = ['kocaeli', 'istanbul', 'ankara',
            'izmir', 'rize', 'Antakya', 'Hatay']
# 4- Şehirlerden hangileri en fazla 5 karakterlidir ?

# for i in sehirler:
#     if len(i) == 5:
#         print(i)

urunler = [
    {'name': 'samsung S6', 'price': '3000'},
    {'name': 'samsung S7', 'price': '4000'},
    {'name': 'samsung S8', 'price': '5000'},
    {'name': 'samsung S9', 'price': '6000'},
    {'name': 'samsung S10', 'price': '7000'}
]

# 5- Ürünlerin fiyatları toplamı nedir ?
# toplam = 0
# for i in urunler:
#     fiyat = int(i['price'])
#     toplam += fiyat
#     print(toplam)

# 6- Ürünlerden fiyatı en fazla 5000 olan ürünün ismini gösteriniz ?

for i in urunler:
    fiyat = int(i["price"])
    if fiyat <= 5000:
        print(i['name'])
