import glob
import argparse
import random
import shutil
import os


def split_data(dataPath, ratio):
    imglist = glob.glob(dataPath + '/*.png') + glob.glob(dataPath + '/*.jpg')
    print(imglist)
    random.shuffle(imglist)

    splitindex = round(len(imglist) * (ratio / 100))

    trainPath = os.path.join(dataPath, 'train')
    if not os.path.exists(trainPath):
        os.makedirs(trainPath)

    for img in imglist[:splitindex]:
        basename = os.path.basename(img)
        newpath = os.path.join(trainPath,basename)
        shutil.copyfile(img, newpath)

    testPath = os.path.join(dataPath, 'test')
    if not os.path.exists(testPath):
        os.makedirs(testPath)

    for img in imglist[splitindex:]:
        basename = os.path.basename(img)
        newpath = os.path.join(testPath,basename)
        shutil.copyfile(img, newpath)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--dataPath", type=str, required=True)
    parser.add_argument("--ratio", type=int)
    args = parser.parse_args()

    split_data(args.dataPath, args.ratio)