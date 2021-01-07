# coding=utf-8
import argparse
import os
import sys
import glob
import cv2
import shutil

def main(args):

    ename = ['bedroom','kitchen','livingroom','bathroom']

    for fpath, dirs, fs in os.walk(args.tpath):
        for file in fs:
            if file.split('.')[0] != '':
                #print(file)
                _, ext = os.path.splitext(file)
                print(file)
                print(ext)
                if ext == '.png':
                    for index, i in enumerate(['卧室','厨房','客厅','卫生间']):
                        #print(fpath)
                        if fpath.find(i) != -1:
                            shutil.copyfile(os.path.join(fpath, file), os.path.join(os.path.join('../indoor_e',ename[index]),file))
                            break



if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--tpath', type=str, required=True)
    parser.add_argument('--maxlen', type=int, default=1000)
    args = parser.parse_args()
    main(args)