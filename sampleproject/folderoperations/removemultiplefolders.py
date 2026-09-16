import os

def remove_multiple_folders(folderpath):
    os.removedirs(folderpath)

remove_multiple_folders("C:/DEMO/A/B/C/D/E/F/G")