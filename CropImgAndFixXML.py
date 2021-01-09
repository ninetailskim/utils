import argparse
import os
import cv2
import glob
import xml.etree.ElementTree as ET
import copy

def CropImgAndFixXML(imgpath, xmlpath, newimgpath, newxmlpath):
    imglist = glob.glob(os.path.join(imgpath, '*.jpg'))
    imglist = sorted(imglist)
    for imgfile in imglist:
        file, ext = os.path.splitext(os.path.basename(imgfile))
        xmlfile = os.path.join(xmlpath,file+'.xml')
        if os.path.exists(xmlfile):
            img = cv2.imread(imgfile)
            showimg = copy.deepcopy(img)
            h, w, _ = showimg.shape
            cv2.putText(showimg, str(h) + '  ' + str(w), (0,0), cv2.FONT_HERSHEY_SIMPLEX)
            cv2.imshow("tmp", showimg)
            cv2.waitKey()
            
            order = input("input the order")
            while(order != 0):
                if order == 'w':
                    size = int(input("input the size"))
                    tmpimg = showimg[size:, :, :]
                    h, w, _ = tmpimg.shape
                    cv2.putText(tmpimg, str(h) + '  ' + str(w), (0,0), cv2.FONT_HERSHEY_SIMPLEX)
                    cv2.imshow("tmp", tmpimg)
                    cv2.waitKey()
                elif order == 's':
                    size = int(input("input the size"))
                    tmpimg = showimg[:size, :, :]
                    h, w, _ = tmpimg.shape
                    cv2.putText(tmpimg, str(h) + '  ' + str(w), (0,0), cv2.FONT_HERSHEY_SIMPLEX)
                    cv2.imshow("tmp", tmpimg)
                    cv2.waitKey()
                elif order == 'a':
                    size = int(input("input the size"))
                    tmpimg = showimg[:, size:, :]
                    h, w, _ = tmpimg.shape
                    cv2.putText(tmpimg, str(h) + '  ' + str(w), (0,0), cv2.FONT_HERSHEY_SIMPLEX)
                    cv2.imshow("tmp", tmpimg)
                    cv2.waitKey()
                elif order == 'd':
                    size = int(input("input the size"))
                    tmpimg = showimg[:, :size, :]
                    h, w, _ = tmpimg.shape
                    cv2.putText(tmpimg, str(h) + '  ' + str(w), (0,0))
                    cv2.imshow("tmp", tmpimg)
                    cv2.waitKey()






if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--imgpath', type=str, default='.')
    parser.add_argument('--xmlpath', type=str, default='.')
    parser.add_argument('--newimgpath', type=str, default='.')
    parser.add_argument('--newxmlpath', type=str, default='.')
    args = parser.parse_args()
    CropImgAndFixXML(args.imgpath, args.xmlpath, args.newimgpath, args.newxmlpath)