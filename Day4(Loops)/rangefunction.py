#range(num) --> If you single number that will be considered as stopping point .In this case 0 is starting point.
#range(start,stop)
#range(start,stop,step(inc/dec)


#Example 1: range(num) --> If you single number that will be considered as stopping point .In this case 0 is starting point.
#print(range(10)) #range(0, 10)

#Only stopping value
# print(list(range(10))) #[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(list(range(0,10))) #[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
#print(list(range(10)))  print(list(range(0,10))) Both are same .


#Example 2 : start & stop values
# print(list(range(5,10))) #[5, 6, 7, 8, 9]


#Example 3 :print even numbers between 1 to 10
# #range(start,stop,step(inc/dec)
# print(list(range(0,11,2))) #[0, 2, 4, 6, 8, 10]

#Example 4 :print odd numbers between 1 to 10
#print(list(range(1,10,2))) #[1, 3, 5, 7, 9]

#Example 5 : print reverse numbers from 10 to 1
#print(list(range(10,0,-1))) #[10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

#Example 6: -10,-9,-8,-7,-6,-5,-4,-3,-2,-1,0,1,2,3,4,5,6
#print(list(range(-10,-5))) #[-10,-9,-8,-7,-6]
#output:[-10, -9, -8, -7, -6]

#Example 7 :
# print(list(range(-10,-5,2))) #[-10,-8,-6]
#output :[-10, -8, -6]

#Example 8 :
print(list(range(-10,-5,-2)))