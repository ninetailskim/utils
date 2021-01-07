import glob
import shutil
import os
import xml.etree.ElementTree as ET


xmlpath = glob.glob("../merged_xml/*.xml")
oldimgpath = "../Images/"
newimgpath = "../newimage/"

os.makedirs(newimgpath)

for xp in xmlpath:
    tree = ET.parse(xp)
    root = tree.getroot()
    filename = root.find('filename').text
    
    shutil.copyfile(os.path.join(oldimgpath, filename), os.path.join(newimgpath, filename))
