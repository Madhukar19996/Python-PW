s="Sky is a blue"
l=len(s)
a_count=0
b_count=0
for i in range(0,l):
    if s[i]=='a':
        a_count+=1
    elif s[i]=='b':
        b_count+=1
print("a count:",a_count)
print("b count:",b_count)