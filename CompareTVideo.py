import argparse
import os
import sys
import glob
import cv2
import numpy as np

def CompareTVideo(path1, path2):
    files1list = glob.glob(path1+'*.jpg')
    files1list = sorted(files1list)
    for file1 in files1list:
        basename = os.path.basename(file1)
        file2 = os.path.join(path2, basename)
        if os.path.exists(file2):
            img1 = cv2.imread(file1)
            img2 = cv2.imread(file2)
            res = np.concatenate([img1, img2], axis=1)
            cv2.imshow("res", res)
            cv2.waitKey()

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--path1', type=str, default="")
    parser.add_argument('--path2', type=str, default="")
    args = parser.parse_args()
    CompareTVideo(args.path1, args.path2)