n=int(input("Enter your number:"))
first=0
second=1
print("febonacci series :")
for i in range(1,n+1):
    print(first)
    next = first + second
    first=second
    second=next


# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34