
# def change(n):
#     n[0] = 'Istanbul'


# sehirler = ['İzmir', 'Hatay']


# change(sehirler)

# print(sehirler)


# def add(a, b, c):
#     return sum((a, b, c))


# print(add(10, 20, 40))

# def add(*gelenVeri):
#     return sum((gelenVeri))


# print(add(10, 2, 3, 5, 10, 30, 40, 50, 60))


# def displayUser(**args):
#     for key, value in args.items():
#         print('{} is {}'.format(key, value))


# displayUser(name='Layane', age=31, city='Brazil')
# displayUser(name='Zoe Nisa', age=3, city='Malta', phone='865355232')
# displayUser(name='Mehmet', age=35, city='Turkiye',
#             phone='99694956', email='mehmet@gmail.com')


def myFunction(a, b, c, *args, **kwargs):
    print(a)
    print(b)
    print(c)
    print(args)
    print(kwargs)


print(myFunction(1, 2, 3, 4, 5, 6, 7, 8,
      key1='value 1', key2='value 2', key3='value 3'))
