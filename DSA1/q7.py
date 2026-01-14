# class Employee:
#     def __init__(self, eid, name, sallary):
#         self.emp_id = eid
#         self.emp_name = name
#         self.emp_sall = sallary

#     def display(self):
#         print("Empoyee id:", self.emp_id)
#         print("Empoyee id:", self.emp_name)
#         print("Empoyee id:", self.emp_sall)

# class Change:
#     @staticmethod
#     def increment(obj):
#         obj.emp_sall = obj.emp_sall + 20000
#         obj.display()

# e1 = Employee(101, "shantanu", 500000)
# Change.increment(e1)       
# e1.display()

import time

class Employee:
    def __init__(self, mm, sal):
     self.nn = mm
     self.sall = sal

    def display(self):
        print(f" Name is {self.nn} and salllary is {self.sall}")

        #defining dsetructor
    def __del__(self):
        print("Destructor is called")

e1 = Employee("shantanu", 500000)
e2 = e1
del e1

time.sleep(1)

# class Employee:
#     def __init__(self, obje2):
#         self.oj2 = obje2

#     def __del__(self):
#         print("Employee clas costructor called") 

# class Account:
#    def __init__(self, num):
#        self.account_number = num
#        self.obje2 = Employee(self)
       
#    def __del__(self):
#        print("Account class destructor called")   

# ac = Account(1234)
# del ac

# time.sleep(2)

# class NegativeAge(Exception):
#     pass

# class Age:
#     def __init__(self, ag):
#         if ag < 0:
#             raise NegativeAge("Age cannot  be negative")
        
#     def __del__(self):
#             print("Destructor is called")

# ag = Age(-10)           

# class Movies(object):
#    def __init__(self, title, mins, hero):
#         self.title = title
#         self.mins = mins
#         self.hero = hero

#    def printer(self):
#        print(f" this is : {self.title}\n runtime is : {self.mins} \n hero is : {self.hero}")

# list_of_movies = []
# while True:
#     title = input("Enter the title of movies:")               
#     mons = input("Enter the runtime of movies:")              
#     hero = input("Enter the name of hero of movies:")         
#     obj = Movies(title,mons,hero)   
#     list_of_movies.append(obj)
#     print("Movies added into  the list")
#     ans = print("do you want to add another movies(y/n)")
#     if ans != 'y':
#         break

class Decorator(object):
    def __init__(self, func):
        self.function = func

    def __call__(self, a, b):
        result = self.function(a, b) 
        return result **2       
@Decorator   
def add(a, b):
    return a + b 
print(add(2, 5))
# add = Decorator(add)   
# print(add(1, 2))

class Decorator(object):
    def __init__(self, func):
        self.function = func

    def __call__(self, a, b):
        result = self.function(a, b) 
        return result **2       
# @Decorator   
def add(a, b):
    return a + b 
# print(add(2, 5))
add = Decorator(add)   
print(add(1, 2))

def add(*args):
    sum1 = 60
    for num in args:
        sum1 = sum1 + num
    return sum1   

print(add(10, 20, 30))
print(add(10, 20, 34))

# class Decorator(object):
#     def __init__(self, func):
#         self.function = func

#     def __call__(self, *args):
#         try:
#             if any([isinstance(i, str) for i in args]):
#                 raise TypeError("cannot pass string as argument") 
#             else:
#                 return self.function(*args)
#         expect Exception as obj:
#             return obj
    
# @Decorator
# def add(*args):
#     sum1 = 60
#     for num in args:
#         sum1 = sum1 + num
#     return sum1   

# print(add(10, 20, 30))
# print(add(10, "20", 34))


x = 100

def add(a, b):
    return a + b

print(type(add))

print(callable(x))
print(callable(add))

print(add(10, 20))
print(add.__call__(20, 30))

class Add:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __call__(self, a , b): 
        return a + b
a1 = Add(10,38)
print(Add)   
print(a1.__dict__)   
# print(a1.add())  # Output: 48
print(callable(Add)) 
print(callable(a1))
# a1()  
print(a1(10, 30) ) 

class Employee:
    def __init__(self, first, last):
        self.first = first
        self.last = last
        self.mail = first + last + "gmail.com"

    def fullname(self):
        return f'{self.first} {self.last}'
        
e = Employee("shantanu", "kumar") 
e1 = Employee("rajendra", "jaisawal")
e2 = Employee("aman", "singh") 

e.firstname = "jay"
e1.firstname = "motu"
e2.firstname = "patlu"
print(e.firstname)
print(e.mail)
print(e.fullname())
print("-"*50)
print(e1.firstname)
print(e1.mail)
print(e1.fullname())
print("-"*50)
print(e2.firstname)
print(e2.mail)
print(e2.fullname())
print("-"*50)

class Employee:
    def __init__(self, first, last):
        self.first = first
        self.last = last
        # self.mail = first + last + "gmail.com"
    @property
    def mail(self):
        return f"{self.first} {self.last}@gmail.com"
    @property
    def fullname(self):
        return f'{self.first} {self.last}'
    
    @fullname.setter
    def fullname(self):
        return f"{self.first} {self.last}"
        
e = Employee("shantanu", "kumar") 
e1 = Employee("rajendra", "jaisawal")
e2 = Employee("aman", "singh") 

e.first = "jay"
e1.first = "motu"
e2.first = "patlu"
print(e.first)
print(e.mail)
print(e.fullname())
print("-"*50)
print(e1.first)
print(e1.mail)
print(e1.fullname())
print("-"*50)
print(e2.first)
print(e2.mail)
print(e2.fullname())
print("-"*50)

