# # n = int(input())
# # if n > 0:
# #     for i in range(0, n):
# #         result_sqrt = i * i
# #         print(result_sqrt)

# # n = int(input())
# # num = n       
# # for i in range(1, n):
# #     num += 1
# #     break
# # num = n 
# # print(num) 

# # n = int(input())
# # for i in  range(1, n + 1):
# #     print(i, end="")

# s = 'maa'
# b = 7

# print(s.ljust(b, '*'))
# print(s.rjust(b, '*'))
# print(s.center(b, '*'))
# print(s.ljust(b, '-'))
# print(s.ljust(b))
# print(s.rjust(b))
# print(s.center(b))

# for i in range(1, 5):
#     print(s.center(b))
# for i in range(1, 5):
#     print(s.rjust(b))
# for i in range(1, 5):
#     print(s.ljust(b, '-'))

# s = "hello"
# for ch in s:
#     print(ch)

# s = "HELLO"
# for i in range(1, len(s)+1):
#     print(s[:i])

# # s = "HELLO"
# # for i in range(1, len(s)+1):
# #     print(s[i:])

# s = "HELLO" 
# for i in range(len(s), 0, -1):
#     print(s[:i])   

# s = "HELLO" 
# for i in range(len(s), 0, 1):
#     print(s[:1])   

# s = "HELLO" 
# for i in range(len(s), 0, -2):
#     print(s[:i])   

# # name = "hfcwd"
# # marks = 77
# # print(name.ljust(10), marks.rjust(20))

# name = "gfj"
# b = 10
# print(name.ljust(b, '-'))

# name = "iufowe"
# n =15
# print(name.rjust(n, "-"))


# k = "kjhcc"
# v = 45
# for i in range(1, len(k)):
#     print(k[:i])

# k = "kjhcc"
# v = 45
# for i in range(len(s), 0, -1):
#     print(k[:i])

# name = "Shalu"
# marks = "85"

# print(name.ljust(10), marks.rjust(5))

# name = "Shalu"
# marks = 34

# print("*" * marks)
# print(name.center(marks))
# print("*" * marks)

# text = "WELCOME"
# width = 30

# print("*" * width)
# print(text.center(width, "-"))
# print("*" * width)

# h = "kmsp"
# j = "muskan"

# width = 54
# print("=" * width)
# print(h.center(width))
# print(j.center(width))
# print("=" * width)

n = 7
for i in range(1, n + 1):
    print(("*" * (2*i - 1)).center(2*n))

# n = 5
# for i in range(1, n + 1):
#     print(("*" * (2*i - 1)).center(2*n))

# m = 10
# for i in range(1, m + 1):
#     print(("=" * (3*i - 1)).center(3*m))

# m = 10
# for i in range(1, m - 1):
#     print(("=" * (3*i - 1)).center(3*m))

# width = 30

# print("-" * width)
# print("MENU".center(width))
# print("-" * width)
# print("1. Home".ljust(width))
# print("2. About".ljust(width))
# print("3. Contact".ljust(width))
# print("-" * width)


# n = "Home"
# m = "About"
# p = "Contact"

# width = 20
# print("-" * width)
# print("1.Menu".center(width))
# print("-" * width)
# print("2.Home".ljust(width))
# print("3.About".ljust(width))
# print("4.Contact".ljust(width))
# print("-" * width)


# thickness = 3
# c = 'H'

# for i in range(thickness):
#     print((c*thickness).ljust(thickness*2) + (c*thickness))

# thickness = 4
# p = "T"
# for i in range(thickness):
#     print((p*thickness).ljust(thickness*3) + (p*thickness))

# thickness = 4
# L = "h"    

# for i in range(len(L), 0, -1):
#     print(L[:i])

# for i in range(thickness):
#     print((L*thickness).center(thickness*3) + (thickness*L))

# # n = int(input())
# # for i in range(1, n + 1):
# #     print(i, end="")    


# # n = 1
# # m = 1
# # p = 1
# # x = 2

# # result = [[n , m , p]
# #      for i in range(n + 1)
# #      for j in range(m + 1)
# #      for k in range(p + 1)
# #      if  i + j + k != x ]
  
# # print(result)

# # n = 0
# # m = 3
# # p = 2
# # x = 5

# # result = [[i, j, k]
# #      for i in range(n + 1)
# #      for j in range(m + 1)
# #      for k in range(p + 1)
# #      if  i + j + k != x ]
  
# # print(result)

# n = 0
# m = 3
# p = 2
# x = 5

# result = [[i, j, k]
#      for i in range(n + 1)
#      for j in range(m + 1)
#      for k in range(p + 1)
#      if  i + j + k != x ]
  
# print(result)

# x = 2
# y = 2
# z = 2
# n = 2

# result = [[i, j, k]
#           for i in range(x + 1)
#           for j in range(y + 1)
#           for k in range(z + 1)
#             if i + j + k != n]
# print(result)

# t = (3, 4)
# print(hash(t))

# d = {(1,2): "ok"}
# print(d[(1,2)])

# f = {(3, 2): "hcxgdx"}
# print(f[(3, 2)])

# y = 1, 2
# print(hash(y))

# # if __name__ == '__main__':
# #     students = []

# #     for _ in range(4):
# #         name = "harry", "barry", "tina", "Akriti"
# #         score = 37.21, 37.21, 37, 2, 41
# #         students.append([name, score])

# #     grades = [student[1] for student in students]
# #     lowest = min(grades)
# #     second_lowest = min(g for g in grades if g != lowest)

# #     names = [student[0] for student in students if student[1] == second_lowest]
# #     names.sort()

# #     for name in names:
# #         print(name)

# students = [
#     ['Harry', 37.21],
#     ['Berry', 37.21],
#     ['Tina', 37.2],
#     ['Akriti', 41],
#     ['Harsh', 39]
# ]

# grades = [student[1] for student in students]
# lowest = min(grades)
# second_lowest = min(g for g in grades if g != lowest)

# names = [student[0] for student in students if student[1] == second_lowest]
# names.sort()

# for name in names:
#     print(name)

# students = [
#     ["tina" , 30],
#     ["sp" , 30], 
#     ["rp" , 44], 
#     ["re" , 23]
# ]    

# grades = [student[1] for student in students]

# lowest = min(grades)
# second_lowest = min(g for g in grades if g != lowest)

# names = [student[0] for student in students if student[1] == second_lowest]
# names.sort()
# for name in names:
#     print(name)

# students = [
#     ["tina" , 30],
#     ["sp" , 35], 
#     ["rp" , 44], 
#     ["re" , 23]
# ]  

# students_sort = sorted(students, key=lambda x: (x[1], x[0]))
# print(students_sort)

# students = [
#     ["tina" , 30],
#     ["sp" , 30], 
#     ["rp" , 44], 
#     ["re" , 23]
# ]    

# students_sort_desc = sorted(students, key=lambda x: (x[1], x[0]), reverse=True)
# print(students_sort_desc)

# # class Student:
# #     def __init___(self, name, grade):
# #         self.name = name
# #         self.grade = grade 

# #     def details(self):
# #         print(f"{self.name} is in class {self.grade}")

# # student1 = Student("madhav", 10)
# # print(student1.name, student1.grade) 
# # p1 = Student("madhav", 10)
# # p1.details()

# x = 2
# y = 4
# z = 9
# print(z / y / x)

# var = "james" * 2 * 3
# print(var)

# b = 4
# print(b * 2)

# n = 5 
# print(n ** 2)

# my_string = "Hello"
# print(my_string[0])

# data = ([1, 2], [3, 4])
# data[0].append(5)
# print(data)

# my_list = [1, 2, 3, 4, 5]
# new_list = [x * 2 for x in my_list if x % 2 == 1]
# print(new_list)

# data = {"name": "John", "age": 30}
# print(data.get("city", "Unknown"))

# for num in range(2,-5,-1):
#     print(num, end=", ")

#     # x = 75
# # def myfunc():
# #     x = x + 1
# #     print(x)

# # myfunc(75)
# # print(x)

# sentence = "Joy Joy Joy"
# sentence.replace("Joy", "Bliss", 2)
# print(sentence)

student = { 
  "name": "Emma", 
  "class": 9, 
  "marks": 75 
}

del student["marks"]
print(student)

student.pop("class")
print(student)

x = 0
a = 5
b = 5
if a > 0:
    if b < 0: 
        x = x + 5 
    elif a > 5:
        x = x + 4
    else:
        x = x + 3
else:
    x = x + 2
print(x)


