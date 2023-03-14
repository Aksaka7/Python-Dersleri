sayi_listesi = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# print("For döngüsüne giriliyor")

# for i in sayi_listesi:
#     print(i*3*2)
# num = []
# for i in sayi_listesi:
#     num = i + 2
#     num = num * 2
#     print(f"{i}  => {num}")
# for i in sayi_listesi:
#     print(i)
# for sayi in sayi_listesi:
#     print(sayi)
# print(i)
# print("for döngüsü bitti")

isimler = ["Mehmet", "Nisa", "Hüseyin", "Ahmet", "Layane"]
# for name in isimler:
#     name = name.upper()
#     print(f"Benim ismim {name}")


mesaj = "Merhabalar hoş geldiniz!"

# for harf in mesaj:
#     print(harf)

sayi_demetleri = [(1, 3), (2, 4), (1, 0), (5, 5)]
for sayi1, sayi2 in sayi_demetleri:
    print(sayi1, sayi2)
    print("----------------------")

# plakalar = {"istanbul": 34, "konya": 42, "izmir": 35}
# # print(plakalar.values())

# for anahtar, deger in plakalar.items():
#     print(f"Anahtar {anahtar} ve değer {deger}")


sayi1 = [1, 2, 3, 4, 5]
sayi2 = ["a", "b", "c", "d", "e"]
list3 = [100, 200, 300, 400, 500]

icinde = list(zip(sayi1, sayi2, list3))

print(icinde)
