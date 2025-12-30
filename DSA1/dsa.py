# #Define Set
# # in set include a lot of list 

# # set = (56, 67, 7)
# # for x in set:
# #     print(x)


# # demo1 = ["abc", "xyz"] 
# # demo2 = [45, 77, 6]
# # demo3 = ["gf", "gd" , "bfhj"]
# # for y in (demo1 , demo2 , demo3):
# # # set = demo1 + demo2 + demo3
# #     print(y)

# # demo1 = ["abc", "xyz"] 
# # demo2 = [45, 77, 6]
# # demo3 = ["gf", "gd" , "bfhj"]
# # set1 = (demo1, demo2, demo3)
# # for y in (set1):
# #     print(y)


# # demo1 = ["abc", "xyz"] 
# # demo2 = [45, 77, 6]
# # demo3 = ["gf", "gd" , "bfhj"]
# # set1 = (demo1, demo2, demo3)
# # x = set1 * 3
# # print(x)

# demo1 = ["abc", "xyz"] 
# set1 = (demo1)
# for set1 in demo1:
#     x = set1 * 3
#     print(x)

# def my_function(P, T, R):
#   result = P * T * R / 10
#   print(result)

# my_function(20, 20, 20) 

# def my_function(animal = "edgff"):
#   print("gfytrjnifdydcbnhf", animal , "src xn df xgftsgf")
# my_function()

# from functools import reduce

# arr = [25, 25, 25]
# res = reduce(lambda a, b : a * b , arr)
# print("multiply" , res)

# a = 25
# b = 34
# c = 8
# M = a * b *c
# print(M)

# arr = [12, 10, 5, 6, 52, 36]
# k = 2

# x = arr[:k]
# y = arr[k:]
# y.extend(x)
# print(y)

# tyu = [66, 7687, 6, 47, 76]
# tyu.sort()
# print(tyu)

# tu = [28, 576, 87587, 254, 365]
# result = sorted(tu)
# print(result)

# num = 6879798722636776239264
# res = sorted(str(num))
# print(res)

# tyu = [66, 7687, 6, 47, 76]
# tyu.sort(reverse =True)
# print(tyu)

# tu = [28, 576, 87587, 254, 365]
# result = sorted(tu, reverse=True)
# print(result)

# a = [1, 2, 3, 4, 5]

# # Number of positions to rotate
# n = 0

# # Rotate right by 2
# rotated_list = a[-n:] + a[:-n] 
# print(rotated_list)

# from collections import deque
# a = [1, 2, 3, 4, 5]

# d = deque(a)

# # Rotate 2 positions to the left
# d.rotate(0) 

# # Convert back to list if needed
# rotated_list = list(d) 
# print(rotated_list)

# # a = [1,2, 3, 4, 5]
# # n = 2
# # for _ in range(n):
# #    a.insert(0, a.pop())
# #    print(a)

# a = [1, 2, 3, 4, 5]

# d = deque(a)

# # Rotate 2 positions to the right
# d.rotate(2) 

# # Convert back to list if needed
# rotated_list = list(d) 
# print(rotated_list)

# arr = [6, 5, 4, 4]
# n = len(arr)
# incr = all(arr[i] <= arr[i+1] for i in range(n-1))
# decr = all(arr[i] >= arr[i+1] for i in range(n-1))

# print(incr or decr)

# arr = [6, 5, 4, 4]
# incr = all(a <= b for a, b in zip(arr, arr[1:]))
# decr = all(a >= b for a, b in zip(arr, arr[1:]))
# print(incr or decr)


# arr = [6, 5, 4, 4]
# incr = sorted(arr) == arr
# decr = sorted(arr, reverse=True) == arr
# print(incr or decr)

# rr = [6, 5, 4, 4]
# n = len(arr)

# if n <= 2:
#     print(True)
# else:
#     d = arr[1] - arr[0]
#     m = True
#     for i in range(2, n):
#         if d == 0:
#             d = arr[i] - arr[i-1]
#             continue
#         if (d > 0 and arr[i] < arr[i-1]) or (d < 0 and arr[i] > arr[i-1]):
#             m = False
#             break
#     print(m)

# lst = [1, 2, 3, 4, 5]
# lst[0], lst[-1] = lst[-1], lst[0]

# print( lst)

# Take a string from user and reverse it

# original_string = "hello world"
# rev_string = original_string[::-1]
# print(rev_string)


# num = 8
# i = range(2, num)
# for i in range(2, num):
#     if num % i == 0: 
#         print("prime number")

# else:
#     print("non prime number")

# num = int(input("Enter a number :"))
# is_prime = True
 
# if  num <= 1:
#   is_prime = False

# else:
#   for i in range(2, num):
#     if num % 2 == 0:
#       is_prime = True
#       break

#     if is_prime:
#       print("prime number")
#     else:
#       print("non prime number")

a = 68
b = 76
sum = a + b 
print(sum)

if __name__ == '__main__':
    print("__name__")

# dist_1 = 57687
# dist_2 = 25465
# if dist_1 < dist_2:
#     print(enemy_1)
# else:
#     print(enemy_2)

thislist = ["banana", "Orange", "Kiwi", "cherry"]

thislist.reverse()

print(thislist)

# num = {4, 6, 8, 9, 5, 10}
# e = []
# o = []
# for x in num:
#     if x % 2 == 0:
#         e.append(x)
#         o.append(x)
#         print("even numver:" , e)
#     else:
#         print("odd number:" , o)
newlist = [x for x in range(10)]

print(newlist)      

x = 5
print(type(x))

x = 5
x = complex(x)
print(x)

x = 5
x = float(x)
print(x)

x = 5
x = str(x)
print(x)

# mylist = ['apple', 'banana', 'cherry']
# i = 0
# while i < len(mylist):
#  print(mylist[i])
# i = i + 1

num = "aple"
x = num * 3
print(x)

num = "aple ", "bana", "uru"
[print(x) for x in num]

# num = "aple ", "bana", "uru"
# ewlist

import datetime

# x = datetime.datetime.now()

# print(x.strftime("%B"))

x = datetime.datetime(2025, 12, 30)
print(x)

x = datetime.datetime.now()
print(x)

x = datetime.datetime(2028, 12, 2)
print(x.strftime("%y"))


x = datetime.datetime(1540, 11, 3)
print(x.strftime("%y"))

x = datetime.datetime(1540, 11, 3)
print(x.strftime("%c"))

x = datetime.datetime(1540, 11, 3)
print(x.strftime("%C"))

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)

p1 = Person("John", 36)
print(p1)

mytuple = ("apple", "banana", "cherry")
myit = iter(mytuple)

print(next(myit))
print(next(myit))
print(next(myit))
# print(next(myit))

class MyNumbers:
  def __iter__(self):
    self.a = 1
    return self

  def __next__(self):
    x = self.a
    self.a += 1
    return x

myclass = MyNumbers()
myiter = iter(myclass)

print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))

class MyNumbers:
  def __iter__(self):
    self.a = 1
    return self

  def __next__(self):
    if self.a < 20:
      x = self.a
      self.a += 1
      return x
    else:
      raise StopIteration

myclass = MyNumbers()
myiter = iter(myclass)

for x in myiter:
  print(x)


class Table:
  def __iter__(self):
    self.b = 2
    return self

  def __next__(self):
    if self.b <= 20:
      x = self.b
    self.b += 2
    return x 
  else:
  raise StopIteration

# myclass = Table()
# myiter = iter(myclass)

# print(next(myiter))
# print(next(myiter))
# print(next(myiter))


