# if

# Example 1: age>=18 eligible

# age = 15
# if (age >= 18):
#     print("eligible for vote")


# Example 2: Check the amount value after discount
# amount =150
# discount=0
#
# if amount>1000:
#     discount=amount*10/100
#
# print("Actual amount after reducing discount :", amount-discount)

# if else condition
#Example 1 :
# age = 15
# if (age >= 18):
#     print("eligible for vote")
# else:
#     print("not eligible for vote")

#Example 2 :
# num=int(input("Enter your first number :"))
#
# if(num%2==0):
#     print("even no : ",num)
# else:
#     print("odd no : ",num)


#if elif else
# #Example 3:
#
# amount =1500
# print("Actual amount :", amount)
# discount=0
#
# if amount>10000:
#     discount=amount*20/100
#     print("Actual amount after reducing discount :", amount - discount)
#
# elif 5000<amount<10000 :
#     discount=amount*10/100
#     print("Actual amount after reducing discount :", amount - discount)
#
# elif 1000<amount<5000 :
#     discount=amount*5/100
#     print("Actual amount after reducing discount :", amount - discount)
# else :
#     discount=0
#
# print("Payment amount after discount :", amount -discount)

#Example 2 : 1-Sunday  2 -Monday
# week_number=int(input("Enter your number :"))
#
# if week_number==1:
#     print("Sunday")
# elif week_number==2:
#     print("Monday")
# elif week_number==3:
#     print("Tuesday")
# elif week_number==4:
#     print("Wednesday")
# elif week_number==5:
#     print("Thursday")
# elif week_number==6:
#     print("Friday")
# elif week_number==7:
#     print("Saturday")
# else :
#     print("invalid week number ",week_number)




# nested if else statements
#Example
#num-->2,3
#num -->2 but 3
#num --> 3 but 2
#num --> not 2 not 3

# num=0
# if num%2==0:
#     if num%3==0:
#         print("Divisible by both 2 and 3 ")
#     else:
#         print("Divisible by 2 but not by 3 ")
# else:
#     if num%3==0 :
#         print("Divisible by 3 but not by 2 ")
#     else:
#         print("not divisible by both 2 and 3")


# Short hand if

# a,b=100,20
#
# if a>b:
#     print("a is greater")
#
# if a>b : print("a is greater")

##Short hand if else (ternary operator)
# a,b=20,10
# if a>b:
#    print("a is greater")
# else:
#     print("b is greater")
#
# print("a is greater") if a>b else print("b is greater") ===> ternary operator













#And (Logical operator) with if elif else
#========================================

# num1=int(input("Enter your first number"))
# num2=int(input("Enter your second number"))
# num3=int(input("Enter your third number"))
#
# if num1>num2 and num1>num3:
#     print(" first number is greater ",num1)
# elif num2 >num1 and num2 >num3 :
#     print(" second number is greater ",num2)
# else:
#     print('third number is greater ',num3)



#pass
# a=100
# b=50
#
# if a>b:
#     pass
#
# print("Something")


















