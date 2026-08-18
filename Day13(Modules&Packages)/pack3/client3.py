import sys
sys.path.append("C:/Python-PW/Day13(Modules&Packages)/pack1")


from emp import Employee

# Import Employee from pack1
myemp=Employee(101,"Piyush",50000)
myemp.displayemp() #output: empid:101 empname:Piyush empsal:50000


# Import Student from pack2
sys.path.append("C:/Python-PW/Day13(Modules&Packages)/pack2")
from student import Student

s = Student(141, 'Aryan', 'A')
s.displaystu()   # Output: stuid:141 stuname:Aryan stusal:A