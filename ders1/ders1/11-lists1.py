# message = "Mehmet Beşir ile derslermimiz devam ediyor. Bu 3. ders"
            
# result = message.split()

# print(result)
# print(type(result))
# print(type(result[1]))

# my_list = [1,2,3]
# my_list = [1, 2.3, True, "Eren"] #-> C# array türünü belirtmeniz gerekir int[] 
# print(my_list)
# print(type(my_list))

# list1 = ["bir","iki","üç"]
# list2 = ["dört","beş","altı"]
# numbers = list2 + list1
# print(numbers[3])

# # print(type(numbers))

userEren = ["Eren",21,"Erkek"]
userMehmet = [[["Mehmet",35,"Erkek",userEren]]]
users = [userEren, userMehmet]

                                                                    # print(users[0])
                                                                    # print(users[1])
                                                                    # user1 = users[0]#-> [Eren, 21 , erkek]
                                                                    # print(user1[0]) # - Eren

print(users[1][0][0][3][0][1])



