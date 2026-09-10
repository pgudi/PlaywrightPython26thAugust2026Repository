# Without Return value
def show_studnet_name(sname):
    print("The Student name is ",sname)


show_studnet_name("Santosh")

print("-------------------")
# with return value

def get_student_name(sname):
    return sname


v1=get_student_name("Srinivasa")
print(v1)
print("Name of the Student ",v1)
print("the Student who belong to our Cricket Team is ",v1)