mytuple = ("apple", "banana", "cherry")
myit = iter(mytuple)

print(next(myit))
print(next(myit))
print(next(myit))

mytuple = ("apple", "banana", "cherry")
for x in mytuple:
    print(x)
