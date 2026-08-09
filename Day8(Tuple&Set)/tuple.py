#Creating  a tuple

# mytuple=("apple","banana","cheery")
# print(mytuple) #('apple', 'banana', 'cheery')

#Access tuple elements/values
# mytuple=("apple","banana","cheery")
#
# print(mytuple[1]) #banana
# print(mytuple[-1]) #cheery

##count number of times values is repeated
# mytuple=("apple","banana","cheery","apple","apple")
# print(mytuple.count("apple")) #3


##range of indexes
# mytuple=("apple","banana","cheery","kiwi","melon","mango")
# print(mytuple[2:5]) #('cheery', 'kiwi', 'melon')
# print(mytuple[-4:-1]) #('cheery', 'kiwi', 'melon')

#change the values in a tuple
#by default tuple does not allow you change values bcoz it is immutable
#but there is work around

#tuple --->list--->tuple
# mytuple=("apple","banana","cheery")
# print(id(mytuple)) #2390425731776
# #mytuple[1]="orange" # not possible to change
# #print(mytuple) #TypeError: 'tuple' object does not support item assignment
# mylist=list(mytuple)
# print("after converting into list:",mylist) # ['apple', 'banana', 'cheery']
# mylist[1]="orange"
# print("after changing mylist is:",mylist) #['apple', 'orange', 'cheery']
# mytuple=tuple(mylist)
# print(mytuple) #('apple', 'orange', 'cheery')
# print(id(mytuple)) #2390425930944


## Retrive the data from tuple using looping statements
# mytuple=("apple","banana","cheery")
#
# for i in mytuple:
#     print(i)

##Searching an  item exist or not
#mytuple=("apple","banana","cheery")

# print("cheery" in mytuple) #True
# if "cheery" in mytuple:
#     print("It is existed")
# else:
#     print("It is not existed")

##length -count the number of values in a tuple
# mytuple=("apple","banana","cheery")
# print(len(mytuple)) #3

##Adding new values --> not poosible bcoz tuple is immutable
# mytuple=("apple","banana","cheery")
# mytuple[3]="orange" # Invalid/incorrect can't add  new value : TypeError: 'tuple' object does not support item assignment


##coping the tuple
# mytuple1=("apple","banana","cheery")
# mytuple2=mytuple1
# print(mytuple2) #('apple', 'banana', 'cheery')


##Removing the values from tuple --->not possible bcoz tuple is immutable
# mytuple1=("apple","banana","cheery")
# mytuple1.remove("apple") #incorrect/invalid :AttributeError: 'tuple' object has no attribute 'remove'

##Joining the tuple
# tuple1=("a","b","c")
# tuple2=("10","20","30")
# tuple3=tuple1+tuple2
# print(tuple3) #('a', 'b', 'c', '10', '20', '30')
