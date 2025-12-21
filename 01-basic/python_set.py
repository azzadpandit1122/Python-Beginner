myset = {"apple", "banana", "cherry"}
print(myset)

set = {"laptop", 'desktop', "tablet", "smartstone", True, 1}
print(set)

thisset = {"apple", "banana", "cherry", True, 1, 2}
print(thisset)

thisset = {"apple", "banana", "cherry", True, False, 1, 2}
print(thisset)

thisset = {"apple", "banana", "cherry", True, False, 1, 2}
print(len(thisset))



thisset = {"apple", "banana", "cherry", True, False, 1, 2}
print(type(thisset))


# thisset = set(("apple", "banana", "cherry", "True", "False", 1, 2))
# print(thisset)

thisset = {"apple", "banana", "cherry", "True", "False", 1, 2}
thisset.add("orange")
print(thisset)


thisset = {"apple", "banana", "cherry", "True", "False", 1, 2}
tropical  = {"mango", "pineapple", "papaya"}
thisset.update("tropical")
print(thisset)


thisset = {"apple", "banana", "cherry", "True", "False", 1, 2}
tropical  = ["mango", "pineapple", "papaya"]
thisset.update("tropical")
print(thisset)


thisset  = {"mango", "pineapple", "papaya"}
thisset.discard("pineapple")
print(thisset)


thisset  = ["mango", "pineapple", "papaya"]
x = thisset.pop()
print(x)
print(thisset)



thisset  = {"mango", "pineapple", "papaya"}
thisset.clear()
print(thisset)


# thisset = {"apple", "banana", "cherry"}
# del thisset

# print(thisset)

set1 = {"google", "microsoft", "Apple"}
set2 = {"phone", "Apple", "fruits"}
set3 = set1.intersection(set2)
print(set3)


set1 = {"google", "microsoft", "Apple"}
set2 = {"phone", "Apple", "fruits"}
set3 = set1 & set2
print(set3)

set1 = {"google", "microsoft", "Apple"}
set2 = {"phone", "Apple", "fruits"}
set1.intersection_update(set2)
print(set1)

set1 = {"google", 0, "microsoft", 1,"Apple"}
set2 = {False, "phone", True, "Apple", "fruits"}
set3 = set1.intersection(set2)
print(set3)


set1 = {"google", 0, "microsoft", 1,"Apple"}
set2 = {False, "phone", True, "Apple", "fruits"}
set3 = set1.difference(set2)
print(set3)


set1 = {"google", 0, "microsoft", 1,"Apple"}
set2 = {False, "phone", True, "Apple", "fruits"}
set3 = set1 -set2
print(set3)

set1 = {"google", 0, "microsoft", 1,"Apple"}
set2 = {False, "phone", True, "Apple", "fruits"}
set3 = set1.difference_update(set2)
print(set2)

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.symmetric_difference(set2)
print(set1)

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1 ^ set2
print(set1)


set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set1.symmetric_difference_update(set2)
print(set1)
