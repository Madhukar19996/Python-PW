#Concatentation +
#Case 1 : When we use + between 2 numeric values , it will perform addition.
print(10+10) #20 valid
print(10.2 +2.5) #12.7 valid
print(10+3.5)  #13.5 valid

#Case 2 : When we use + between 2 strings , it will perform concatentation.
print("Welcome"+" Python") #Welcome Python

#Case 3 : When we use + between 2 boolean values , it will perform addition.
print(True+5) #6  True=1   False=0
print(False+5) #5
print(True+True) #2
print(False+False)#0

#Case 4 : When we use + between 1 numeric value and String , It is not valid because 2 values are diffrent
'''
print(10+"Welcome") #TypeError: unsupported operand type(s) for +: 'int' and 'str'.

#Note=In java this case is possible
                   
print(12.3+"Madhukar")  #It is not valid because 2 values are diffrent
print(True + "Madhukar")  #It is not valid because 2 values are diffrent

'''
