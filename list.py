import os

folders = input("please provide list of folders name with spaces in between:").split()
for folder in folders:
        files = os.listdir(folder)
    
        print(" === listing files for the folders - " + folder)
        for file in files:
            print(file)
