#Creating set

# myset1={10,20,30,40,50}
# myset2={"apple","banana","cheery"}
# myset3={100,'A',True,"welcome"}
#
# print(myset1) #{50, 20, 40, 10, 30}
# print(myset2) #{'banana', 'apple', 'cheery'}
# print(myset3) #{True, 'A', 100, 'welcome'}

##creating empty set
# myset=set() #empty set
# print(myset) #set()

##Acccess the items/values from the set

#you can't access items in a set by referring to an index(bcoz set does not support index).
#you can't even change items in a set .but you can add new items to set .(bcoz set does not support index)


#Access data from set using for loop

# myset1={10,20,30,40,50}
# for i in myset1:
#     print(i)

#check if the value is exist(searching item/value in the set)
# myset1={10,20,30,40,50}
#
# print(10 in myset1) #True
# print(20 in myset1) #True

# if 50 in myset1:
#     print("existed")
# else:
#     print("not existed")

##find length/number of values in a set.
# myset1={10,20,30,40,50}
# print(len(myset1)) #5

#count number of times value is repeated in the set.
#Not possible,since set not allowed duplicates

##Sorting the set is possible in the set.
#Not is possible ,since set is unordered

#Reversing set items
#Not is possible ,since set is unordered.



##Add items/value into set
#add() -we can single value
#update() -we can multiple values
#Not possible insertion since set is unordered and not supported index.

# myset={10,20,30,40,50}
# # myset.add(60)
# # print("After adding:",myset) #After adding: {50, 20, 40, 10, 60, 30}
# # myset.update([70,80,90])
# print("After updation:",myset) #After adding: {70, 10, 80, 20, 90, 30, 40, 50, 60}

#If you have duplicates in a set will ignore.
# myset={10,20,30,40,50,10}
# print(myset) #myset={10,20,30,40,50} Duplicate values are ignored

##Removing values/items from set

#Approach 1 : using remove()
# myset={10,20,30,40,50}
#
# myset.remove(10)
#myset.remove(10) KeyError: if the value is not exist into the set
#after removing: {50, 20, 40, 30}


#Approach 3 : using discard()
# myset={10,20,30,40,50}
#
# myset.discard(10)
# myset.discard(60) #will not throw any error if the value is not existed .
# print("after discarding:",myset) #after discarding: {50, 20, 40, 30}

#Approach 3 : using pop()-->removes a random items/values from the set.
# myset={10,20,30,40,50}
# myset.pop()
# print("after removing:",myset) #myset={10,20,30,40,50}
# myset.pop()
# print("after removing:",myset) #after removing: {40, 10, 30}

#Approach 4 : using clear()-->removes a all items/values from the set.
# myset={10,20,30,40,50}
# myset.clear()
# print("after clearing:",myset) #set()

#detele set
# del myset
# print("After deletion",myset) #NameError: name 'myset' is not defined

#coping set
#Approach 1: copy()
# myset1={10,20,30,40,50}
# myset2=myset1.copy()
#print(myset1)
# print(myset2) #{50, 20, 40, 10, 30}

# myset1={10,20,30,40,50}
# myset2=myset1
# print(myset1) #{50, 20, 40, 10, 30}
# print(myset2) #{50, 20, 40, 10, 30}

#Approach 2: set()
# myset1={10,20,30,40,50}
# myset2=set(myset1)
# print(myset1) #{50, 20, 40, 10, 30}


##joining of sets
#Approach 1:  using union()
# myset1={'a','b','c'}
# myset2={10,20,30}
# myset3=myset1.union(myset2)
# print(myset3) #{'b', 20, 'a', 'c', 10, 30}


#Approach 2:  using | symbol
# myset1={'a','b','c'}
# myset2={10,20,30}
# myset3=myset1 |(myset2)
# print(myset3) #{'b', 20, 'c', 10, 'a', 30}


##retreiving common values from set
#Approach 1 : using intersection()
# myset1={'a','b','c',10}
# myset2={10,20,30,'b'}
# myset3=myset1.intersection(myset2)
# print(myset3) #{10, 'b'}

#Approach 2 : using & symbol
# myset1={'a','b','c',10}
# myset2={10,20,30,'b'}
# myset3=myset1 &(myset2)
# print(myset3) #{10, 'b'}
