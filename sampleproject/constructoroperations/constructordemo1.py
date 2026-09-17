class Student:
    def __init__(self):
        print("Welcome to No Args Constructor")

    def __init__(self, firstname):
        print("first Name :",firstname)

    def __init__(self, firstname,coursename,age):
        print("First Name :",firstname)
        print("Course Name :",coursename)
        print("Age :",age)

obj1=Student()
obj2=Student("Santosh")
obj3=Student("Santosh","Research and Science",22)