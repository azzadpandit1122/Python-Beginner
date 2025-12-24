fruits  = ("apple", "banana", "orange")
for x in fruits:
    print(x)

fruits  = ("apple", "banana", "orange")
for x in fruits:
    if x == "orange":
        break
    print(x)

list = [2,3, 4, 5, 6, 7, 8]
for x in list:
    if x ==5:
        continue
    print(x)

# i = 0
# while i < 6:
#      print(i)
#      if (i == 6):
#          print(i)
#          i += 0

i  = 1
while i < 6:
    i +=1
    if (i ==3):
        break 
    i += 1

# Continue to the next iteration if i is 3:

i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)