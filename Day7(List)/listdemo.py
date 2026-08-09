# #Creating list
# mylist1=[10,30,40,50,60]
# mylist2=["apple","mango","banana","grapes"]
# mylist3=[1,20.50,"Ram",'A',True]
#
# print(mylist1) #[10, 30, 40, 50, 60]
# print(mylist2) #['apple', 'mango', 'banana', 'grapes']
# print(mylist3) #[1, 20.5, 'Ram', 'A', True]
#
# mylist4=list() #This will create empty list
# print(mylist4) #[]

#Access items/value/objects from the list
# mylist=["apple","banana","cheery"] #index starts from 0
#
# print(mylist[0]) #apple
# print(mylist[2]) #cheery
#
# print(mylist[-1]) #cheery
# print(mylist[-2]) #banana


##Access multiple values from a list (range of indexes)
# mylist=["apple","banana","orange","cheery","kiwi","mango","melon"]
#print(mylist[2:5]) #['orange', 'cheery', 'kiwi']
# print(mylist[-4:-1]) #['cheery', 'kiwi', 'mango']

#Change the item value in list
# mylist=["apple","banana","cherry"]
# print("Before the change",mylist) #Before the change ['apple', 'banana', 'cherry']
# mylist[0]="orange"
# print("After the change",mylist) #After the change ['orange', 'banana', 'cherry']

##loop with list
# mylist=["apple","banana","cherry"]
# for i in mylist:
#     print(i,end=' ')

##check if the item is exist or not (searching in a item in a list)

# mylist=["apple","banana","cherry"]
#
# if "banana" in mylist:
#     print("Yes banana is exist")
# else:
#     print("No, banana is not exist")

## find out length/size of a list

# mylist=["apple","banana","cherry"]
#
# print(len(mylist)) #3
#
#
# str="Madhukar"
# print(len(str)) #8

#count number of times is repeated in the list
# mylist=["apple","banana","cherry","apple","apple"]
# print(mylist.count("apple")) #3

##sorting  the list
# mylist=["mango","banana","cherry","apple"]
#
# print("orginal list: ",mylist)

#mylist.sort() #sort the elements ascending order ['apple', 'banana', 'cherry', 'mango']
# mylist.sort(reverse=True) #sort the elements in descending order ['mango', 'cherry', 'banana', 'apple']
#
# print("sorted values:",mylist)




# Reverse list items
#pre-requisite : values must be in sorted order

# mylist=["apple","banana","cheery","mango"] #ascending order
# print("orginal values :",mylist)
# mylist.reverse()
# print("reversed values in a list",mylist)


## Add item append() insert()
#mylist=["apple","banana","cheery"]
# print("Before append",mylist) #Before append ['apple', 'banana', 'cheery']
#
# mylist.append("orange")
# print("after append",mylist) #after append ['apple', 'banana', 'cheery', 'orange']

# print("before insertion",mylist) #before insertion ['apple', 'banana', 'cheery']
# mylist.insert(1,"grapes")
# print("after insertion",mylist) #after insertion ['apple', 'grapes', 'banana', 'cheery']


#Remove items from list
#remove()
# Approach 1: remove() -->accepts value
# mylist=["apple","banana","cheery"]
# mylist.remove("banana")
# print("after removing",mylist) #after removing ['apple', 'cheery']

# Approach 2: pop() --> index
# mylist=["apple","banana","cheery"]
# mylist.pop(2)
# print("after removing",mylist) #after removing ['apple', 'banana']

# Approach 3: del
# mylist=["apple","banana","cheery"]
# del mylist[1] #we passed index of the element,here del is not a method, it is a identifier/keyword.
# print(mylist) #['apple', 'cheery']

##delete the list
#del
# del mylist
# print(mylist) #NameError: name 'mylist' is not defined. Did you mean: 'list'?



#coping the list

#Approach 1 :copy()
# mylist1=["apple","banana","cheery"]
# mylist2=mylist1.copy()
# print(mylist1) #['apple', 'banana', 'cheery']
# print(mylist2) #['apple', 'banana', 'cheery']

#Approach 2 :list()
# mylist1=["apple","banana","cheery"]
# mylist2=list(mylist1)
# print(mylist1)
# print(mylist2)



#Join the lists
#Approach 1 : using +
# mylist1=[1,2,3]
# mylist2=["a","b","c"]
# mylist3=mylist1+mylist2
# print(mylist3) #[1, 2, 3, 'a', 'b', 'c']


##Approach 2 :using for loop
mylist1=[1,2,3]
mylist2=["a","b","c"]
mylist3=list()

# for i in mylist2:
#     mylist1.append(i)
# print(mylist1)    #[1, 2, 3, 'a', 'b', 'c']

#case 1:
# for i in mylist1:
#     mylist3.append(i)
# print(mylist3)

#case 2:
# for i in mylist1:
#     mylist3.append(i)
#
# for i in mylist2:
#     mylist3.append(i)
#
# print(mylist3) #[1, 2, 3, 'a', 'b', 'c']

##Approach 3 :using extend() method
# mylist1=[1,2,3]
# mylist2=["a","b","c"]
# mylist1.extend(mylist2)
# print(mylist1) #[1, 2, 3, 'a', 'b', 'c']








