car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.keys()

print(x) #before the change

car["color"] = "red"

print(x)

car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.values()

print(x) #before the change

car["year"] = 2020

print(x) #after the change

car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.get("year")
print(x)

# car = {
# "brand": "Ford",
# "model": "Mustang",
# "year": 1964
# }

# x = car.keys("brand")
# print(x)


# car = {
# "brand": "Ford",
# "model": "Mustang",
# "year": 1964
# }

# x = car.values("year")
# print(x)

car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.items()
car["age"] = 34
print(x)


dict = {"type" : "fruits" , "name" : "banana"}
y = dict.get("type")
print(y)


x = {"type" : "fruits" , "name" : "banana"}
print(x["name"])


thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
if "brand" in thisdict:
    print("yes")

dict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
dict["year"] = 2022
print(dict)

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.update({"year": 2020})
print(thisdict)
    
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.update({"color" : "silver"})
print(thisdict)

# fruits =  {'name' :'prachi', "age" : 20, 'year' : 2025}
# x = fruits.pop()
# print(x)
# fruits["age"] = 20
# print(x)

fruits =  {'name' :'prachi', "age" : 20, 'year' : 2025}
fruits.pop('age')
print(fruits)

fruits =  {'name' :'prachi', "age" : 20, 'year' : 2025}
fruits.popitem()
print(fruits)


fruits =  {'name' :'prachi', "age" : 20, 'year' : 2025}
del fruits["age"]
print(fruits)


fruits =  {'name' :'prachi', "age" : 20, 'year' : 2025}
fruits.clear()
print(fruits)


num1 = int(input("enetr a number: "))
sr = num1**(1/2)
print("the square root of the given number is", sr)