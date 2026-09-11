
def display_employee(ename, jobname="Health Analyst", dname="Health", sal=45000):
    print("Emp0loyee Name :",ename)
    print("Emp0loyee Job Name :",jobname)
    print("Department Name :",dname)
    print("Employee Salary :",sal)
    print("-------------------")

display_employee("Santosh")
display_employee("Santosh", jobname="Senior Doctor")
display_employee("Adams", jobname="Senior Doctor", dname="Research")
display_employee("Richard", jobname="Senior Analyst", dname="Research and Science")