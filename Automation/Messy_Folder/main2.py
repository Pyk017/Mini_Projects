import os

files_list = os.listdir('./')

os.mkdir('csv')
os.mkdir('txt')
os.mkdir('mp3')

for file in files_list:
    if file.endswith("mp3"):
        os.rename(file, 'mp3/' + file)
    if file.endswith("csv"):
        os.rename(file, 'csv/' + file)
    if file.endswith("txt"):
        os.rename(file, 'txt/' + file)
    
print("Success")
