n, x = map(int, input().split())

marks = []
for _ in range(x):
    marks.append(list(map(float, input().split())))

    for student in zip*(marks):
        print(sum(student) / x)

#         Sample Input

# 1 4
# x**3 + x**2 + x + 1
# Sample Output

# True

# start, end = map(int, input().split())
# polynomial = input()

# found = True
# for x in range(start, end + 1):
#     if eval(polynomial) == 0:
#         found = False
#         break

# print(found)

# Read input
# n = int(input())
# list_a = list(map(int, input().split()))
# m = int(input())
# list_b = list(map(int, input().split()))

# # Convert lists to sets to find common elements
# common_elements = set(list_a) & set(list_b)

# # Output the number of common elements
# print(len(common_elements))

# 9
# 1 2 3 4 5 6 7 8 9
# 9
# 10 1 2 3 11 21 55 6 8
# Sample Output

# 4

# Read input
# n = int(input())
# list_a = list(map(int, input().split()))
# m = int(input())
# list_b = list(map(int, input().split()))

# count = 0

# for x in list_b:
#     if x in list_a and x < 10:  # Only count if in A and less than 10
#         count += 1

# print(count)

# Read input
# a = int(input())
# b = int(input())
# c = int(input())

# # Compute full power
# full_power = a ** b

# # Compute modulo
# mod_result = full_power % c

# # Print results
# print(full_power)
# print(mod_result)

a = pow(4, 5)
print(a)

b = 4 ** 4
print(b)