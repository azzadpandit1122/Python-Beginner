# # n, x = map(int, input().split())

# # marks = []
# # for _ in range(x):
# #     marks.append(list(map(float, input().split())))

# #     for student in zip*(marks):
# #         print(sum(student) / x)

# #         Sample Input

# # 1 4
# # x**3 + x**2 + x + 1
# # Sample Output

# # True

# # start, end = map(int, input().split())
# # polynomial = input()

# # found = True
# # for x in range(start, end + 1):
# #     if eval(polynomial) == 0:
# #         found = False
# #         break

# # print(found)

# # Read input
# # n = int(input())
# # list_a = list(map(int, input().split()))
# # m = int(input())
# # list_b = list(map(int, input().split()))

# # # Convert lists to sets to find common elements
# # common_elements = set(list_a) & set(list_b)

# # # Output the number of common elements
# # print(len(common_elements))

# # 9
# # 1 2 3 4 5 6 7 8 9
# # 9
# # 10 1 2 3 11 21 55 6 8
# # Sample Output

# # 4

# # Read input
# # n = int(input())
# # list_a = list(map(int, input().split()))
# # m = int(input())
# # list_b = list(map(int, input().split()))

# # count = 0

# # for x in list_b:
# #     if x in list_a and x < 10:  # Only count if in A and less than 10
# #         count += 1

# # print(count)

# # Read input
# # a = int(input())
# # b = int(input())
# # c = int(input())

# # # Compute full power
# # full_power = a ** b

# # # Compute modulo
# # mod_result = full_power % c

# # # Print results
# # print(full_power)
# # print(mod_result)

# a = pow(4, 5)
# print(a)

# b = 4 ** 4
# print(b)

# class Object:
#     pass

# p1 = Object()
# p1.name = "madhav"
# p1.age = 23

# print(p1.name)
# print(p1.age)

# class Object:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def greek(func):
#         print(f"hello i am {func.name} ! currently my age {func.age}")

# p1 = Object("sita", 23)
# p1.greek()

# n = "Hghjg"
# m = "Kfhjg"
# width = 15

# print("*" * width)
# print("H" * width)
# print(n.ljust(width, "*"))
# print(n.rjust(width, "*"))
# print(n.center(width, "*"))

# for i in range(1, 5):
#     print(n.center(width, "*"))

# print(m.rjust(width, "*"))

# for ch in n:
#     print(ch)

# n = "Hghjg"
# b = 10
# for i in range(1, 5):
#     print(n.rjust(b, '-'))

# for i in range(1, len(n) + 1):
#     print(n[:i])

    
# for i in range(len(n) , 0, -1):
#     print(n[:i])

# b = "fgftf"
# print(f"{b: <15}World")    
# print(f"{b: >15}World")    
# print(f"{b: ^15}World")    

# a = "madhav"
# b = 45
# c = 7
# print(f"name: {a: <5} age: {b: >3} frg; {c: >2} ")
# print(f"name: {a: <7} age: {b: >2} gty: {c: <5} ")


# n  = 3
# width = 30
# c = "H"

# # upper part cover
# for i in range(1, n + 1):
#     print((c * (2*i - 1)).center(2*n))

# # mid part
# print(c * width)


# for i in range(1,4):
#     print(c * width)


# for i in range(n-1, -1, -1):
    # print(("H" * (2*i + 1)).ljust(2 + 3*i)) 


# for i in range(3):
#     space = " " * i
#     h_count = 4 - i
#     print(space + "h" * h_count)
    # print(c*n).rjust(n*3) + (c*n)  


# # print()

# # n = 7
# # for i in range(1, n + 1):
# #     print(("*" * (2*i - 1)).center(2*n))
# n = 4
# c = "*"

# for i in range(n):
#     print((c * (i + 1)).center(10))

# for i in range(n-1, -1, -1):
#     print((c * (i + 1)).center(10))

# print("Hello".center(10, '-')) # आउटपुट: --Hello---
# print(f"{'Hello':^10}")      # आउटपुट:   Hello

# # top part
# for i in range(1, 6, 2):
#     print(" " * (5 - i) + "H" * i)

# # middle block
# for _ in range(4):
#     print("H" * 28)

# # bottom part (reverse of top)
# for i in range(5, 0, -2):
#     print(" " * (5 - i) + "H" * i)

# thickness = 4
# c = "h"
# for i in range(thickness):
    # print(c*thickness).rjust(thickness*3) + (c * thickness)


    
  # hhhhhh
  #  hhh
    # h


class Mains():
        def __init__(self):
            self.salary = 23455 
            self.age = 43
e1 = Mains()      
e2 = Mains()
print(e1.__dict__)

class Person():
      def __init_(self, name1, name2):
            self.name1 = name1
            self.name2 = name2

p1 = Person("mike", "osle") 
# p1.name1()
# p1.name2()       
print(p1.name1)
print(p1.name2)


