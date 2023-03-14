x = 5

hak = 0
devam = "e"

result = 5 < x < 10
# print(result)

#True, True -> True
#True,False -> False


#and  türkçede ve anlamına gelir 1 and 1 = 1, 1 and 0 = 0, 0 and 0 = 0
# or türkçede veya anlamına gelir 1 or 1 = 1, 1 or 0 = 1 , 0 or 0 = 0


 

result = (x > 5) and (x < 10)
result = (hak > 0) and (devam == "e")


#Sayı çift mi veya 0 dan büyük mü 
result = ((x % 2) == 0) or (x > 0)

result = not (x < 20)



# x 5-10 arasında olan bir çift sayı mı 
x = 6
result = ((x>5) and (x<10)) and (x % 2 == 0)

print(result)