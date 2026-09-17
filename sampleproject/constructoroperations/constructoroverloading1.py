
class Employee:
    def __init__(self, empno=None, ename=None, jobname=None, sal=None):
        self.empno=empno
        self.ename=ename
        self.jobname=jobname
        self.sal=sal
        print("Employee Number :",self.empno)
        print("Employee Name :",self.ename)
        print("Employee Job Name :",self.jobname)
        print("Employee Salary :",self.sal)
        print("---------------")

obj1=Employee()
obj2=Employee(101)
obj3=Employee(102,"Santosh")
obj4=Employee(103,"Vinith","Analyst")
obj5=Employee(104,"Srinivasa","Clerk",25000)