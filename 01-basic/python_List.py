mylist = list(('apple', "name", "age", 2, 7))
print((mylist))


mylist = list(('apple', "name", "age", 2, 7))
print(len((mylist)))



mylist = list(('apple', "name", "age", 2, 7))
print((mylist[-1]))


mylist = list(('apple', "name", "age", 2, 7))
print((mylist[1]))



mylist = list(('apple', "name", "age", 2, 7))
print((mylist[2:4]))



mylist = list(('apple', "name", "age", 2, 7))
print((mylist[:-6]))



mylist = list(('apple', "name", "age", 2, 7))
print((mylist[-3:]))


# mylist = list(('apple', "name", "age", 2, 7))
# print((mylist[-3:-1]))


mylist = list(('apple', "name", "age", 2, 7))
print((mylist[-3:1]))


mylist = list(('apple', "name", "age", 2, 7))
print((mylist[3:5]))

mylist = list(('apple', "name", "age", 2, 7))
print((mylist[-3:3]))

thislist = ['abcd', "xyz", "pqr", "tfdfs"]
if "xyz" in thislist:
    print("yes")

    mylist = ["appl", "banana", "cherry"]
    mylist[2] = ["black", "water"]
    print(mylist)
                 

    mylist = ["appl", "banana", "cherry", "orange", "kiwi", "mango"]
    mylist[1:5] = ["black", "water"]
    print(mylist)


    mylist = ["appl", "banana", "cherry", "orange", "kiwi", "mango"]
    mylist[1:2] = ["black", "water"]
    print(mylist)


    mylist = ["appl", "banana", "cherry", "orange", "kiwi", "mango"]
    mylist.insert(2, "watermelon")
    print(mylist)


    mylist = ["appl", "banana", "cherry", "orange", "kiwi", "mango"]
    mylist.insert(2, "cucumber")
    print(mylist)


    mylist = ["appl", "banana", "cherry", "orange", "kiwi", "mango"]
    mylist[2] = ["cucumber"]
    print(mylist[3])


    mylist = ["appl", "banana", "cherry", "orange", "kiwi", "mango"]
    mylist.remove("cherry")
    print(mylist)



mylist = ["appl", "banana", "cherry", "orange", "kiwi", "mango"] 
mylist.pop(2)
print(mylist)

thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)


thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist)


thislist = ["apple", "banana", "cherry"]
thislist.pop(-3)
print(thislist)


thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)


thislist = ["apple", "banana", "cherry"]
del thislist[-2]
print(thislist)


# thislist = ["apple", "banana", "cherry"]
# thislist.clear(-2)
# print(thislist)


thislist = ["apple", "banana", "cherry"]
for x in thislist:
    print(x)


thislist = ["name", "age", "pot", "city"]
for x in thislist:
  print(x)

thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
  print(thislist[i])


#   x = ["phone", "laptop", "tablet"]
#   for y in x:
#     print(y)


# thislist = ["apple", "banana", "cherry"]
# [print(x) for x in thislist]


# # thislist = ["apple", "banana", "cherry"]
# # i = 3
# # while i < len(thislist):
# #    print(thislist[3])
# #    i =  i + 1


# list1 = ["a", "b", "c"]
# list2 = ["a", "b", "c"]
# for x in list2:
#    list1.append(x)
# print(list1)

# list = ["abc", "def", "xyz"]
# for x in list:
#    print(x)

