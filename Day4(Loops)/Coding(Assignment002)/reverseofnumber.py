n=int(input("Enter number :"))
orginal_no=n
rev_number=0;

while n!=0:
    rem=n%10
    rev_number=rev_number*10+rem
    n=n//10


if orginal_no==rev_number:
    print("palindrome number",rev_number)
else:
    print("not palindrome no",rev_number)

