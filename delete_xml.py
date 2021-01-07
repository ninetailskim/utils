import os
import time
import shutil
import glob

xmlfilepath = 'trashbin/bbox'

imgfilepath = 'trashbin/only_xml'

xmlname = os.listdir(xmlfilepath)
num = len(xmlname)

print(num)

for i in range(num):
    name = xmlname[i]
    if name[-3:] == 'xml':
        print(name)
        filename = name[:-4]
        if filename + '.JPEG' not in xmlname:
            oldpath = os.path.join(xmlfilepath, name)
            #newpath = 
            shutil.move(oldpath, imgfilepath)