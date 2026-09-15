
def read_existing_file_content4(filename):
    try:
        file=open(filename, 'r')
        for line in file:
            print(line, end="")
    except IOError as e:
        print("There is a error occured during opening a File ",e)
    finally:
        file.close()

read_existing_file_content4("C:/DEMO/Test.txt")