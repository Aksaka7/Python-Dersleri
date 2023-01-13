website = "http://www.erensunar.com"
course = "Python Kursu: Baştan Sona Python Programlama Rehberiniz (40 saat)"

# 1- 'course' karakter dizisinde kaç karakter bulunmaktadır ?
# Lenght
# result = len(website)
yazdir = len(website + course)

# 2- 'website' içinden www karakterlerini alın.
# result = website[7:10]

result = website[7:10]


# 3- 'website' içinden com karakterlerini alın.
# result = website[-3:]

result = website[-3:]


# 4- 'course' içinden ilk 15 ve son 15 karakterlerini alın.
# ilk15 = course[:15]
# son15 = course[-15:]
# print(ilk15)
# print(son15)

first15 = course[:15]
last15 = course[-15:]

# print("Bu İlk 15 Karakterdir : " + first15)
# print("Bu Son 15 karakterdir : " + last15)

# 5- 'course' ifadesindeki karakterleri tersten yazdırın.
# result = course[::-1]

wrongprint = course[::-1]

name, surname, age, job = "Zoe Nisa", "Asker", 3,  "Bebeğim"
# x,y = 30, 31
# 6- Yukarıda verilen değişkenler ile ekrana aşağıdaki ifadeyi yazdırın.
#    'Benim adım Bora Yılmaz, Yaşım 32 ve mesleğim mühendis.'
# result = "Benim adım " + name + " " + surname + ", Yaşım " + str(age) + " ve mesleğim " + job
# result = f"Benim adım {name} {surname}, Yaşım {age} ve mesleğim {job}" #Formatted stringlerde tür dönüşümüne gerek yoktur.

ffonction = f"Benim adım {name} {surname}, Yaşım {age} ve meslegim {job}"


# 7- 'Hello world' ifadesindeki w harfini 'W' ile değiştirin.
string = 'Hello world'
# result = string[:6] + "W" + string[-4:]

result = string[:6] + "M" + string[-4:]

# 8- 'abc' ifadesini yan yana 4 defa yazdırın.
# result = "abc" * 3

result = "abc " * 4

print(" " + result)
