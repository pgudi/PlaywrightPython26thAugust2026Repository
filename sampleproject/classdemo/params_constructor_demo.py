
class Department:
    def __init__(self, deptno,dname,loc):
        self.deptnumber=deptno
        self.deptname=dname
        self.location=loc

    def display_department_details(self):
        print(self.deptnumber,"|", self.deptname,"|", self.location)

    
obj=Department(10,"Accounting","Boston")
obj.display_department_details()

obj2=Department(20, "Research","Sanjose")
obj2.display_department_details()