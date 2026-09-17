
class Employee:
    def __init__(self, **kwargs):
        if(kwargs.get("empno")==None and kwargs.get("ename")==None and kwargs.get("job")==None and kwargs.get("sal")==None):
            print("It is a No Args Constructor!!!")
            print("----------------")
        elif(kwargs.get("ename")==None and kwargs.get("job")==None and kwargs.get("sal")==None):
            print("Employee Number :",kwargs.get("empno"))
            print("----------------")
        elif(kwargs.get("job")==None and kwargs.get("sal")==None):
            print("Employee Number :",kwargs.get("empno"))
            print("Employee Name :",kwargs.get("ename"))
            print("----------------")
        elif(kwargs.get("sal")==None):
            print("Employee Number :",kwargs.get("empno"))
            print("Employee Name :",kwargs.get("ename"))
            print("Employee Job :",kwargs.get("job"))
            print("----------------")
        else:
            print("Employee Number :",kwargs.get("empno"))
            print("Employee Name :",kwargs.get("ename"))
            print("Employee Job :",kwargs.get("job"))
            print("Employee Salary :",kwargs.get("sal"))
            print("----------------")

obj1=Employee()
obj2=Employee(empno=1901)
obj3=Employee(empno=1902,ename="Santosh")
obj4=Employee(empno=1903,ename="Srinivasa",job="Analyst")
obj5=Employee(empno=1904,ename="Vinith",job="Clerk",sal=43000)



