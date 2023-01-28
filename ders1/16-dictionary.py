#key - value [],(),str,int,flaot,dict

#41-> kocalei, 34 -> istanbul

# sehirler = ["kocaeli","istanbul","izmir"]
plakalar = [41,34,35]

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
    "mehmetbesir": {
        "yas":35,
        "isim":"Mehmet Beşir",
        "email":"mehmetbesir@gmail.com",
        "roller":["admin","user"],
        "telNo":"5392851942"
        
    },
    "erensunar": {
        "yas":22,
        "isim":"Eren Sunar",
        "email":"erensunar@gmail.com",
        "roller":["user"],
        "telNo":"5538583912"
    }






}
erenin_rolleri = users["erensunar"]["roller"]
# print(erenin_rolleri)
# print(type(erenin_rolleri))
erenin_rolleri.append("admin")
# print(erenin_rolleri
users["erensunar"]["roller"] = erenin_rolleri
print(users["erensunar"]["roller"])





