# import datetime

# x = datetime.datetime.now()
# print(x)

# x = datetime.datetime.now()
# print(x.year)


# i = 1
# while i < 6:
#   print(i)
#   i += 1
  
#   num = 4
#   for x in range(4):
#     print(x)

# import json

# x = {
#   "child1": {
#   "name" : "Emil",
#   "year" : 2004
# }, 
# "child2" : {
#   "name" : "Tobias",
#   "year" : 2007
# }, 
# "child3" : {
#   "name" : "Linus",
#   "year" : 2011
# }
# }
# y = json.dumps(x)
# print(y)

# import json

# print(json.dumps({"name": "John", "age": 30}))
# print(json.dumps(["apple", "bananas"]))
# print(json.dumps(("apple", "bananas")))
# print(json.dumps("hello"))
# print(json.dumps(42))
# print(json.dumps(31.76))
# print(json.dumps(True))
# print(json.dumps(False))
# print(json.dumps(None))


import json
x = {
  "car" :[
  {"name" : "laptop" , "brand" : "dell"},
  {"name1": "laptop1" , "brand1" : "hp"}
  ]
}
print(json.dumps(x))

x = {
  "car" :[
  {"name" : "laptop" , "brand" : "dell"},
  {"name1": "laptop1" , "brand1" : "hp"}
  ]
}
print(json.dumps(x,  indent =5))

import re

txt = "The rain in Spain"

#Find all lower case characters alphabetically between "a" and "m":

x = re.findall("[a-m]", txt)
print(x)

text  = "it is a 589 doller"
x = re.findall("[1-9]" , text)
print(x)

import re

txt = "hello planet"

#Search for a sequence that starts with "he", followed by two (any) characters, and an "o":

x = re.findall("he..o", txt)
print(x)

txt = "the rain im spain"
x = re.sub("\s" , "7" , txt)
print(x)

# import re

# import camelcase

# x = camelcase.camelcase()

# text = "today is a sunday"

# print(x.hump(text))

# import camelcase

# c = camelcase.CamelCase()

# txt = "lorem ipsum dolor sit amet"

# print(c.hump(txt))

txt = f"the rain im spain"
print(txt)

text = f"today is a sunday"
print(text)

text = "today is a sunday"
print(text.upper())

txt = f"{5:b}"
print(txt)

txt = f"{1011:d}"
print(txt)

x = float('inf')

txt = f"The price is {x:F} dollars."
print(txt)

#same example, but with a lower case f:

txt = f"The price is {x:f} dollars."
print(txt)

# age = 36
# name = "John"
# txt = "His name is {1}. {1} is {0} years old. i read in c class {2}"
# print(txt.format(age, name))

import math

num = int(input("Enter a number: "))
x = math.sqrt(num)
print(x)