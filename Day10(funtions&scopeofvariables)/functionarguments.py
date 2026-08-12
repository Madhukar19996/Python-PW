#1. Arbitrary or variable-length arguments
#2. Positional or required arguments
#3. Keyword arguments

# Example 1 : Function with arbitrary arguments
# def sum_fun(*numbers):
#     total=0
#     for i in numbers:
#         total=total+i
#     return total
#
# print(sum_fun(10,20)) #30
# print(sum_fun(10,20,30,40,50)) #150
# print(sum_fun()) #0

# Example 2 : Function with Positional and Keyword arguments

# def myfun(i,j):
#     print(i,j)

#myfun(10,20) #Positional arguments

#myfun(i=10,j=20) #keyword arguments
#myfun(j=10,i=20) ##keyword arguments 20 10

#myfun(10) #TypeError: myfun() missing 1 required positional argument: 'j'


# Example 3 : Default values can be assigned to positional arguments
# def myfun(i=0,j=0):
#     print(i,j)
#
# myfun(100) #100 0
# myfun() #0 0


# Example 4 : Mixing of both the positional and keyword arguments
# def myfun(a,b,c):
#     print(a,b,c)
# #
# # myfun(10,20,30) #positional arguments
# # myfun(a=10,b=20,c=30) #Keyword arguments
# # myfun(c=10,b=20,a=30) #30 20 10 #Keyword arguments
#
# myfun(10,20, c=30) #positional and keyword arguments
#
# myfun(10,b=20,c=30) #10 20 30
# #myfun(10,b=20,30) #SyntaxError: positional argument follows keyword argument
#                    #This is a wrong positional arguments must appear before any keyword arguments.This is a logical error.
#
# myfun(10,30,b=20)   #TypeError: myfun() got multiple values for argument 'b'

#Example 5: Function can return multiple values
# def largest(a,b):
#     if a>b:
#         return a,b
#     else:
#         return b,a
#
# result=largest(10,20) #tuple (20, 10)
# print(result) #(20, 10)33
# print(type(result)) #<class 'tuple'>