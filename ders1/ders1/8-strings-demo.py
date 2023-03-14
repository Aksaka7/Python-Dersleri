website = "https://www.mehmetasker.com/"
course = "Başlangıç seviyesi Python Kursu: Baştan sona Programlama Rehberi (40 Saat)'lik Egitim."

# 1- 'Course' karkteri dizisinde kaç karakter bulunmaktadır.
karakterin_Uzunlugu = len(course) #86

# 2- 'website' içinden www Karakterlerinini Al ve ekrane yaz
karakteri_Al = website[8:11] #www Aldık

# 3- 'website' içinden com Karakterlerinini Al ve ekrane yaz
karakteri_Al = website[-4:-1]

# 4- 'course' içinden ilk ve son 15 karakteri yazdır. 
karakteri_Al = course[:15]
karakteri_Al = course[-15:]

# 5- 'course' ifadesindeki karakterleri tersten yazdırın
karakteri_Al = course[::-1]

name,surname,age,jop = 'Bora','Yılmaz',32,'Mühendis'
# 6- Yukarıdaki verilen degişkenler ile ekrana aşağıdaki ifadeyi yazdırın. 
# 'BEnim adım Bora Yılmaz, Yaşım 32 ve meslegim mühendis.'
#print(f"Benim adım {name} {surname}, Yaşım {age} ve Meslegim {jop}.")

# 7 - 'Hello world' içindeki w harfini W ile degiştir. 
hello = "Hello world"
karakteri_Al= hello[0:6] + "W" + hello[-4:]


#8 - 'abc' ifadesini yan yana 3 defa yazınız.

karakteri_Al = "abc " * 3

print(karakteri_Al)
