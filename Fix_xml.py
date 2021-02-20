import argparse
import os
import glob
import xml.etree.ElementTree as ET

'''
0 shoe
1 trans can
2 sock
3 wire
'''

label2id = {
    'shoes': '0',
    'trash can': '1',
    'sock': '2',
    'wire': '3'
}


def VOC2YOLO(xmlPath, newxmlpath):
    xmlfiles = glob.glob(xmlPath+"/*.xml")
    for xmlfile in xmlfiles:
        print(xmlfile)
        basename = os.path.basename(xmlfile)
        tree = ET.parse(xmlfile)
        root = tree.getroot()
        width = int(root.find('size')[0].text)
        height = int(root.find('size')[1].text)
        members = root.findall('object')
        for i in range(len(members)):
            
            member = members[i]

            item = member[0].text
            if item not in label2id.keys():
                print(item)

            xmin = int(member[4][0].text)
            ymin = int(member[4][1].text)
            xmax = int(member[4][2].text)
            ymax = int(member[4][3].text)

            if xmin < 0 or xmin > width:
                print("occur")
            
            if ymin < 0 or ymin > height:
                print("occur")
            
            if xmax < 0 or xmax > width:
                print("occur")

            if ymax < 0 or ymax > height:
                print("occur")

            xmin = 0 if xmin < 0 else xmin
            ymin = 0 if ymin < 0 else ymin
            xmax = width if xmax > width else xmax
            ymax = height if ymax > height else ymax

            xmin = width if xmin > width else xmin
            ymin = height if ymin > height else ymin
            xmax = 0 if xmax < 0 else xmax
            ymax = 0 if ymax < 0 else ymax

            icx = (xmin + xmax) // 2
            icy = (ymin + ymax) // 2
            iheight = ymax - ymin
            iwidth = xmax - xmin

            if iheight * iwidth == 0:
                root.remove(member)
                print("fuck")
                continue

            member[4][0].text = str(xmin)
            member[4][1].text = str(ymin)
            member[4][2].text = str(xmax)
            member[4][3].text = str(ymax)

        newxmlfile = os.path.join(newxmlpath, basename)
        tree.write(newxmlfile)   



if __name__ == '__main__':
    paser = argparse.ArgumentParser()
    paser.add_argument("--xmlPath", type=str, required=True)
    paser.add_argument("--newxmlPath", type=str, required=True)
    args = paser.parse_args()
    VOC2YOLO(args.xmlPath, args.newxmlPath)
