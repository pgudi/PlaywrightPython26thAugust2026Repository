
def verify_positive_number(num):
    try:
        if(num < 0):
            raise Exception("Input only the Numbers, which are greater than Zero")
        else:
            print(num," is a Positive Number")
    except Exception as e:
        print(e)

verify_positive_number(12)
verify_positive_number(-10)