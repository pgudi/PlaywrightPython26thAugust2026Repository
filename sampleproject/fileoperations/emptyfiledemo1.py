
def create_empty_file(filename):
    try:
        file=open(filename, "x")
    except IOError as e:
        print("there is an Error Occured during creation of blank File ",e)
    finally:
        file.close()

create_empty_file("C:/DEMO/TestingTopics.txt")