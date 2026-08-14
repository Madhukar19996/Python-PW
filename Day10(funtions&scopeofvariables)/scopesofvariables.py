#Global & Local variables
#The variables create outside of the functions are called as Global variables.
#The variables create inside of the functions called as Local variables.


#Example 1 :
# x=20 #global variables
#
# def myfun():
#     y=10 #local variable
#     # print(x)#able to access global variable within the function
#     # print(y)
#
# myfun()
# print(x)
#print(y) #NameError: name 'y' is not defined --> can't access local variable in outside of the function.

#Example 2 :
# x=100 #global variable
#
# def myfun():
#     x=200 #local variable
#     print(x) ##200
#
# myfun()
# print(x) #100


#Example 3 :


# x=100 #global variable
#
#
# def myfun():
#     global x
#     x=200
#     print(x) #200
#
#
# myfun()
# print(x) #200


#Example 4:Declare the Global variable inside the function

def myfun():
    #global x=100 #syntax error --not valid
    global x
    x=100
    print(x)

myfun()
print(x)






