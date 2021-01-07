import xml.etree.ElementTree as ET 

tree = ET.parse("images\Data0512222.xml")
root = tree.getroot()

pathname = root.find('path')
pnl = pathname.text.split('\\')
print(pnl)
pnl[-1] = 'Data0512'+'.jpg'

newpathname = pnl[0]
for i in range(1,len(pnl)):
    newpathname = newpathname + '\\' + pnl[i]
pathname.text = newpathname

print(pathname.text)