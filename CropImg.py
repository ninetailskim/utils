'''python CropImgAndFixXML.py 
--imgpath=D:\exp\images 
--xmlpath=D:\exp\merged_xml 
--newimgpath=D:\exp\images2 
--newxmlpath=D:\exp\merged_xml2
'''
import argparse
import os
import cv2
import glob
import copy
import shutil

def makepath(path):
    if not os.path.exists(path):
        os.makedirs(path)


def CropImg(imgpath, newimgpath):

    tmpath = os.path.join(newimgpath,'tmp')

    makepath(newimgpath)
    makepath(tmpath)

    imglist = glob.glob(os.path.join(imgpath, '*.jpg'))
    imglist = sorted(imglist)
    index = 0
    for imgfile in imglist:
        print(index,' / ', len(imglist))
        index += 1
        basename = os.path.basename(imgfile)
        file, ext = os.path.splitext(basename)

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
            if order == '9':
                break

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

        if order == '9':
            shutil.move(imgfile, os.path.join(tmpath, basename))
            cv2.destroyAllWindows()
            continue

        fn, ext = os.path.splitext(basename)

        newimgfile = os.path.join(newimgpath, fn+'.png')
        cv2.imwrite(newimgfile, img[wsize:oh-ssize,asize:ow-dsize,:]) 

        shutil.move(imgfile, os.path.join(tmpath, basename))

        cv2.destroyAllWindows()


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--imgpath', type=str, default='.')
    parser.add_argument('--newimgpath', type=str, default='.')
    args = parser.parse_args()
    CropImg(args.imgpath, args.newimgpath)