import os
import shutil # we use shutil library while we want to delete to full directory

class Work_with_file:

    def resources(self,path):
        if os.path.exists(path):
            print("That location is exist")
            if os.path.isfile(path):
                print("This is a file")
            elif os.path.isdir(path):
                print("This is a directory")

    def write_file(self,path,text):
        with open(path, "w") as file:
            file.write(text)

    def read_file(self, path):
        with open(path) as file:
            print(file.read())

    def delete_file_and_emptyfolder(self,path):
        try:
            if os.path.isfile(path):
                os.remove(path)
                print(path, "file was deleted by delete_file_and_emptyfolder")
            #For empty folder
            elif os.path.isdir(path):
                os.rmdir(path)
                print(path, "directory was deleted by delete_file_and_emptyfolder")
        except FileNotFoundError:
            print("The file was not found")
        except PermissionError:
            print("You do not have permission to delete that")
        except OSError:
            print("You cannot delete it with delete_file_and_emptyfolder")


    def delete_full_folder(self,path):
        try:
            shutil.rmtree(path)
            print(path, "directory was deleted by delete_full_folder")
        except FileNotFoundError:
            print("The directory was not found")
        except PermissionError:
            print("You do not have permission to delete that")



txt_path = "36-test.txt"
folder_path = "testemptyfolder"
full_folder_path = "testfullfolder"
text = "Python is a KING ! Death to obsolete languages"

withfile = Work_with_file()

withfile.write_file(txt_path, text)
withfile.read_file(txt_path)


withfile.resources(txt_path)
withfile.resources(folder_path)

withfile.delete_file_and_emptyfolder(txt_path)
withfile.delete_file_and_emptyfolder(folder_path)
withfile.delete_full_folder(full_folder_path)


