
def write_text_content1(filename):
    try:
        file=open(filename,"w")
        list=["Line 1 \n","Line 2 \n","Line 3 \n","Line 4 \n", "Line 5 \n"]
        file.writelines(list)
    except IOError as e:
        print("There is an Error Occured while writing content in to A File :",e)
    finally:
        file.close()

write_text_content1("C:/DEMO/Welcome_new.txt")