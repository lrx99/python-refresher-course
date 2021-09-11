import os

path = "C:\\Users\\LRXCalvin\\PycharmProjects\\refresherCourse\\test.txt"

#file detection
if os.path.exists(path):
    print("the file exist")
    if os.path.isfile(path): #checking if its a file
        print("its a file")
    elif os.path.isdir(path): #checking if its a directory
        print("its a dir")
else:
    print("wth is going on")

#reading a file
with open(path) as file: #with open() will help close the file, or we will need to use
    print(file.read())   #print(file.close())

#writing a file
text = "This is some amazing text art."
with open(path, 'a') as file: #'a' -> append, 'w' -> write, 'r' -> read
    file.write(text)

#copying a file
#copyfile() -> copies contents of a file
#copy() -> does what copyfile() do + permission mode + destination can be a dir
#copy2() -> does what copy() do + copies metadata(file's creation and modification time)
import shutil

shutil.copyfile(path, "text(1).txt") #(source, destination)

#moving a file
"""destination = "C:\\users\\LRXCalvin\\Desktop\\test.txt"

try:
    if os.path.exists(destination):
        print("There is a file already there")
    else:
        os.replace(path, destination)
        print("File has been moved")
except FileNotFoundError:
    print(path+ "not found!")"""

#deleting a file
rubbish = "text(1).txt"
emptyFolder = "folder"

try:
    os.remove(rubbish) #delete a file only
    os.rmdir(emptyFolder) #delete an empty dir
    shutil.rmtree(emptyFolder) #delete a dir containing files
except FileNotFoundError:
    print("File was not found")
except PermissionError:
    print("No permission to delete the file")
else:
    print(path+ "is deleted")