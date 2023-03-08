website = "http://www.MehmetASKER.com"
course = "Python Kursu Baştan Sona Python Programlama "
#course = "PythonKursuBaştanSonaPythonProgramlama"
mesaj = " Hello World "

# 1-  ' Hello World ' karakter dizisinin baş ve sondaki boşluk karakterlerini silin.

result = mesaj.strip()


# 2- 'www.MehmetASKER.com' içindeki mehmetasker bilgisi haricindeki her karakteri silin.
metin = "www.Mehmet.com"
result = metin.strip("w.com")


# 3-  'course' karakter dizisinin tüm karakterlerini küçük harf yapın.
result = course.lower()


# 4- 'website' içinde kaç tane a karakteri vardır ? (count('a'))
result = website.count("A")


# 5- 'website' "www" ile başlayıp com ile bitiyor mu?
result = website.startswith("http://www")
result = website.endswith(".com")


# 6-  'website' içinde '.com' ifadesi var mı?
# varsa İndex baslangıcını veriyor
result = website.find(".com")


# "com" nerede başlıyorsa orayı Yaz
result = course.rindex('Programlama')  # exception


# 7- 'course' içindeki karakterlerin hepsi alfabetik mi? (isalpha, isdigit)
result = course.isalpha()
result = course.isdigit()

# 8- 'Contents' ifadesini satırda 50 karakter içine yerleştirip sağ ve soluna * ekleyiniz.
result = "Contents".center(50, "*")

# 9-  'course' karakter dizisindeki tüm boşluk karakterlerini '-' ile değiştirin.
result = course.replace("-", " ")


# 10- 'Hello World' karakter dizisinin 'World' ifadesini 'There' olarak değiştiri
result = "Hello World".replace("World", "There")


# 11-  'course' karakter dizisini boşluk karakterlerinden ayırın.
result = course.split(" ")
print(result)