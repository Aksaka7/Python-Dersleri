
# def square(num): return num ** 2


# numbers = [1, 18, 5, 6, 8, 9, 12, 13, 15, 22]

# # result = list(map(lambda num: num**2, numbers))
# # result = list(map(square, numbers))


# # GElecek olan sayıların sadece  çift olanlarını bize filtrele

# def check_Even(num): return num % 2 == 0


# # result = list(filter(check_Even, numbers))
# result = list(filter(lambda num: num % 2 == 0, numbers))

# print(result)


name = 'mehmet'


# def yaziyiBuyult(a):
#     print(a.upper())

#     def hello(): print(f"Merhaba {a}")
#     hello()


# yaziyiBuyult('Asım')


x = 50


def test():
    global x
    print(f"{x} burda Global")
    x += 20


test()
test()
test()
print(x)
