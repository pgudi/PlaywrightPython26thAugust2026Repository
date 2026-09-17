
class Employee:
    def __init__(self, *args):
        if(len(args)==0):
            print("It is No Args Constructor!!!")
            print("----------")
        elif(len(args)==1):
            print("Employee Id :",args[0])
            print("----------")
        elif(len(args)==2):
            print("Employee Id :",args[0])
            print("Employee Name :",args[1])
            print("----------")
        elif(len(args)==3):
            print("Employee Id :",args[0])
            print("Employee Name :",args[1])
            print("Employee Job Name :",args[2])
            print("----------")
        else:
            print("Employee Id :",args[0])
            print("Employee Name :",args[1])
            print("Employee Job Name :",args[2])
            print("Employee Salary:",args[3])
            print("----------")

obj1=Employee()
obj2=Employee(1901)
obj3=Employee(1902,"Santosh")
obj4=Employee(1903,"Srinivasa","Analyst")
obj5=Employee(1904,"Vinith","Clerk",43000)