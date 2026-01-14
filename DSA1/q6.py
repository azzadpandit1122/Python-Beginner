# class Cart:
#     pass

# c1 = Cart()
# print(c1)

# class Cart:
#     def __str__(self, basket1, basket2, basket3):
#         self.clothes = basket1
#         self.electronic = basket2 
#         self.other = basket3

#     def __len__(self):
#         print("total number of item in cart:") 
#         return len(self.clothes) + len(self.electronic) + len(self.other)   
    
# ss = Cart(["pant", "shirt","saree"], ["Earphone", "headphone", "neckband"], ["ddd", "wdvgv", "hjc"])
# # print(ss)
# print(len(ss))

class Addition:
        def add(self, numa, numb, numc):
            print("addition is :", numa + numb + numc)

        def add(self, num1, num2):
            print("addition is :", num1 + num2)

a = Addition()
a.add(100, 20)
# a.add(100, 20, 30)
# print(a.add)       

class Addition:
     def add(self, num1=None, num2= None, num3=None):
          if num1 != None and num2 != None and num3 != None:
               print("addition is : ", num1 + num2 + num3)
        
          elif  num1 != None and num2 != None :
               print("Add is :", num1 + num2)

          else:
              print("incorrect parameter provided")   

c1 = Addition()     
c1.add(10, 20, 30)
c1.add(10, 20)
# c1.add(20, 30, 40, 50)        
class Addition:
     def add(self, num1=None, num2= None, num3=None):
          if num1 != None and num2 != None and num3 != None:
               print("addition is : ", num1 + num2 + num3)
        
          elif  num1 != None and num2 != None :
               print("Add is :", num1 + num2)

          else:
              print("incorrect parameter provided")   

c1 = Addition()     
c1.add(10, 20)
c1.add(10, 20, 30)
# c1.add(20, 30, 40, 50) 

class Addition:
     def add(self, num1, num2, num3):
          if num1 and num2 and num3 :
               print("addition is : ", num1 + num2 + num3)
        
          elif  num1 and num2:
               print("Add is :", num1 + num2)

          else:
              print("incorrect parameter provided")   

c1 = Addition()     
c1.add(10, 20, 30)
# c1.add(10, 20)
# c1.add(20, 30, 40, 50) 

class Add:
    def __gt__(self, other):
       num1 = self.value
       num2 = other.value
       if num1 > num2:
            print("True")

       else:
            print("False")    
a1 = Add()
a1.value = 10
a2 = Add()
a2.value = 6
a1 > a2

class Add:
    def __gt__(self, other):
       num1 = self.value
       num2 = other.value
       if num1 > num2:
            print("True")

       else:
            print("False")    
a1 = Add()
a1.value = 10
a2 = Add()
a2.value = 6
a1 > a2


# class Car:
#     def show_color(self, color):
#         self.color = color        
#         print(self.color)

# c1 = Car("Red", "bjh")
# c1.show_color()  # ERROR! kyunki color parameter nahi mila

class Car:
     def __init__(self, color):
          self.color = color

     def show_color(self):
          print(self.color)   

c1 = Car("Red")
c1.show_color()    

class Function:
   def __init__(object, phone, laptop):
      object.phone = phone
      object.laptop = laptop

   def greet(aaa):
      print("hello, I have a" + aaa.phone, aaa.laptop)

T1 = Function("fhgd", "fyuf")
T1.greet()   

class Area:
     def area(self, l =0, b = 0):
          if l > 0 and b > 0:
               print("Area of rectangle:", l * b )
          elif l > 0 and b == 0:
               print("Area of square: ", l * l)    

a  = Area()
a.area(10)
a.area(10, 20)

class Outer :
     def __init__(self):
          print("Outer class constructor called")

     def display(self):
          print("This is display method")    

     class inner :
          def __init__(self):
               print("This class contructor called")

          def show(self):
               print("This is show method")

obj = Outer()
inn = obj.inner()
inn.show()
inn.__init__()
obj.display()
obj.__init__()

class Student:
     def __init__(self, name, roll, dd, mm, yy):
          self.name = name
          self.roll = roll
          self.DoB = self.DOB(dd, mm, yy)

     def  display(self):
          print(f"name is {self.name} and  roll is {self.roll}")
          self.DoB.display()


     class DOB:
          def __init__(self, dd, mm, yy):
               self.dd = dd
               self.mm = mm
               self.yy = yy

          def display(self):
               print(f"date of birth is {self.dd}/{self.mm}/{self.yy}")

s1 = Student("ajay", 67, 12, 6, 1999)              
s1.display()




        