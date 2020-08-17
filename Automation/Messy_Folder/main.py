import os   # Interacting with Operating-System
import re   # Regular Expression
import shutil  # High-level operations of file and collections of files

input_dir = input("Enter Directory which you want to organize :- ")     # Please enter directory... in which you want to sort files according to extensions
os.chdir(input_dir)     # Changing current working directory

pattern_ext = re.compile("(.{3}$)")   # Compiling the regular expression to identify extensions.

formats = {}


# Checking for different extensions and their count.

for root, directory, files in os.walk(os.getcwd()):     # walking through the file directory and subdirectories

    for file in files:      # for each file 
        r = pattern_ext.search(file)    # searching the pattern
        ext = r.group()
        if ext not in formats:          # Building a dictionary, in which key will be the extension and value will the occurrence of it in the folder.
            formats[ext] = 1
        else:
            formats[ext] += 1

folders_ext = {}


# Creation of Folders

for i, j in formats.items():        # for every extension
    path = os.path.join(os.getcwd(), i.upper())     # joining the path of current working directory and the file
    folders_ext[i] = path                   # Storing it in another dictionary in which key will be the extention name and value is the path to New folder created with that extention name.
    if not os.path.exists(path):            # Checking if New Folder path already exists or not. If No, make directory else move ahead.
        os.mkdir(path)

# Moving file to their respective extension-folders.

for root, directory, files in os.walk(os.getcwd()):
    for file in files:
        r = pattern_ext.search(file)
        ext = r.group()

        path_file = os.path.join(os.getcwd(), file)     # Joining the path of every file with currect working directory
        # print(path_file, folders_ext[ext])
        try:
            shutil.move(path_file, folders_ext[ext])    # Moving file to their respective folders.
        except: 
            pass

print("Operation Successful!")