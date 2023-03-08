x, y, z = 2, 5, 10

# 1- Kullanıcıdan aldığınız 2 sayının çarpımı ile x,y,z toplamının farkı nedir ?
# number1 = float(input("Bir sayı giriniz: "))
# number2 = float(input("İkinci sayı giriniz: "))
# result = (number1 * number2) - (x+y+z)
# print(result)


# num1 = float(input("Bir sayı : "))
# num2 = float(input("Bir sayı : "))

# result = (num1*num2) - (x+y+z)

# print(result)


# 2- y' nin  x' e kalansız bölümünü hesaplayınız.
# print(y//x)

# result = y//x


# 3- (x,y,z) toplamının mod 3' ü nedir ?

result = (x+y+z) % 3


# 4- y' nin x. kuvvetini hesaplayınız.

result = y ** x


# 5- x, *y, z = numbers işlemine göre z' nin küpü kaçtır ?

x, *y, z = 1, 5, 7, 10, 6
# print(x)
# print(y)
# print(z)
# result = z ** 3
# print(216/6)


# 6- x, *y, z = numbers işlemine göre y nin değerleri toplamı kaçtır ?


x, *y, z = 1, 5, 7, 10, 6
result = y[0] + y[1] + y[2]
print(result)
