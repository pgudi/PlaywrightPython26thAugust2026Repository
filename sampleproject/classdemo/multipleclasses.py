class Employee:
    def __init__(self, ename, jobname,sal):
        self.ename=ename
        self.jobname=jobname
        self.sal=sal

    def show_employee_details(self):
        print(self.ename, "|", self.jobname,"|",self.sal)


class Insurance:
    def __init__(self, insurancename, policynumber):
        self.insurancename=insurancename
        self.policynumber=policynumber

    def display_insurance_details(self):
        print(self.insurancename, "=>", self.policynumber)


obj1=Employee("Santosh","Sales Manager",45000)
obj1.show_employee_details()

obj1=Insurance("Vehicle Insurance","VAH001100011")
obj1.display_insurance_details()