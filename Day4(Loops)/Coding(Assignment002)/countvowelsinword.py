s=input("Enter any words")
s=s.lower()
length=len(s)

vowelscount=0
for i in range (0,length):
    if s[i] =='a' or s[i] =='e' or s[i] =='i' or s[i] =='o' or s[i] =='u':
      print(s[i])
      vowelscount+=1
    elif s[i]>='a' and s[i]<='z':
        pass

print("Vowels count in word is ",vowelscount)

