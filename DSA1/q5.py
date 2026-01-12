class Finance:
    def __init__(self):
        self.revenue = 10000000
        self.number_of_sales = 114

f1 = Finance()
print(f1. __dict__)

class HR:
    def __init__(self):
        self.number_of_emp = 32
        print(f1.revenue)

H1 = HR()
print(H1.__dict__)

class Finance:
    def __init__(self):
        self.revenue = 10000000
        self.number_of_sales = 114

f1 = Finance()
print(f1. __dict__)

class HR:
    def __init__(self):
        self.number_of_emp = 32
        f1.revenue = 1

H1 = HR()
print(H1.__dict__)

class Finance:
    def __init__(self):
        self.__revenue = 10000000             # private data
        self._number_of_sales = 114             # protected data

f1 = Finance()
print(f1. __dict__)

class HR:
    def __init__(self):
        self.number_of_emp = 32
        f1.__revence = 0

H1 = HR()
print(H1.__dict__)

class Finance:
    def __init__(self):
        self.__revenue = 10000000             # private data
        self.__number_of_sales = 114             # protected data

    def display(self):
        print(f'revenue is {self.__revenue}  to this is {self.__number_of_sales}')
        self.__revenue = 200000
        print(f'revenue is {self.__revenue}  to this is {self.__number_of_sales}')

f1 = Finance()
f1.display()
# print(__revenue)

class Finance:
    def __init__(self):
        self.__revenue = 10000000             # private data
        self.__number_of_sales = 114  
        

f1 = Finance()
# print(f1._Finanace__revenue)
print(f1.__dict__)

class Finance:
    def __init__(self):
        self.__revenue = 10000000             # private data
        self.__number_of_sales = 114  
        
    def _display(self):
        print(self.__revenue)

f1 = Finance()
f1._display()


# ploymorphism

# + :- python object

print(10+20)  #30
print("Hello" + "world")  #Helloworld

emp = ["jay", "viru", "ram"]
company = "infosysy"

for i in reversed(company):
    print(i)

print("for list now")
for i in reversed(emp):
    print(i)


class Veh:
    def __init__(self, name, colour, price):
        self.name = name 
        self.colour = colour
        self.price = price 

    def get_details(self):
        print("name is:", self.name)
        print("colour is:", self.colour)
        print("price is:", self.price)

    def max_speed(self):
        print("maximum speed limit is 100")

    def gear(self):
        print("gear change is 6")

class Car(Veh):
    def max_speed(self):
        print("maximum speed limit is 140")

    def gear(self):
        print("gera change is 7")

    def get_details(self):
        print("name is:", self.name)
        print("colour is:", self.colour)
        print("price is:", self.price)    

F1 = Veh("Truck", "red", "12000000")
c1 = Car("JCB", "yellow", 6757657577)
F1.get_details()        
F1.max_speed()        
F1.gear()        
c1.get_details()              
c1.max_speed()              
c1.gear()              


class BMW:
    def fuel_type(self):
        print("Diesel")
        
    def max_speed(self):
        print("max_speed is 200")

class Farrari:
    def fuel_type(self):
        print("Petrol")

    def max_speed(self):
        print("max_speed is speed 180")

def  car_details(obj):
    obj.fuel_type()
    obj.max_speed()

bmw = BMW()
farrari = Farrari()

car_details(bmw)
print("--------")
car_details(farrari)


num = 2345
mun = 23443454
print(num + mun)
print(num.__add__(mun))
print(int.__add__(num, mun))
print(dir(int))


num = "Hello"
mun = "world"
print(num + mun)
print(num.__add__(mun))
print(str.__add__(num, mun))
print(dir(str))


# step1: check datatype of left operated.#str
# step2:  go in that class
# step3: call. __add__()  function

class Book:
    def __init__(self, title, pages):
        self.title = title
        self.pages = pages
        # self.another = another

    def __add__(self, other):      #b1, b2  , b3  
         total = self.pages + other.pages 
         return Book("All book", total)
    
    def __str__(self):
        return str(self.pages)
    
b1 = Book("One little girls", 300)   
b2 = Book("making indian awesome", 300)
b3 = Book("half girlfriend", 400)
b4 = Book("half girlfriend", 400)
print("total number of pages:" ,b1 + b2 + b3 + b4)

class Hotel:
    def __init__(self, name, fare):
        self.name = name
        self.fare = fare

    def __gt__(self, other):
        return self.fare>other.fare

h1 = Hotel("Taj mahal", 20000)   
h2 = Hotel("punchtantra", 10000)

print(h1<h2)

class Hotel:
    def __init__(self, name, fare):
        self.name = name
        self.fare = fare

    def __gt__(self, other):
        return self.fare>other.fare

h1 = Hotel("Taj mahal", 20000)   
h2 = Hotel("punchtantra", 10000)

print(h1>h2)