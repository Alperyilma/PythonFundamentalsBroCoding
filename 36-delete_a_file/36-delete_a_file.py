import os
import shutil # we use shutil library while we want to delete to full directory

path = "36-test.txt"
path_folder = "empty_folder"
path_full_folder = "folder"

 #Below method is for a file

try:
    os.remove(path)
except FileNotFoundError:
    print("File was not found")

 #For empty folder

try:
    os.rmdir(path_folder)
except FileNotFoundError:
    print("File was not found")
except PermissionError:
    print("You do not have permission to delete that")
else:
    print(path_folder, "was deleted")


#For full folder

try:
    shutil.rmtree(path_full_folder)
except OSError:
    print("You cannot delete that using that function")
else:
    print(path_full_folder, "was deleted")


