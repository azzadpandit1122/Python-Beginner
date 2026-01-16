# stack = []
# # class __init__(self):
# #     pass

# #     def isEmpty(self, my_stack):
# #         if len(my_stack) == 0:
# #             return True
# #         else:
# #             return False

# # function for getting stack's top element
# def get_top(my_stack):
#     if isEmpty(my_stack):
#         print("stack is Empty")
#     else:   
#         return my_stack[-1]
    
# # function for push operation
# def push(self, my_stack, ele):
#     my_stack.append(ele)

# # function for pop operation

# def stack_pop(self, my_stack):
#     if isEmpty(my_stack):
#         print("stack is Empty") 
#         print("can't delete")
#     else:
#         deleted_ele = my_stack.pop()
#         print(deleted_ele, "got deleted") 

# # display all element from stack
# def display(self, my_stack):
#     x = len(my_stack)
#     for i in range(x-1, -1, -1):
#         print(my_stack[i])   

# # function for checking length of stack
# def length(my_stack):
#     return len(my_stack)

# push(stack, 30)
# push(stack, 350)
# push(stack, 40)

# display(stack)

# print(length(stack))
# print("latest inserted element", get_top(stack))
# stack_pop(stack)
# display(stack)


# stack = []
# class __init__(self, homepage):
#     self.stack = [homepage]

#     def isEmpty(self):
#         if len(self.stack) == 0:
#             return True
#         else:
#             return False

# # function for getting stack's top element
#     def get_top(self):
#         if self.isEmpty(self, my_stack):
#             print("stack is Empty")
#         else:   
#             return self.stack[-1]
    
# # function for push operation
#     def push(self, my_stack, ele):
#         self.stack.append(ele)

# # function for pop operation

#     def stack_pop(self):
#         if isEmpty(self, stack):
#             print("stack is Empty") 
#             print("can't delete")
#         else:
#             deleted_ele = self.stack.pop()
#             print(deleted_ele, "got deleted") 

# # display all element from stack
#     def display(self):
#         x = len(self.stack)
#         for i in range(x-1, -1, -1):
#             print(self.stack[i])   

# # function for checking length of stack

#     def length(self):
#         return len(self.stack)

# links_stack = stack("Home.html")

# while True:
#     print("-"*40)
#     n = int(input("please enter the choice \n1.visit another link\n2.back\n3.history"))
#     print("-"*40)
#     if n == 1:
#         links = input("Enter a link:")
#         links_stack.push()
#     elif n == 2:
#         links_stack.pop()
#     elif n == 3:
#         links_stack.display()
#     elif n  == 4:
#         links.stack.get_top()
#     elif n == 5:
#         break
#     else:
#         print("Invalid n")

# __len__

# In python, the __len__ method is a special method that is
#  used to define the behavior of the built-in len() function for custom 
# objects. When you implement the __len__ method in a class, you enable instances 
# of that class to respond to len() calls, returning the length or size of the object as
#  defined by your implementation.

class  Bank :
    def __init__(self, balance, aadhar, acc_no, name):
        print("init is running")
        self.bal = balance
        self.aa = aadhar
        self.acc_no = acc_no
        self.name = name

    def __len__(self):
        return len(self.__dict__)
h1 = Bank(5000, 123456789012, 9876543210, "John Doe")
print(len(h1))

print(h1.__dict__)