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


thisset = {"apple", "banana", "cherry"}
del thisset

print(thisset)