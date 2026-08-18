class Student:
    def __init__(self, name, age, roll_no):
        self.name = name
        self.age = age
        self.roll_no =roll_no
    def display_details(self):
        print(self.name ,self.age , self.roll_no)


s1 = Student("Rahul", 20, 101)
s1.display_details()