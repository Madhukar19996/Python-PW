#Creating a class along with object

# class Myclass:
#     def myfun(self):
#         pass
#
#     def display(self,name):
#         print(name)



# mc1=Myclass()
# mc1.myfun()
# mc1.display("Madhukar")
#
#
# mc2=Myclass()
# mc2.myfun()
# mc2.display("Pushkar")


#Example 2 : Instance method vs static method
#Note : 'self' inside the static method is just a parameter name it does not refer to object.
# class Myclass:
#     def m1(self):
#         print("this is instance method ...")
#
#     @staticmethod
#     def m2(self,num): ##==> 'self' inside the static method is just a parameter name it does not refer to object.
#         print(self,num)
# #
# # mc=Myclass()
# #
# # mc.m1() #instance method
# # mc.m2(10,20) #static method
#
# Myclass.m2(10,20) #static method s can be access directly from the class .

# #Example 3 : define  the variable inside the class (class variables / instance variables)
#
# class Myclass:
#     a,b=10,20 #class variables
#
#     def add(self):
#         print(self.a+self.b)
#     def mul(self):
#         print(self.a*self.b)
#
# mc=Myclass()
# mc.add() #30
# mc.mul() #200

#Example 4 : Local variables ,Global variables & class variables .

# i,j=15,25 #global variables
# class Myclass:
#     a,b=10,20 #class variables
#
#     def add(self,x,y):
#         print(x+y) #local variables   -->300
#         print(self.a+self.b)#class variables -->30
#         print(i+j) #global variables -->40
#
#
# mc=Myclass()
# mc.add(100,200)
'''
output :

300
30
40

'''

#Example 5 : Local variables ,Global variables & class variables (names of variables are same) .

# a,b=15,25 #global variables
# class Myclass:
#     a,b=10,20 #class variables
#
#     def add(self,a,b):
#         print(a+b) #local variables   -->300
#         print(self.a+self.b)#class variables -->30
#         print(globals()['a']+globals()['b']) #global variables -->40
#
#
# mc=Myclass()
# mc.add(100,200)

#Example 6 : Class with constructor
#--init__(self) : constructor

#constructor used for initialize data
# constructor invoked automatically when object is created

# class Myclass:
#     def __init__(self):
#         print("This is constructor...")
#     def m1(self):
#         print("Hello...")
#     def m2(self,x,y):
#         return x+y
#
# mc=Myclass()
# mc.m1()
# print(mc.m2(10,20))

#Example 7: constructor with parameters and class variable

# class Myclass:
#     name="Madhukar" #class variable
#
#     def __init__(self,name):
#         print(name) #Pushkar
#         print(self.name) #Madhukar
#
# mc=Myclass("Pushkar")


#Example 8: Aclass with constructor and method

# class Emp:
#     def __init__(self,eid,ename,sal):
#         self.eid=eid
#         self.ename=ename
#         self.sal=sal
#
#     def dispaly(self):
#         print(self.eid,self.ename,self.sal)
#
#
# e1=Emp(101,"Nikhil","30000")
# e1.dispaly()
#
# e2=Emp(102,"Avishek","35000")
# e2.dispaly()


