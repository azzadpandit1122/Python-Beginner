
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
     def __init__(self, name, age):#method:
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

class Main():
     company_name = "wipro"
     def __init__(self, name, marks):
          self.name = name
          self.marks = marks
     
     def person(self):
          print(self.name, self.marks)

     def change_data(self):
          self.name = input('Enter an name: ')    
          self.marks = input('Enter a number: ')

std1 = Main("jay", 98)
std2 = Main('roy', 99)
std3 = Main('rai', 97)

std1.person()
std2.change_data()
print(std2. __dict__)
Main.company_name = "TCS"
print(Main. company_name)  #wipro
std2. company_name = 'salesforce'
print(std2. company_name)   #salesforce

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

class Employee():        
  def SetName(self, mn):        #setter method
       self.name = mn

  def getName(self):        #getter method
     print("The name is" , self.name)
     
e1 = Employee()
e2 = Employee()

e1.SetName(input("Enter a name: "))
e2.SetName(input("Enter a name; "))
print("e1 object is: " , e1.__dict__)
print("e2 object is: " , e2.__dict__)
e1.getName()
e2.getName()

class Employee:
     bonus = 1000
     def display(self):  #inheritance method
          print("this is employee class method")

     def Manager(Employee):
          bonus1 = 2000
          def show(self):
               print("This is manger class method")






