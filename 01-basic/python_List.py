mylist = list(('apple', "name", "age", 2, 7))
print((mylist))


mylist = list(('apple', "name", "age", 2, 7))
print(len((mylist)))



mylist = list(('apple', "name", "age", 2, 7))
print((mylist[-1]))


mylist = list(('apple', "name", "age", 2, 7))
print((mylist[1]))


mylist = list(('apple', "name", "age", 2, 7))
print((mylist[2:4]))


mylist = list(('apple', "name", "age", 2, 7))
print((mylist[:-6]))



mylist = list(('apple', "name", "age", 2, 7))
print((mylist[-3:]))


mylist = list(('apple', "name", "age", 2, 7))
print((mylist[-3:-1]))


mylist = list(('apple', "name", "age", 2, 7))
print((mylist[-3:1]))


mylist = list(('apple', "name", "age", 2, 7))
print((mylist[3:5]))

mylist = list(('apple', "name", "age", 2, 7))
print((mylist[-3:3]))


thislist = ['abcd', "xyz", "pqr", "tfdfs"]
if "xyz" in thislist:
    print("yes")

    mylist = ["appl", "banana", "cherry"]
    mylist[2] = ["black", "water"]
    print(mylist)
                 

    mylist = ["appl", "banana", "cherry", "orange", "kiwi", "mango"]
    mylist[1:5] = ["black", "water"]
    print(mylist)


    mylist = ["appl", "banana", "cherry", "orange", "kiwi", "mango"]
    mylist[1:2] = ["black", "water"]
    print(mylist)


    mylist = ["appl", "banana", "cherry", "orange", "kiwi", "mango"]
    mylist.insert(2, "watermelon")
    print(mylist)


    mylist = ["appl", "banana", "cherry", "orange", "kiwi", "mango"]
    mylist.insert(2, "cucumber")
    print(mylist)


    mylist = ["appl", "banana", "cherry", "orange", "kiwi", "mango"]
    mylist[2] = ["cucumber"]
    print(mylist[3])


    mylist = ["appl", "banana", "cherry", "orange", "kiwi", "mango"]
    mylist.remove("cherry")
    print(mylist)


mylist = ["appl", "banana", "cherry", "orange", "kiwi", "mango"] 
mylist.pop(2)
print(mylist)

thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)


thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist)


thislist = ["apple", "banana", "cherry"]
thislist.pop(-3)
print(thislist)


thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)


thislist = ["apple", "banana", "cherry"]
del thislist[-2]
print(thislist)


# thislist = ["apple", "banana", "cherry"]
# thislist.clear(-2)
# print(thislist)


thislist = ["apple", "banana", "cherry"]
for x in thislist:
    print(x)


thislist = ["name", "age", "pot", "city"]
for x in thislist:
  print(x)


thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
  print(thislist[i])


  x = ["phone", "laptop", "tablet"]
  for y in x:
    print(y)


thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]


# thislist = ["apple", "banana", "cherry"]
# i = 3
# while i < len(thislist):
#    print(thislist[3])
#    i =  i + 1


list1 = ["a", "b", "c"]
list2 = ["d", "e", "f"]
for x in list2:
   list1.append(x)
print(list1)


list = ["abc", "def", "xyz"]
for x in list:
   print(x)


Home = ["house", "home", "room", "quater"]
Home.append("name")
print(Home)

# import numpy as np

# n = int(input())  
# identity_matrix = np.identity(n)
# print(identity_matrix)

# Read input
# n = int(input())
# arr = list(map(int, input().split()))

# # Check if n is in the list
# if n in arr:
#     print(True)
# else:
#     print(False)

# cube = lambda x: x**3

# def fibonacci(n):
#     fib = []
#     a, b = 0, 1
    
#     for _ in range(n):
#         fib.append(a)
#         a, b = b, a + b
#     return fib
    
# if __name__ == '__main__':
#     n = int(input())
#     print(list(map(cube, fibonacci(n))))    

# import re

# def fun(s):
#     return re.match(r'^[a-zA-Z0-9_-]+@hackerrank\.com$' , s)

# def filter_mail(emails):
#     return list(filter(fun, emails))

# if __name__ == '__main__':
#     n = int(input())
#     emails = []
#     for _ in range(n):
#         emails.append(input())

# filtered_emails = filter_mail(emails)
# filtered_emails.sort()
# print(filtered_emails)

# import numpy as np

# n, m = map(int, input().split())
# arr = np.array([list(map(int, input().split())) for _ in range(n)])

# print(np.mean(arr, axis=1))
# print(np.var(arr, axis=0))
# print("{:.11f}".format(np.std(arr)))

# import numpy as np

# n, m = map(int, input().split())
# arr = np.array([list(map(int, input().split())) for _ in range(n)])

# print(np.mean(arr, axis=1))
# print(np.var(arr, axis=0))
# print(round(np.std(arr), 11))

# import numpy as np
# 2
# 1 2
# 3 4
# 1 2
# 3 4
# Sample Output

# [[ 7 10]
#  [15 22]]

# n = int(input())

# A = np.array([list(map(int, input().split())) for _ in range(n)])
# B = np.array([list(map(int, input().split())) for _ in range(n)])

# print(np.dot(A, B))

# import numpy as np

# n = int(input())

# a = np.array([list(map(int, input().split())) for _ in range(n)])
# b = np.array([list(map(int, input().split())) for _ in range(n)])

# print(np.dot(a, b))


# import numpy as np

# # take input, split and convert to int
# shape = tuple(map(int, input().split()))

# # create arrays
# print(np.zeros(shape, dtype=int))
# print(np.ones(shape, dtype=int))

# 3 3 3
# Sample Output 0

# [[[0 0 0]
#   [0 0 0]
#   [0 0 0]]

#  [[0 0 0]
#   [0 0 0]
#   [0 0 0]]

#  [[0 0 0]
#   [0 0 0]
#   [0 0 0]]]
# [[[1 1 1]
#   [1 1 1]
#   [1 1 1]]

#  [[1 1 1]
#   [1 1 1]
#   [1 1 1]]

#  [[1 1 1]
#   [1 1 1]
#   [1 1 1]]]

# import numpy as np

# # ye line alignment ke liye
# np.set_printoptions(sign=' ')

# # input rows aur columns
# n, m = map(int, input().split())

# # create array with 1s on main diagonal
# print(np.eye(n, m))
#   for identity
# [(1  0  1)
#  (0  1  0)
#  (0  0  1)]

# read sets
# M = int(input())
# a = set(map(int, input().split()))

# N = int(input())
# b = set(map(int, input().split()))

# # symmetric difference: elements in a or b but not in both
# diff = sorted(a ^ b)  # a ^ b = symmetric difference

# # print each element in new line
# for x in diff:
#     print(x)
# STDIN Function ----- -------- 
# 4 set a size M = 4 2 4 5 9 a = {2, 4, 5, 9}
# 4 set b size N = 4 2 4 11 12 b = {2, 4, 11, 12}
# Sample Output 
# 5 9 11 12