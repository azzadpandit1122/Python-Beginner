# x = ("market", "school", "university", "college")
# x.insert(2, "kiwi")
# print(x)


x = ("market", "school", "university", "college")
print(len(x))


mytuple = ("apple", "banana", "cherry")
print(type(mytuple))



mytuple = ("apple", "banana", "cherry",)
print(type(mytuple))


mytuple = ("apple", "banana", "cherry",)
print(len(mytuple))


# mytuple = tuple(("apple", "banana", "cherry"))
# print(mytuple)

x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)
print(x)


mytuple = ("apple", "banana", "cherry")
y = list(mytuple)
y.append("orange")
mytuple = tuple(y)        
print(y)


thistuple = ("apple", "banana", "cherry")
y = ("orange",)
thistuple += y
print(thistuple)


# thistuple = ("apple", "banana", "cherry")
# y = ("orange")
# thistuple += y
# print(thistuple)

mytuple = ("dell", "hp", "lenovo", "asus")
y = list(mytuple)
y.remove("hp")
print(y)


# mytuple = ("dell", "hp", "lenovo", "asus")
# del mytuple(0)
# print(mytuple)


mytuple = ("dell", "hp", "lenovo", "asus")
for x in mytuple:
    print(x)

A = ("computer", "monitor", "keyboard", "mouse",) 
b = A*3 
print(b)  

# A = ("computer", "monitor", "keyboard", "mouse",) 
# b = A + 3 
# print(b)  
                              

# A = ("computer", "monitor", "keyboard", "mouse",) 
# b = A - 3 
# print(b)  


# mytuple = ('apple', 'banana', 'cherry')
# i = 2
# while i < len(mytuple):
#   print(mytuple[2])
#   i = i + 1


mytuple = ("apple", "banana", "cherry")
x =  list(mytuple)
x.remove("apple")
print(x)


mytuple = ("apple", "banana", "cherry")
x =  list(mytuple)
x.append("how are you")
print(x)