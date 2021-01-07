import argparse
import os
import sys
import glob
import cv2

def main(args):
    for fpath, dirs, fs in os.walk(args.tpath):
        for file in fs:
            if file.split('.')[0] != '':
                oldname = os.path.join(fpath, file)
                img = cv2.imread(oldname)
                shape = img.shape
                maxlen = max(shape[0],shape[1])
                ratio = maxlen / args.maxlen
                shape0 = shape[0] / ratio
                shape1 = shape[1] / ratio
                img = cv2.resize(img, (round(shape1), round(shape0)))
                newfile = file.split('.')[0]+'.png'
                cv2.imwrite(os.path.join(fpath, newfile), img)



if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--tpath', type=str, required=True)
    parser.add_argument('--maxlen', type=int, default=1000)
    args = parser.parse_args()
    print(args)
    print(type(args))
    print(args.Namespace)
    input()
    main(args)