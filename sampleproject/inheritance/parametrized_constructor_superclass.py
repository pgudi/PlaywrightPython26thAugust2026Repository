class Employee:
    def __init__(self, empno,ename,job):
        self.empno=empno
        self.ename=ename
        self.job=job

    def display_employee_details(self):
        print(self.empno, self.ename, self.job)


class Department(Employee):
    def __init__(self, dname,location,empno1, ename1, job1):
        super().__init__(empno1, ename1, job1)
        self.dname=dname
        self.location=location

    def display_department_details(self):
        print(self.dname, self.location)

obj=Department("Accounting","California",101,"Santosh","Analyst")

obj.display_employee_details()
obj.display_department_details()