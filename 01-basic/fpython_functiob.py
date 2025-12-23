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


 