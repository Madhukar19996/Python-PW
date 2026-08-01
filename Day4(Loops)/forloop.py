#Example 1 :
#print(list(range(1,11)))

#Example 1 : print numbers 1 to 10
# for i in range(1,11):
#     print(i,end=' ') #1 2 3 4 5 6 7 8 9 10

#Example 2 : print even numbers between 1 to 10

#range(2,11,2)
#Method 1 :
# for i in range(2,11,2):
#     print(i,end=' ') #2 4 6 8 10

#Method 2 :
# for i in range(1,11):
#     if i%2==0:
#      print(i,end=' ') #2 4 6 8 10


#Example 3 : print reverse numbers between 10 to 1
#range(10,0,-1)
# for i in range(10,0,-1):
#     print(i,end=" ") #10 9 8 7 6 5 4 3 2 1

#Example 4: Variables scope in python
#Exceptional case : In python loop variables are accessible after the loop ends
# for i in range(1,6):
#     print(i,end=' ') #1 2 3 4 5
#
# print(i)  #5



#Example 5:
# for i in range(1,6):
#     pass
#
# print(i)  #5


