import os
import time
import shutil
import glob

xmlfilepath = 'trashbin/bbox'

imgfilepath = 'trashbin'

xmlname = os.listdir(xmlfilepath)
imgname = os.listdir(imgfilepath)
num = len(imgname)

print(num)

for i in range(num):
    
    name = imgname[i]
    print(name)
    filename = name[:-4]
    if name[-4:] == 'JPEG':
        if filename + 'xml' in xmlname:
            filePath = os.path.join(imgfilepath, name)
            newfile=os.path.join(xmlfilepath, name)
            shutil.copyfile(filePath, newfile)
            print(filePath)
            print(newfile)
        else:
            filePath = os.path.join(imgfilepath, name)
            newfile=os.path.join(imgfilepath, os.path.join('no_xml',name))
            shutil.copyfile(filePath, newfile)
            print(filePath)
            print(newfile)