
def read_existing_file_content1(filename):
    try:
        file=open(filename, 'r')
        content=file.read()
        print(content)
    except IOError as e:
        print("There is a error occured during opening a File ",e)
    finally:
        file.close()

read_existing_file_content1("C:/DEMO/Test.txt")