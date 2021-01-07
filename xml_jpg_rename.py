import glob
import xml.etree.ElementTree as ET  
import os
import shutil 

xml = glob.glob("merged_xml/*.xml")
print(xml)

for i, xmlpath in enumerate(xml):
    tree = ET.parse(xmlpath)
    root = tree.getroot()

    filename = root.find('filename')
    imagename = filename.text
    #os.rename('images/'+imagename,'newimages/Data0512'+str(i)+'.jpg')
    shutil.copyfile('images/'+imagename, 'newimages/Data0512'+str(i)+'.jpg') 
    print(filename.text)
    filename.text = 'Data0512'+str(i)+'.jpg'

    pathname = root.find('path')
    pnl = pathname.text.split('\\')
    pnl[-1] = 'Data0512'+str(i)+'.jpg'

    newpathname = pnl[0]
    for index in range(1,len(pnl)):
        newpathname = newpathname + '\\' + pnl[index]
    pathname.text = newpathname

    tree.write('newxml/Data0512'+str(i)+'.xml')