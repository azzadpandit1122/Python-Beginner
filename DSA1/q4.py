
class Person():
      def __init__(self, name1, name2):
            self.name1 = name1
            self.name2 = name2

p1 = Person("mike", "osle")     
print(p1.name1 , p1.name2)
# print(p1.name2)

class Person():
      def __init__(self, name, name2):
            self.name = name
            self.name1 = name2

      def printname(self):
            print(self.name, self.name1)

class Student(Person):
      def __init__(self, name, name1):
        Person. __init__(self, name, name1)  

x = Student("Mike", "Osle")
x.printname()


# created class
class Employee():
     def __init__(self, name, age):    #method:
          self.name = name
          self.age = age

    #  def __init__(se)     
e1 = Employee("jay", 22)
e2 = Employee("ray", 23)
print(getattr(e1, "age"))  #22
setattr(e2, "name", 'mohan')
print(e2. __dict__)
delattr(e1, 'age')
print(e1. __dict__)
print(hasattr(e1, 'pen'))

print(Employee. __doc__)
print(Employee. __dict__)
print(Employee. __name__)
print(Employee. __module__)

# class Main():
#      company_name = "wipro"
#      def __init__(self, name, marks):
#           self.name = name
#           self.marks = marks
     
#      def person(self):
#           print(self.name, self.marks)

#      def change_data(self):
#           self.name = input('Enter an name: ')    
#           self.marks = input('Enter a number: ')

# std1 = Main("jay", 98)
# std2 = Main('roy', 99)
# std3 = Main('rai', 97)

# std1.person()
# std2.change_data()
# print(std2. __dict__)


# Main.company_name = "TCS"
# print(Main. company_name)  #wipro
# std2. company_name = 'salesforce'
# print(std2. company_name)   #salesforce

class Main():
     company_name = "wipro"
     def __init__(self, name, marks):
          self.name = name
          self.marks = marks
     @classmethod
     def person(cls):
          print(cls.company_name)


std1 = Main("jay", 98)
std2 = Main('roy', 99)

Main.person()

# class Employee():        
#   def SetName(self, mn):        #setter method
#        self.name = mn

#   def getName(self):        #getter method
#      print("The name is" , self.name)
     
# e1 = Employee()
# e2 = Employee()

# e1.SetName(input("Enter a name: "))
# e2.SetName(input("Enter a name; "))
# print("e1 object is: " , e1.__dict__)
# print("e2 object is: " , e2.__dict__)
# e1.getName()
# e2.getName()

class Employee:
     bonus = 1000
     def display(self):  #inheritance method
          print("this is employee class method")

class Manager(Employee):
     bonus1 = 2000
     def show(self):
          print("This is manager class method")

e1 = Employee()
m1 = Manager()

e1.display()
m1.show()
print(m1.bonus1)
print(e1.bonus)

class Father:
     def __init__(self):
          print("Father constructor called")
          self.vehicle = "scooter"

class Son(Father):
     def __init__(self):
          print("Son constructor called")
          self.vehicle = "BMW"

s = Son
print(s.__dict__)        

class Computer(object):
     def __init__(self):
          self.ram = "8gb"
          self.storage = "512gb"
          print("Compuete class constructor call")

class Mobile(Computer):
          def __init__(self):
               # super().__init__()
               self.model = 'iphone  x' 
               print("Mobile class constructor call")

Apple = Mobile()                
print(Apple.__dict__)

class Computer(object):
     def __init__(self, ram , storage):
          self.ram = ram
          self.storage = storage
          print("Compuete class constructor call")


     # def display(self):
          # print("hello World")    

class Mobile(Computer):
          def __init__(self, ram , storage):
               super().__init__(ram, storage)
               self.model = 'iphone  x' 
               print("Mobile class constructor call")

Apple = Mobile("8gb", "512gb")                
print(Apple.__dict__)

# constructor in multi_level inheritance
# class human_being(object):
#   def __init__(self):
#        self.name = input("Enter a name: ")
#        print("human being constructor called")

# class Employee(human_being):
#   def __init__(self):
#        self.salary = float(input("Enter a salary: "))
#        print("employee constructor called")

# class Manager(Employee):
#   def __init__(self):
#        self.bonus = float(input("Enter a bonus: "))
#        print("Manager constructor called")

# # pass

# m1 = Manager()      

class human_being(object):
     # def __init__(self):
       pass

class Employee(human_being):
     # def __init__(self):
       pass

class Manager(Employee):
     # def __init__(self):
       pass

e1 = Employee()    

class Human_being(object):
     # def __init__(self):
          salary = 1224334

class Employee(Human_being):
     salary = 125465 

class Manager(Employee):
     sallary = 5757887
     
e1 = Employee()
print(e1.salary)   #125465


# hieracal inheritance
class Person():
     def __init__(self, mn, ag):
          self.mn = mn
          self.ag = ag
     def display(self):
          print("This is person display method")


class Employee(Person):
     def __init__(self, mn, ag, sal):
          super().__init__(mn, ag)
          self.sal = sal
     def display1(self):
          print("This is employee display method")


class Student(Employee):
     def __init__(self, mn, ag, m):
          super().__init__(mn, ag, m)
          self.m = m
     def display2(self):
          print("This is student display method")

s1 = Student("jay", 20, 99)
e1 = Employee("rai", 34, 787)
p1 = Person("bbb", 20)

s1.display()
s1.display1()

p1.display()
# p1.display2()


# multiple inheritance
class Country:
      office = "delhi"

class State:
      office = "Mumbai" 

class district:
      pass     

d = Country()
print(d.office)

class Country:
     def __init__(self):
           self.office = "delhi"
class State:
      def __init__(self):
            self.office = "Mumbai"

class district:
      pass     

d = Country()
print(d.office)

class A:
    pass
class B:
      pass
class C:
      pass
class X(A, B, C):
      pass
class Y(B, C):
      pass
class P(X, Y):
      pass
print(P.mro())

