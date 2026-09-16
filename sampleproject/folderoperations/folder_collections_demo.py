import os

def folder_collections_demo(folderpath):
    dirs=os.listdir(folderpath)

    for foldername in dirs:
        full_path=folderpath + foldername
        if(os.path.isdir(full_path)==True):
            print(full_path)

folder_collections_demo("C:/DEMO/")