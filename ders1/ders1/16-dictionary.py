# key - value [],(),str,int,flaot,dict

# 41-> kocalei, 34 -> istanbul

# sehirler = ["kocaeli","istanbul","izmir"]
plakalar = [41, 34, 35]

# aranan_index = sehirler.index("kocaeli")

# print(aranan_index)

# print(plakalar[aranan_index])
# print(plakalar["kocaeli"]) #-> 41


# plakalar = {'kocaeli':41,
#             'istanbul':34,
#             "konya":42 ,
#             "izmir":35}

# # print(plakalar['istanbul'])
# plakalar["ankara"] = 6
# plakalar["kocaeli"] = 83
# # print(plakalar)
# print(plakalar["kocaeli"])

users = {
    'mehmetAsker': {
        'name': "Mehmet",
        "age": 35,
        "city": "Hatay",
        "country": "Turkiye",
        "email": "asker@Aksakal.com",
        "password": "823554523223354",
        "phone": "+35699619587",
        "rollers": ["admin"]
    },
    'layaneAsker': {
        'name': "Layane",
        "age": 35,
        "city": "Hatay",
        "country": "Turkiye",
        "email": "asker@Aksakal.com",
        "password": "823554523223354",
        "phone": "+35699619587",
        "rollers": ["admin"]
    }




}

yetki_Ver = users['layaneAsker']["rollers"]
print(yetki_Ver)
yetki_Ver.append("SuperAdmin")

users["layaneAsker"]["rollers"] = yetki_Ver
print(users["layaneAsker"]["rollers"])

# erenin_rolleri = users["erensunar"]["roller"]
# # print(erenin_rolleri)
# # print(type(erenin_rolleri))
# erenin_rolleri.append("admin")
# # print(erenin_rolleri
# users["erensunar"]["roller"] = erenin_rolleri
# print(users["erensunar"]["roller"])
