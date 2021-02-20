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


def VOC2YOLO(xmlPath,yoloPath):
    xmlfiles = glob.glob(xmlPath+"/*.xml")
    for xmlfile in xmlfiles:
        print(xmlfile)
        basename = os.path.basename(xmlfile)
        tree = ET.parse(xmlfile)
        root = tree.getroot()
        yolofile = os.path.join(yoloPath, basename[:-4]+'.txt')
        with open(yolofile,'w+') as fp:
            width = int(root.find('size')[0].text)
            height = int(root.find('size')[1].text)
            for member in root.findall('object'):
                item = ""
                item += label2id[member[0].text]
                xmin = int(member[4][0].text)
                ymin = int(member[4][1].text)
                xmax = int(member[4][2].text)
                ymax = int(member[4][3].text)

                icx = (xmin + xmax) // 2
                icy = (ymin + ymax) // 2
                iheight = ymax - ymin
                iwidth = xmax - xmin

                item = item + " " + str(icx / width) 
                item = item + " " + str(icy / height)
                item = item + " " + str(iwidth / width)  
                item = item + " " + str(iheight / height) + '\n'

                fp.write(item)    



if __name__ == '__main__':
    paser = argparse.ArgumentParser()
    paser.add_argument("--xmlPath", type=str, required=True)
    paser.add_argument("--yoloPath", type=str, required=True)
    args = paser.parse_args()
    VOC2YOLO(args.xmlPath,args.yoloPath)
