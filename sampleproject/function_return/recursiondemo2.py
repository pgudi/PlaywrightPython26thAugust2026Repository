# Case 2: Without using a Looping Statement , print numbers from 10 to 20
num=10
def display_number():
    global num
    if(num<=20):
        print(num)
        num=num+1
        display_number()

display_number()