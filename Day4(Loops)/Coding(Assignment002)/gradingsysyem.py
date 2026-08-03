
marks=int(input("Enter your marks : "))

if 90<=marks  and marks <=100:
    print("Congratulation Excellent  Your grade is : A ")

elif 80<=marks  and marks <90:
    print(" Congratulation Great Your grade is B ")
elif 70<=marks and marks <80:
    print(" Congratulation Good Your grade is C ")
elif 60<=marks and marks <70:
    print(" Congratulation Great Your grade is D")
elif 50<=marks and marks <60:
    print("You need to work hard .Your grade is E")
elif 0<=marks and marks <=50:
    print("You need to work hard .Your grade is F")
else :
    print("You are a super human yours marks is greater than 100")