import glob
import argparse
import random
import shutil
import os


def split_data(dataPath, annoPath, ratio):
    imglist = glob.glob(dataPath + '/*.png') + glob.glob(dataPath + '/*.jpg')
    print(imglist)
    random.shuffle(imglist)

    splitindex = round(len(imglist) * (ratio / 100))

    trainPath = os.path.join(dataPath, 'train')
    trainAnnoPath = os.path.join(annoPath, 'train')
    if not os.path.exists(trainPath):
        os.makedirs(trainPath)
    if not os.path.exists(trainAnnoPath):
        os.makedirs(trainAnnoPath)

    for img in imglist[:splitindex]:
        basename = os.path.basename(img)
        filename, ext = os.path.splitext(basename)
        newpath = os.path.join(trainPath, basename)
        oriannopath = os.path.join(annoPath,filename+'.txt')
        tarannopath = os.path.join(trainAnnoPath,filename+'.txt')
        shutil.copyfile(img, newpath)
        shutil.copyfile(oriannopath, tarannopath)

    testPath = os.path.join(dataPath, 'test')
    testAnnoPath = os.path.join(annoPath, 'test')
    if not os.path.exists(testPath):
        os.makedirs(testPath)
    if not os.path.exists(testAnnoPath):
        os.makedirs(testAnnoPath)

    for img in imglist[splitindex:]:
        basename = os.path.basename(img)
        filename, ext = os.path.splitext(basename)
        newpath = os.path.join(testPath,basename)
        oriannopath = os.path.join(annoPath,filename+'.txt')
        tarannopath = os.path.join(testAnnoPath,filename+'.txt')
        shutil.copyfile(img, newpath)
        shutil.copyfile(oriannopath, tarannopath)



if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--dataPath", type=str, required=True)
    parser.add_argument("--annoPath", type=str, required=True)
    parser.add_argument("--ratio", type=int)
    args = parser.parse_args()

    split_data(args.dataPath, args.annoPath, args.ratio)