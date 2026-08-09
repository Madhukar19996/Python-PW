balance=0
while True:
    print("===ATM===")
    print("1.Deposit")
    print("2.Withdraw")
    print("3.Exit")
    print("4.Check Balance")
    n=int(input())
    if n==1:
        print("Enter the amount to be deposit")
        deposit=int(input())
        balance+=deposit
        print("your balance is ",balance)
    elif n==2:
        print("Enter the amount to be withdraw")
        withdraw=int(input())
        balance-=withdraw
        print("your balance is ", balance)
    elif n==3:
        break
    elif n==4:
        print("balance",balance)


