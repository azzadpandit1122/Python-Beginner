a = 6
b = 7
print(a + b)

# a = int(input("Enter a number:"))
# b = int(input("Enter a number:"))

# print(a + b)

def myfunction():
    return (a , b)
a = 10
b = 49

print(a + b)

x = lambda a ,b : a + b
print(x(10, 6))

x = lambda a ,b : a + b
print(x(10,897857))

print(sum([10,87576]))


import operator
print(operator.add(10, 6))

print(operator.add(10, 5))

import math
n = 7
print(math.factorial(n))

n = 3
print(math.factorial(n))

import math as np
n = 4
print(np.prod(range(1, n + 1)))

from functools import reduce

arr = [56, 67, 6578, 59]
ans = reduce(lambda a, b : a + b, arr)
print("sum" , ans)


list = [566, 64, 8328, 9865, 665]
ans = max(list)
print(ans)

list = [566, 64, 8328, 9865, 665]
ans = min(list)
print(ans)