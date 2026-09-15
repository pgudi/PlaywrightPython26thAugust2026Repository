
def write_text_content1(filename):
    try:
        file=open(filename,"w")
        file.write("It is a old Palace and It has found in the out of the city. \n")
        file.write("the palace was previous ruled by Kadamba Dynesty. \n")
    except IOError as e:
        print("There is an Error Occured while writing content in to A File :",e)
    finally:
        file.close()

write_text_content1("C:/DEMO/Welcome.txt")