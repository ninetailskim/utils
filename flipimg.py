import argparse
import cv2
import glob


def Flip(imgpath):
    imgfiles = glob.glob(imgpath+'/*.jpg')
    for imgfile in imgfiles:
        print(imgfile)
        img = cv2.imread(imgfile)
        img = cv2.flip(img, 0, dst=None)
        cv2.imwrite(imgfile, img)





if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--imgpath', type=str, default='.')
    args = parser.parse_args()
    Flip(args.imgpath)