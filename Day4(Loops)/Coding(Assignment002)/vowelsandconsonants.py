s="Madhukar"
l=len(s)
s=s.lower()
vowels_count=0
consonants_count=0

for i in range(0,l):

  if s[i]=='a' or s[i]=='e' or s[i]=='i' or s[i]=='o' or s[i]=='u':
    vowels_count=vowels_count+1
  elif s[i]>='a' and s[i]<='z':
    consonants_count=consonants_count+1

print("vowels count :",vowels_count)
print("consonant count :",consonants_count)