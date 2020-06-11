import os

path1 = os.getcwd() + '\\trainer'
path2 = os.getcwd() + '\\dataset'
suc = True

try:
    os.mkdir(path1)
    os.mkdir(path2)
except OSError:
    print('directory creation failed')
    suc = False
else:
    print('directory creation worked')
    suc = True
