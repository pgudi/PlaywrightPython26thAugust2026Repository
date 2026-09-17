
class Employee:
    def __init__(self, empno=None, ename=None, jobname=None, sal=None):
        self.empno=empno
        self.ename=ename
        self.jobname=jobname
        self.sal=sal
        if(empno==None and ename==None and jobname==None and sal==None):
            print("It is a No Args Constructor!!")
            print("-----------------")
        elif(ename==None and jobname==None and sal==None):
            print("Employee Number :",self.empno)
            print("-----------------")
        elif(jobname==None and sal==None):
            print("Employee Number :",self.empno)
            print("Employee Name :",self.ename)
            print("-----------------")
        elif(sal==None):
            print("Employee Number :",self.empno)
            print("Employee Name :",self.ename)
            print("Employee Job Name :",self.jobname)
            print("-----------------")
        else:
            print("Employee Number :",self.empno)
            print("Employee Name :",self.ename)
            print("Employee Job Name :",self.jobname)
            print("Employee Salary :",self.sal)
            print("-----------------")

obj1=Employee()
obj2=Employee(1001)
obj3=Employee(1001, "Santosh")
obj4=Employee(1002,"Sahana","Clerk")
obj5=Employee(1003,"Srinivasa","Analyst",45000)
