# name="john"
# age=30
# sal=50000.50

name ,age ,sal="Madhukar",26,40000

#Approach 1 :
#print(name,age,sal)

#Approach 2 :
#
# Name is :Madhukar
# Age is :26
# Salary is :40000

#print("Name is "+name) #valid because variable value is also string we can concatenation with same type .
#print("Age is "+age) # Not valid ==> TypeError: can only concatenate str (not "int") to str.

# print("Name is ",name)
# print("Age is ",age)
# print("Salary is ",sal)

#Approach 3 :
#%s -->string     %d-->int       %g-->decimal

# print("Name:%s  Age :%d  Salary:%d "%(name,age,sal))
# print("Age:%d  Name:%s  Salary:%d "%(age,name,sal))

#Approach 4 : {} format()
# print("Name:{} Age:{}  Salary:{}".format(name,age,sal))

#Approach 5 :{} format()

# print("Name:{0} Age:{1}  Salary:{2}".format(name,age,sal))
# print("Salary:{2} Age:{1}  Name:{0} ".format(name,age,sal))



# print("welcome to \n python") #printing the data in next line
print("welcome\tto python") #providing the tab space