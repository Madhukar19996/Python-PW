#Creating string in 3 approaches

#Approach 1: using double quotes
#name="Madhukar"
#grade="A"


#Approach 2: using single quotes
#name='Piyush'
#grade='B'

#Approach 3: using constructor
# name=str()  #--> empty string
# grade=str() # --> empty string
#
# name=str('Madhukar')
# grade=str('B')
# print(name,grade)
#
# print(type(name))
# print(type(grade))

## + and * operators with strings
# s="Welcome"
# print(s+" Programming")
#
# print(s *3)


##slicing strings
#starting index count from 0
#ending index count from 1


s="welcome"
# print(s[1:3]) #el
#
# print(s[:6])  #here starting index is 0 by default-->welcom
#
# print(s[2:]) #lcome --> here ending index is last value
#
# print(s[1:-1]) #elcom
# print(s[1:-2]) #elco
#
#
# print(s[-5:-2]) #lco
#

##formating string
#F-string was introduced in python 3.6,and is now the preferred way of formating strings.
#To specify a string as an f-string.
#simply put an f in front of the string literal, and add curly brackets {} as placeholders for variables and other operations.

#Example 1
# age=27
# #str="My name is Madhukar, I'm "+age
# #print(str) #TypeError: can only concatenate str (not "int") to str
# str=f"My name is Madhukar, I'm {age}"
# print(str)
# print(f"My name is Madhukar, I'm {age}")


#Example 2 : output : The price is 50.00
# price=50
# s=f"The price is {price:.2f} "
# print(s)
#

#Example 3 :output :The price is 200 dollars

# price=20
# s=f"The price is {price*10} dollars"
# print(s)

#Example 4 :
# in notin with strings
#return the boolean values

s="Madhukar"

# print("kar"in s) #True
# print("Madu" in s ) #False


print("kar"not in s) #False
print("Madu" not in s ) #True









