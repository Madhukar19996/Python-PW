#capititalize() : converts first character into upper case
# s="hello"
# print(s.capitalize()) #Hello


#casefold() and lower():converts  string into the lower case.
# s="HELLO"
# print(s.casefold()) #hello


#upper():converts  string into the upper case.
# s="hello"
# print(s.upper()) #HELLO

# title(): converts the first character of each word to upper case.
# s="welcome to python programming"
# print(s.title()) #Welcome To Python Programming

# swapcase(): swaps cases ,lower cases become upper case and vice versa .
# s="Welcome to Python Programming"
# print(s.swapcase()) #wELCOME TO pYTHON pROGRAMMING


##center() : Returns a centered string
# s="banana"
# print(s.center(10))
#
# print(s.center(10,'*'))

#format() : Formats specified values in a string
# name="Madhuakar"
# print("Hello {}".format(name)) #Hello Madhuakar


#find() : Searches the string  for a specified value and returns the position of where it was found.
s="hello"
# print(s.find("e")) #1
# print(s.find("l")) #2
# print(s.find("x")) #-1

##index() : Searches the string for a specified value and returns the position of where it was found.
#same as find(), but raises a ValueError if the value is not found.

# print(s.index("e"))
# print(s.index("l"))
# print(s.index("x")) #ValueError: substring not found

#count() : Returns the number of times a specified value occurs in a string.
# s="banana"
# print(s.count("a")) #3
# print(s.count("na")) #2


##replace(): Returns a string where a specified value is replaced with a specified value.
# s="Hello world"
# print(s.replace("world","There")) #Hello There
#
# print(s.replace("l","X")) #HeXXo worXd


##isalnum() Return True if all characters in the string are alphanumeric (no punctuation and spaces or no special characters).
# s="ABC123"
# print(s.isalnum()) #True

# s="abc!"
# print(s.isalnum()) #False

##isalpha() Returns True if all characters in the string are in the alphabets.
# s="Hello"
# print(s.isalpha()) #True

# s="123"
# print(s.isalpha()) #False


##isdecimal() Returns True if all the characters are decimal (0-9)
# s="123"
# print(s.isdecimal()) #True
#
# s="123.55"
# print(s.isdecimal()) #False
#
# s="xyz"
# print(s.isdecimal()) #False


##isdigit() Returns True if all the characters are digits, otherwise False.
# s="123"
# print(s.isdigit()) #True
#
# s="xyz"
# print(s.isdigit()) #False
#
# s="123.55"
# print(s.isdecimal()) #False


##isnumeric() Returns True if all the characters are numeric (0-9), otherwise False.
#"-1" and "1.5" are NOT considered numeric values, because all the characters in the string must be numeric.
#and the - and . are not .

# s="123"
# print(s.isnumeric()) #True

# s="123.55"
# print(s.isnumeric()) #False

# s="xyz"
# print(s.isnumeric()) #True

#islower()
#isupper()
# s="madhukar"
# print(s.islower()) #True
# print(s.isupper()) #False
