

while True :
    try:
        n = int(input("Enter a number between 1 to 10:"))
    except ValueError:
        print("That's not a valid number")
        continue
    if 1<=n<=10:
            print("Break the loop")
            break
    else:
        print("Invalid input")