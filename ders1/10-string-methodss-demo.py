website = "http://www.MehmetASKER.com"
course = "Python Kursu: Baştan Sona Python Programlama "
mesaj = " Hello World "

# 1-  ' Hello World ' karakter dizisinin baş ve sondaki boşluk karakterlerini silin.

bosluklariSil = mesaj.strip()


# 2- 'www.erensunar.com' içindeki erensunar bilgisi haricindeki her karakteri silin.
metin = "www.erensunar.com"
result = website.strip("htp:/w.com")
print(result)
firstside = metin[4:][:-4]


# 3-  'course' karakter dizisinin tüm karakterlerini küçük harf yapın.

small = course.lower()


# 4- 'website' içinde kaç tane a karakteri vardır ? (count('a'))
how_MuchA = website.count("a")

# 5- 'website' "www" ile başlayıp com ile bitiyor mu?


# 6-  'website' içinde '.com' ifadesi var mı? 
#varsa İndex baslangıcını veriyor
result = website.find("com")


# "com" nerede başlıyorsa orayı Yaz
# result = website.rindex('com') # exception
change = website.rindex("com")


# 7- 'course' içindeki karakterlerin hepsi alfabetik mi? (isalpha, isdigit)
result = course.isalpha()



# 8- 'Contents' ifadesini satırda 50 karakter içine yerleştirip sağ ve soluna * ekleyiniz.
content = "Contents"

result = content.center(50, "*")


# 9-  'course' karakter dizisindeki tüm boşluk karakterlerini '-' ile değiştirin.
result = course.replace(" ","-")


# 10- 'Hello World' karakter dizisinin 'World' ifadesini 'There' olarak değiştiri
result =  mesaj.replace("World", "There")
# 11-  'course' karakter dizisini boşluk karakterlerinden ayırın.

result = course.split()


