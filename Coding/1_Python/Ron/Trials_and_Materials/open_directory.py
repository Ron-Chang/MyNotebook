import os
import subprocess

# # windows
# app = "explorer"
# targetDir = r'c:\documents and settings\foo\bar'
# folder_info = app+" "+targetDir
# subprocess.Popen(folder_info)

#MacOS_1
targetDirectory = "/Users/ron/Downloads"
subprocess.call(["open", targetDirectory])
