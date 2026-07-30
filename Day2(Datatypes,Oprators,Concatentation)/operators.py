#Arithmetic operator : +, - , * , / , // , % , **

"""
a=5
b=2

print(a+b) #7
print(a-b) #3
print(a*b) #10
print(a/b) #2.5
print(a//b)#2
print(a%b) #1
print(a**b) #5*5 = 25

"""

# Relational Operators : <, > , >=, <= , ==, !=
# It support any kind of data.
#It always returns boolean value True/False.

"""""
a=5
b=10

print(a>b) #False
print(a<b) #True
print(a==b) #Fasle
print(a!=b) #True


b=5

print(a==b) #True
print(a!=b) #False
print(a<=b) #True
print(a>=b) #True

"""

#Logical operators : and ,or, not  ==> In java it is symbols ( $, || , !)
#It supports any boolean data type
#It always returns boolean value True/False

#a       b       a and b     a or b   not a    not b
#---------------------------------------------------
#True    True      True        True      False    True
#True     False    False       True      False
#False    True     False       True      True
#False    False    False       Fasle     True
'''''
a=True
b=False

print(a and b) #False
print(a or b) #True
print(not a)  #False
print(not b) #True

'''
#Combination of both relation and logical operator

print((1<2)) #T
print((1>2)) #F

print((1<2) and (1>2)) #F
print((1<2) or (1>2)) #T