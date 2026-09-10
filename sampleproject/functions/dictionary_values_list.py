# Case 6: Write a program for the given dictionary assign all values into a list.

def assign_dict_values_to_list(dictionary_test):
    list=[]
    for val in dictionary_test.values():
        list.append(val)
    print(list)


employee={
    "ename":"Santosh",
    "jobname":"Sales Executive",
    "sal":45000,
    "dname":"Sales and Purchase"
}
assign_dict_values_to_list(employee)