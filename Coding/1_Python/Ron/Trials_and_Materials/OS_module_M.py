import os
"""
os.access(path, mode)
"""
# Check a access authority
# path = "/tmp/foo.txt"
# mode = [os.F_OK,os.R_OK,os.W_OK,os.X_OK]
# mode_meaning = ["test_path_exist","test_path_readable","test_path_writable","test_path_executable"]

#e.g.
ret = os.access("tmp/foo.txt", os.F_OK)
print ("F_OK - 返回值 {}".format(ret))
# Result: F_OK - 返回值 False

"""
os.chdir(path)
"""
os.chdir("tmp")
data = open("foo.txt", "r")
for i in data:
    print(i)
data.close()
