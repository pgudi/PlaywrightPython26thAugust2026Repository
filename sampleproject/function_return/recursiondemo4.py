
def fifth_table(num):
    if num> 10:
        return
 
    print("5 x", num, "=", 5 * num)
    fifth_table(num + 1)
 
fifth_table(1)