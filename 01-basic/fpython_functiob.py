print("namste")

def myfunction():
    print("values")
myfunction()

temp = 77
celsius = (temp - 32) * 5/9
print(celsius)

# def my_function():
#   print(" Refsnes")

# my_function("Emil")
# my_function()
# my_function("Linus")

def my_function(name): # name is a parameter
    print("Hello", name)      

my_function("Emil")

# This function expects 2 arguments, and gets 2 arguments::

def my_function(fname, lname):
  print(fname + " " + lname)

my_function("Emil", "Refsnes")

# def my_function(fname, lname):
#   print(fname + " " + lname)

# my_function("Emil")

# def my_function(name = "friend"):
#   print("Hello", name)

# my_function("Emil")
# my_function("Tobias")
# my_function()
# my_function("Linus")

def my_function(country = "Norway"):
  print("I am from", country)

my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")


def my_function(animal, name):
  print("I have a", animal)
  print("My", animal + "'s name is", name)

my_function(name = "Buddy", animal = "dog")


def my_function(animal, name):
  print("I have a", animal)
  print("My", animal + "'s name is", name)

my_function("dog", "Buddy")

def my_function(animal, name):
  print("I have a", animal)
  print("My", animal + "'s name is", name)

my_function("Buddy", "dog")

def my_function(animal, name, age):
  print("I have a", age, "year old", animal, "named", name)

my_function("dog", name = "Buddy", age = 5)

def my_function(fruits):
  for fruit in fruits:
    print(fruit)

my_fruits = ["apple", "banana", "cherry"]
my_function(my_fruits)


def my_function(x, y):
  return x + y

result = my_function(5, 3)
print(result)


def my_function():
  return ["apple", "banana", "cherry"]
fruits = my_function()
print(fruits[0])
print(fruits[1])
print(fruits[2])



def my_function():
  return (10, 20)
x, y = my_function()
print("x:", x)
print("y:", y)

# def my_function(name, /):
#   print("Hello", name)

# my_function("Emil")

# def my_function(name):
#   print("Hello", name)

# my_function(name = "Emil")


# def my_function(name, /):
#   print("Hello", name)

# my_function(name = "Emil")

# def my_function(*, name):
#   print("Hello", name)

# my_function(name = "Emil")

# def my_function(name):
#   print("Hello", name)

# my_function("Emil")

# def my_function(*, name):
#   print("Hello", name)

# my_function("Emil")

def my_function(a, b, /, *, c, d):
  return a + b + c + d

result = my_function(5, 10, c = 15, d = 20)
print(result)


# def my_function():
#   print(my_function)

# my_function("Emil", "Refsnes")


animal = "dog"
name = "pet"
my_function = f"my {animal} is a {name}"
print(my_function)

def my_function(animal):
  print("gfytrjnifdydcbnhf", animal , "src xn df xgftsgf")
my_function("dog")

def my_function(animal = "edgff"):
  print("gfytrjnifdydcbnhf", animal , "src xn df xgftsgf")
my_function()


def my_function(animal = "edgff"):
  print("gfytrjnifdydcbnhf", animal , "src xn df xgftsgf")
my_function()
my_function("dxgghgc")
my_function("gsyr")

def my_function(x , y):
    print("x:", x)
    print("y:", y)
my_function(10, 50)    


def function(wifi, *name):
  for x in name:
   print(wifi, x)
   function("fruits", "animal", 'cftyd')


def my_function(greeting, *names): 
    for x in names:
      print(greeting, x)

my_function("Hello", "Emil", "Tobias", "Linus")


# def my_function(*numbers):
#   total = 0
#   for num in numbers:
#     total += num
#   return total

# print(my_function(1, 2, 3))
# print(my_function(10, 20, 30, 40))
# print(my_function(5))

# def my_function():
#   for num in number:
#     tatol +=num
#     print(my_function(3, 5, 6, 8, 7))

num = [80, 56, 5,78]
for y in range(3):
    print(num)


num = 50
for i in range(1, 5):
    print(num*i)

x = 6
for i in range(2, 10):
   print(x*i)

#    x = [2, 9, 1]
# for i in range(6):
#    print(x*i)

x = range(2, 9, 1)
print(7 in x)

r = range(0, 10, 2)
print(list(r))
print(len(r))

x = 50
for i in range(2):
  print(x)
