class first:
    a = ("fuywf", "jdgf", "fhd")
    
b = first()
print(b.a)

class Person:
  pass

p1 = Person()
p1.name = "Tobias"
p1.age = 25

print(p1.name)
print(p1.age)

age = 54
name = "gdf"
nvcy = f"my name is {name}, i am {age} year old"
print(nvcy)

class  myfirstclass:
   pass
x = myfirstclass()
x.name = "sagar"
x.age = 67
x.year = 2025

a = f"i am {x.name}, my currently {x.age}, and in this {x.year} year)"
print(a)
# print(x.age)
# print(x.year)

# class firstclass:
#      def __inti__(self, name, age, year):
#         self.name = name
#         self.age = age
#         self.year = year
        
# a = firstclass("sagar", 34, 1587)

# print(a.name)     
# print(a.age)    
# print(a.year)     

# class Person:
#   def __init__(self, name, age, city, country):
#     self.name = name
#     self.age = age
#     self.city = city
#     self.country = country

# p1 = Person("Linus", 30, "Oslo", "Norway")

# print(p1.name)
# print(p1.age)
# print(p1.city)
# print(p1.country)

a = 4
b = 2
c = a/b
print(c)


num = {"fsr", "dt", "fgvk"}

num.remove("dt")
print("update list: \n", num)

num = {"fsr", "dt", "fgvk"}
print(num)

num.add("hfygjh")
print("update list: \n", num)

total = 1
for i in range(1, 11):
   total += i
   print(i)

total = 1
for i in range(1, 7):
   total += i
   print(i)

   
total = 0
for i in range(1, 7):
   total += i
print(f"sum is", {total})

total = 1
for i in range(1, 7):
   total *= i
print("multiply is", total)

total = 0
for i in range(1, 20):
    total += i
print(f"sum is {total}")

total = 1
for i in range(1, 5):
    total *= i
print("multiply is", total)

total = 1
for i in range(1, 5):
    total -= i
print(f"subtract is", {total})

class person:
   pass

p1 = Person()
p1.name = "sagar"
p1.age = 45
p1.country = "India"

print(p1.name)
print(p1.country)
print(p1.age)

class laptop:
   pass 

p1.name = "Tommy"
p1.country = "america"
p1.age = 34

x = f"my name is{p1.name}, my currently age {p1.age}, currently live in this {p1.country} country."
print(x)

def my_function():

   x = 56
   y = 66
   print("x:", x)
   print("y:", y)

my_function()

def my_firstfunction(x , y):
  return x + y

result = my_firstfunction(64653696, 65568)
print(result)

def bvgdyt():
   return("dchfytd" , "dtruyc", "e7rfcv")

hgjh = bvgdyt()

print(hgjh[2])

class Myfunction:
   def __init__(self, name, age):
      self.name = name
      self.age = age

   # def greet(self):
      print("hello, my name is " + self.name)
      
p1 = Myfunction("hvdufds", 56)
# p1.greet()


class Myfunction:
   def __init__(self, name):
      self.name = name

   def printname(self):
      print(self.name)

p3 = Myfunction("fdyusfdv")
p1 = Myfunction("fasdv")

p3.printname()
p1.printname()

class Person:
  def __init__(myobject, name, age):
    myobject.name = name
    myobject.age = age

  def greet(abc):
    print("Hello, my name is " + abc.name)

p1 = Person("Emil", 36)
p1.greet()


class Function:
   def __init__(ccc, era, auro):
      ccc.era = era
      ccc.auro = auro

   def greet(abc):
      print("gfc bnbngvm, gugj isfc igdfv" + abc.era)

T1 = Function("gfcvg", "gfrtc")
T1.greet()        

class function():
    pass

p1.name = "yryfc"
p1.age = 65
p1.number = "America"

x = f"chf, cfdt  uitfv duyfc {p1.name}, {p1.age}, {p1.number} fytcv"
print(x)

class Function:
   def __init__(ccc, era, auro):
      ccc.era = era
      ccc.auro = auro

   def greet(object):
      return "Hello, " + object.era , object.auro
   
   def welcome(fff):
      message = fff.greet()
      print(message , "welcome in our learn python develope ")

p1 = Function("tyytdc", "bhs")
p1.welcome()    

class Function:
   def __init__(object, phone, laptop):
      object.phone = phone
      object.laptop = laptop

   def greet(aaa):
      print("hello, I have a" + aaa.phone, aaa.laptop)

T1 = Function("fhgd", "fyuf")
T1.greet()   


class Object:
   def __init__(self, jh, ydc):
      self.jh = jh
      self.ydc = ydc


   def greet(hhh):
      return "Hello," + hhh.jh, hhh.ydc

   def welcome(jjj):
      msg = jjj.greet()
      print(msg, "vhfff udch jv dvd ")

p1 = Object("bjsdhgv", 7867)
p1.welcome()

class Phone:
   def __init__(self, hhh):
      self.hhh = hhh
      # self.gggg = gggg

   def name(vvv):  
    print(vvv.hhh)

Y3 = Phone("vivi")
Y4 = Phone(67)
Y5 = Phone("gjhfhv")

Y3.name()
Y4.name()
Y5.name()

class Phone:
   def __init__(self, hhh, gggg):
      self.hhh = hhh
      self.gggg = gggg

p1 = Phone("gjhg", 765)    

print(p1.hhh)
print(p1.gggg)