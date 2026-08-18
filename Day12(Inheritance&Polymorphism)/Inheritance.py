#Example 1 :

# class A:
#     def m1(self):
#         print("this is m1 method from class A")
#
# class B(A):
#     def m2(self):
#         print("this is m2 method from class B")
#
# bobj=B()
#
# bobj.m1()
# bobj.m2()


#Example 2 : single inheritance

# class A:
#     x,y=10,20
#     def m1(self):
#         print(self.x+self.y)
#
# class B(A):
#     a,b=200,100
#
#     def m2(self):
#         print(self.a-self.b)
#
# bobj=B()
#
# bobj.m1() #30
# bobj.m2() #100


#Example 3 : Multilevel inheritance
#
# class A:
#     x,y=10,20
#     def m1(self):
#         print(self.x+self.y)
#
# class B(A):
#     a,b=200,100
#
#     def m2(self):
#         print(self.a-self.b)
#
# class C(B):
#     i,j=50,150
#
#     def m3(self):
#         print(self.i*self.j)
#
# cobj=C()
# cobj.m1() #30
# cobj.m2() #100
# cobj.m3() #7500


#Example 4 : Heirarchy inheritance

# class A:
#     x,y=10,20
#     def m1(self):
#         print(self.x+self.y)
#
# class B(A):
#     a,b=200,100
#
#     def m2(self):
#         print(self.a-self.b)
#
# class C(A):
#     i,j=50,150
#
#     def m3(self):
#         print(self.i*self.j)
#
# bobj=B()
# bobj.m1() #A
# bobj.m2() #B
#
# cobj=C()
# cobj.m1() #A
# cobj.m3() #C


#Example 5 : Multiple Inheritance

# class A:
#     x,y=10,20
#     def m1(self):
#         print(self.x+self.y)
#
# class B():
#     a,b=200,100
#
#     def m2(self):
#         print(self.a-self.b)
#
# class C(A,B):
#     i,j=50,150
#
#     def m3(self):
#         print(self.i*self.j)
#
# cobj=C()
# cobj.m1() #A
# cobj.m2() #B
# cobj.m3() #C


#Example 6 : calling parent method using child class ( super () )

# class A:
#     def m1(self):
#         print("this is m1 from class A")
#
# class B(A):
#     def m1(self):
#         print("This is m1 from class B")
#         super().m1() #invoke the immediate parent class method
#
# bobj=B()
#
# bobj.m1() #class B m1 method -->This is m1 from class B


#Example 7 : calling parent class variables using child class

# class A:
#     a,b=10,20
#
# class B(A):
#     i,j=100,200
#
#     def m1(self,x,y):
#         print(x+y) #local variables
#         print(self.i + self.j) #B class variables
#         print(self.a+self.b) #A class variables
#
# bobj=B()
# bobj.m1(1000,2000)


#Example 8: overriding variables
#
# class Parent:
#     name="Madhukar"
#
# class Child(Parent):
#     name="Piyush" #Overriding variables
#     def m(self):
#       print(super().name)
#
# cobj=Child()
# print(cobj.name) #Piyush
# cobj.m() #Madhukar


##Example 9: overriding methods








