import os
import glob
import xml.etree.ElementTree as ET

xmlpath = glob.glob("../merged_xml/*.xml")
newxmlpath = "../newmerged_xml/"

os.makedirs(newxmlpath)

index = 0

for xp in xmlpath:
    tree = ET.parse(xp)
    root = tree.getroot()
    print(index)
    index += 1
    for member in root.findall('object'):
        if member[0].text == 'sf':
            member[0].text = 'smoke'

    tree.write(os.path.join(newxmlpath,xp.split('/')[-1]))
        