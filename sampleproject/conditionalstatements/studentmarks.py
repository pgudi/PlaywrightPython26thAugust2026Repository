marks=int(input("enter the Student Marks : \n"))

if(marks>=70 and marks<=100):
    print("the Result is FCD !!!!")
elif(marks<70 and marks>=60):
    print("the Result is First Class !!!!")
elif(marks<60 and marks>=50):
    print("the Result is Second Class !!!!")
elif(marks<50 and marks>=35):
    print("the Result is Pass Class !!!!")
elif(marks<35 and marks>=0):
    print("The Result has Failed !!!")
else:
    print("Invalid Marks")