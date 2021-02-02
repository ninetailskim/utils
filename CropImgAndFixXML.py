import argparse
import os
import cv2
import glob
import xml.etree.ElementTree as ET
import copy

def makepath(path):
    if not os.path.


def CropImgAndFixXML(imgpath, xmlpath, newimgpath, newxmlpath):
    
    imglist = glob.glob(os.path.join(imgpath, '*.jpg'))
    imglist = sorted(imglist)
    for imgfile in imglist:
        file, ext = os.path.splitext(os.path.basename(imgfile))
        xmlfile = os.path.join(xmlpath, file+'.xml')
        if os.path.exists(xmlfile):
            img = cv2.imread(imgfile)
            showimg = copy.deepcopy(img)
            h, w, _ = showimg.shape
            cv2.putText(showimg, str(h) + '  ' + str(w), (0,0), cv2.FONT_HERSHEY_SIMPLEX)
            cv2.imshow("tmp", showimg)
            cv2.waitKey()
            
            order = input("input the order")
            wsize = 0
            asize = 0
            ssize = h
            dsize = w
            while(order != 0):
                if order == 'w':
                    wsize = int(input("input the size"))
                    tmpimg = showimg[wsize:, :, :]
                    h, w, _ = tmpimg.shape
                    cv2.putText(tmpimg, str(h) + '  ' + str(w), (0,0), cv2.FONT_HERSHEY_SIMPLEX)
                    cv2.imshow("tmp", tmpimg)
                    cv2.waitKey()
                elif order == 's':
                    ssize = int(input("input the size"))
                    tmpimg = showimg[:ssize, :, :]
                    h, w, _ = tmpimg.shape
                    cv2.putText(tmpimg, str(h) + '  ' + str(w), (0,0), cv2.FONT_HERSHEY_SIMPLEX)
                    cv2.imshow("tmp", tmpimg)
                    cv2.waitKey()
                elif order == 'a':
                    asize = int(input("input the size"))
                    tmpimg = showimg[:, asize:, :]
                    h, w, _ = tmpimg.shape
                    cv2.putText(tmpimg, str(h) + '  ' + str(w), (0,0), cv2.FONT_HERSHEY_SIMPLEX)
                    cv2.imshow("tmp", tmpimg)
                    cv2.waitKey()
                elif order == 'd':
                    dsize = int(input("input the size"))
                    tmpimg = showimg[:, :dsize, :]
                    h, w, _ = tmpimg.shape
                    cv2.putText(tmpimg, str(h) + '  ' + str(w), (0,0))
                    cv2.imshow("tmp", tmpimg)
                    cv2.waitKey()
                
            tree = ET.parse(xmlfile)
            root = tree.getroot()
            sizeObj = root.find('size')
            width = int(sizeObj[0].text)
            height = int(sizeObj[1].text)

            sizeObj[0].text = str(dsize - asize)
            sizeObj[1].text = str(ssize - wsize)

            for member in root.findall('object'):
                xmin = int(member[4][0].text)
                ymin = int(member[4][1].text)
                xmax = int(member[4][2].text)
                ymax = int(member[4][3].text)

                member[4][0].text = str(xmin - asize)
                member[4][1].text = str(ymin - wsize)
                member[4][2].text = str(xmax - asize)
                member[4][3].text = str(ymax - wsize)

            newxmlpath = os.path.join(newxmlpath, file+'.xml')
            tree.write(newxmlpath)   


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--imgpath', type=str, default='.')
    parser.add_argument('--xmlpath', type=str, default='.')
    parser.add_argument('--newimgpath', type=str, default='.')
    parser.add_argument('--newxmlpath', type=str, default='.')
    args = parser.parse_args()
    CropImgAndFixXML(args.imgpath, args.xmlpath, args.newimgpath, args.newxmlpath)