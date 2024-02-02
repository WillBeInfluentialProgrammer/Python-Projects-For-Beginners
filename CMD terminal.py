import os
print("Microsoft Windows [Version 10.0.19044.1466] \n (c) Microsoft Corporation. All rights reserved. \n")
while 1:
    cmd = input(os.getcwd() + ">")
    print(os.popen(cmd).read())