# File handlimg

# mode : r - read, w - write, a - append:
#open file

file = open("txt.py", "r")

#read file
file = open("txt.py", "r")
content = file.read()           # read entire data
print(content)
file.close()

file = open("txt.py", "r")
content = file.readline()           # read data first line
print(content)
file.close()

file = open("txt.py", "r")
content = file.readlines()           # read data in list form
print(content)
file.close()

# write a file

file = open("example2.py", "w")
file.write("Natmste, chjgada")
file.close()

file = open("example2.py", "a")
file.write("\njhdfejf")
file.close()