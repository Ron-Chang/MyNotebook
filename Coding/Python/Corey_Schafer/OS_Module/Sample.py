import os
#print(dir(os))
# to get more methods

# os.getcwd() stand for GET Current Working Directory
print(os.getcwd())

# os.chdir("") stand for CHange DIRectory
os.chdir("tmp")
print(os.getcwd())

# os.listdir(default = "current location") stand LIST Directory
print(os.listdir(".."))

# 2 ways to make a directory
# os.mkdir("name") allow to MaKe a DIRectory
# os.makedirs("name/sub_1/sub_2") allow to MAKE different level sub DIRectorieS
os.mkdir("mkdir_test")
os.makedirs("makedirs_test/sub_1/sub_2")

print(os.listdir())

# 2 ways to remove a directory
# os.rmdir("name") allow to ReMove a DIRectory
# os.removedirs("name/sub_1/sub_2") allow to REMOVE different level sub DIRectorieS (Be Careful to use it.)
os.rmdir("mkdir_test")
os.removedirs("makedirs_test/sub_1/sub_2")

#os.rename("original name", "new name")
os.rename("foo.txt", "demo.txt")
os.rename("demo.txt", "foo.txt")

#os.stat("target") get STATe of the file
print(os.stat("foo.txt"))
# st_size: the file size is 17 Bytes
print(os.stat("foo.txt").st_size)
# st_mtime: the file's modify time.
print(os.stat("foo.txt").st_mtime) # Get a machine time
from datetime import datetime
mod_time = os.stat("foo.txt").st_mtime
print(datetime.fromtimestamp(mod_time)) # Get a human readable form

# os.walk("dir_name") WALK entire directory tree print out
# extremely handy for web and find a file.
os.chdir("/Users/ron/Documents/MyNotebook/Coding/1_Python")
print(os.getcwd())
for dirpath, dirnames, filenames in os.walk("Ron"):
    print("Current Path: ", dirpath)
    print("Directories: ", dirnames)
    print("Files: ", filenames)
    print()

os.chdir("Ron/Trials_and_Materials/") # switch dir back

# os.environ.get("")
# os.path.join(dir_1,dir_2) Automatic to add a slash / between them
file_path = os.path.join(os.environ.get("HOME"),'test.txt')
print(file_path)
'''Extention
with open (file_path, "w") as f:
    f.write("text_1")
'''


# os.path
# print(dir(os,path)) to get more methods

# os.path.basename("") Get file's name
# os.path.dirname("") Get file's directory
# os.path.split("") Get file's directory and name
print(os.path.basename("tmp/foo.txt"))
print(os.path.dirname("tmp/foo.txt"))
print(os.path.split("tmp/foo.txt"))
# os.path.exists("") Check file exists or not
print(os.path.exists("tmp/foo.txt"))
# os.path.isdir("") Check is it a directory or not
# os.path.isfile("") Check is it a file or not
print(os.path.isdir("tmp"))
print(os.path.isfile("tmp"))
# os.path.splitext("") Split root and extention
print(os.path.splitext("tmp/foo.txt"))
# print(os.path.splitext("tmp/foo.txt")[0])
