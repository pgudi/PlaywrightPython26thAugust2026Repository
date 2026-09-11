
def display_details(*args, **kwargs):
    for item in args:
        print(item)

    print("---------")

    for k, v in kwargs.items():
        print(k, " --> ",v)

display_details(10,20,30,40,customername="LG Service",emailid="services@lg.com")