message = "Mehmet Beşir ile dersimiz devam ediyor. Bu ders 2. Ders çok güzel gidiyor\nKemal eren Sunar\nMehmet Beşir"
# Kelimeleri boşluklardan parçalar
# kelimelerListesi = message.split()
# print(type(kelimelerListesi))

splityap = message.split()


#
# #İçine aldığı parametreye göre böler
# cumlelerListesi = message.split("\n")
# print(cumlelerListesi)
# print(len(cumlelerListesi))

# Tüm harfleri büyültür
# result = message.upper()

# Tüm harfleri küçültmek içn
# result = message.lower()

# Sadece ilk harfler büyür
# result = message.title()

# Sadece stringin ilk harfini büyültür
# result = message.capitalize()
# result =message[0].upper() + message[1:].lower()

# Baştaki ve sondaki boşlukları siler
# message = "      Eren Sunar         "
# result = message.strip()


# result = "*".join(message)

# String ifade içerisinde arama yapar varsa başlangıç değerini dönderir yoksa -1 dönderir

# result = message.find("Eren")

# website = "www.youtube.com"
# Başlangıç değeri uyuşuyor mu
# result = website.startswith("https")

# result = website.endswith(".com")

# result = website.replace("YOUTUBE", "erensunar")


# message = "EREN ÇİÇEKÇİLİK"
# Bu aşamada il kodda küçük ç ile küçük c değişir
# message = message.replace("ç","c")

# Replace methodu varsa 2. parametre ile değiştirir. yoksa hiçbir işlem yapmaz
# message = message.replace("Ç","C")
# message = message.replace("İ", "I")

# message = message.center(50,"-")
