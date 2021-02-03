import argparse
import os
import cv2
import glob
import xml.etree.ElementTree as ET
import copy
import shutil

def makepath(path):
    if not os.path.exists(path):
        os.makedirs(path)


def CropImgAndFixXML(imgpath, xmlpath, newimgpath, newxmlpath):

    tmpath = os.path.join(newimgpath,'tmp')

    makepath(newimgpath)
    makepath(newxmlpath)
    makepath(tmpath)

    imglist = glob.glob(os.path.join(imgpath, '*.jpg'))
    imglist = sorted(imglist)
    for imgfile in imglist:
        basename = os.path.basename(imgfile)
        file, ext = os.path.splitext(basename)
        xmlfile = os.path.join(xmlpath, file+'.xml')
        if os.path.exists(xmlfile):
            img = cv2.imread(imgfile)
            showimg = copy.deepcopy(img)
            oh, ow, _ = showimg.shape
            cv2.putText(showimg, str(oh) + ' ' + str(ow), (0,20), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 3)
            cv2.imshow(basename, showimg)
            cv2.waitKey(1)
            
            order = input("input the order: ")
            wsize = 0
            asize = 0
            ssize = 0
            dsize = 0
            while(order != '0'):
                showimg = copy.deepcopy(img)
                if order == 'w':
                    wsize = int(input("input the w size: "))
                    tmpimg = showimg[wsize:oh-ssize,asize:ow-dsize,:]
                    h, w, _ = tmpimg.shape
                    cv2.putText(tmpimg, str(h) + '  ' + str(w), (0,20), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 3)
                    cv2.imshow(basename, tmpimg)
                    cv2.waitKey(1)
                elif order == 's':
                    ssize = int(input("input the s size: "))
                    tmpimg = showimg[wsize:oh-ssize,asize:ow-dsize,:]
                    h, w, _ = tmpimg.shape
                    cv2.putText(tmpimg, str(h) + '  ' + str(w), (0,20), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 3)
                    cv2.imshow(basename, tmpimg)
                    cv2.waitKey(1)
                elif order == 'a':
                    asize = int(input("input the a size: "))
                    tmpimg = showimg[wsize:oh-ssize,asize:ow-dsize,:]
                    h, w, _ = tmpimg.shape
                    cv2.putText(tmpimg, str(h) + '  ' + str(w), (0,20), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 3)
                    cv2.imshow(basename, tmpimg)
                    cv2.waitKey(1)
                elif order == 'd':
                    dsize = int(input("input the d size: "))
                    tmpimg = showimg[wsize:oh-ssize,asize:ow-dsize,:]
                    h, w, _ = tmpimg.shape
                    cv2.putText(tmpimg, str(h) + '  ' + str(w), (0,20), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 3)
                    cv2.imshow(basename, tmpimg)
                    cv2.waitKey(1)
                print(h / 480 * 640)
                order = input("input the order: ")
                
            tree = ET.parse(xmlfile)
            root = tree.getroot()
            sizeObj = root.find('size')
            width = int(sizeObj[0].text)
            height = int(sizeObj[1].text)

            sizeObj[0].text = str(ow - dsize - asize)
            sizeObj[1].text = str(oh - ssize - wsize)

            for member in root.findall('object'):
                xmin = int(member[4][0].text)
                ymin = int(member[4][1].text)
                xmax = int(member[4][2].text)
                ymax = int(member[4][3].text)

                member[4][0].text = str(xmin - asize)
                member[4][1].text = str(ymin - wsize)
                member[4][2].text = str(xmax - asize)
                member[4][3].text = str(ymax - wsize)

            newxmlfile = os.path.join(newxmlpath, file+'.xml')
            tree.write(newxmlfile) 

            newimgfile = os.path.join(newimgpath, basename)
            cv2.imwrite(newimgfile, img[wsize:oh-ssize,asize:ow-dsize,:]) 

            shutil.move(imgfile, os.path.join(tmpath, basename))

            cv2.destroyAllWindows()


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--imgpath', type=str, default='.')
    parser.add_argument('--xmlpath', type=str, default='.')
    parser.add_argument('--newimgpath', type=str, default='.')
    parser.add_argument('--newxmlpath', type=str, default='.')
    args = parser.parse_args()
    CropImgAndFixXML(args.imgpath, args.xmlpath, args.newimgpath, args.newxmlpath)