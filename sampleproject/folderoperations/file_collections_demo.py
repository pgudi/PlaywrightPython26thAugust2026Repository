import os
def file_collections_demo(folderpath):
    dirs=os.listdir(folderpath)

    for filename in dirs:
        full_path=folderpath + filename

        if(os.path.isfile(full_path)==True):
            print(full_path)




file_collections_demo("C:/DEMO/")