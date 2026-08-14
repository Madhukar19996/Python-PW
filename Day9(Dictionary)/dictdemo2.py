d1={}
print(type(d1))

d1={101:"Madhukar",102:"Ayush",103:"Harsh",104:"Nilesh"}
# print(d1)
#
# d2=dict(a=10,b=20,c=30)
# print(d2)
#
# print(d1[101])
# print(d1[102])
# print(d1[103])
# print(d1[104])
#print(d1[100]) #KeyError: 100

# for i in d1:
#     print(i)

"""
101
102
103
104

"""
# for k in d1:
#     print(k,":",d1[k])

d1[101]="Pushkar"

# for k in d1:
#     print(k,":",d1[k])

# del d1[104]
#
# for k in d1:
#     print(k,":",d1[k])
# d1[105]="Nilesh"
# for k in d1:
#     print(k,":",d1[k])

# print(d1.items()) #dict_items([(101, 'Pushkar'), (102, 'Ayush'), (103, 'Harsh'), (104, 'Nilesh')])
# print(d1.keys())
# print(d1.values())

# for i in d1.values():
#     print(i)
# for j in d1.keys():
#     print(j)
# for x in d1.items():
#     print(x)
# for k,v in d1.items():
#     print(k,v)

# print(d1)
# print(max(d1))
# print(min(d1))
# print(sum(d1))
# print((sorted(d1)))

d1.pop(101)

print(d1)

print(d1.popitem())
print(d1)
d1.clear()
print(d1)

#dic comprehension
d3={x:x**2 for x in range(1,6)}
print(d3) #{1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

