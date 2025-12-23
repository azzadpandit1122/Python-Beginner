# num1 = int(input("enter a number: "))
# height = float(input("enter a number: "))
# base = float(input("enter a number: "))
# area = (1/2)*base*height
# print("the rea of the triangle", area)

# x = 23
# y = 24
# tem = x 
# print(x)
# x = y 
# print(x)
# print(y)

# y = tem
# print(y)

# other method 
x =  39
y = 30
x , y = y , x
print(x)
print(y) 

# x  = int(input("enter a number: "))


# if x % 2 == 0:
#     print("even")
# else: 
#     print("odd")

num1 = 13
num2  = 34
num3 = 35
if num1 > num2 and num1 > num3:
    print( num1, "lowest")

elif num2 > num3 and num1 > num2:
    print(num2, "lowest")

else:
    print(num3 , "highest")

import random

num = random.randint(0, 10)
print(num)



# num = int(input("enter a number: "))
# fact = 1
# if num < 0:
#     print('factorial 0f 0 does not exist')   
# if num == 0:
#     print("factorial 0f 0 is", 1)
#     if num > 0:
#         for i in range(1, num+1):
#             fact = fact*1
#             print("the factorial of the given number is", fact)


Home = ["house", "home", "room", "quater"]
Home.append("name")
print("Home")