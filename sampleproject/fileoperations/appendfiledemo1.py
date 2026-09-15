
def append_content_file1(filename):
    try:
        file=open(filename,"a")
        file.write("Java is a High Level Language. \n")
        file.write("Python is a Scripting Language. \n")
    except IOError as e:
        print("There is an error occured during writing content to a File :",e)
    finally:
        file.close()

append_content_file1("C:/DEMO/Example.txt")