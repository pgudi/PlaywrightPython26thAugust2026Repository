# Case 3: Without using a Looping Statement, print even numbers from 20 to 40
num=20
def display_even_number():
    global num
    if(num<=40):
        if(num % 2 ==0):
            print(num)
        num=num+1
        display_even_number()


display_even_number()