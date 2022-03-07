import glob
import shutil
import os
import argparse



def pickImageFromTxt(args):
    if args.newimgpath:
        os.makedirs(args.newimgpath,exist_ok=True)
    
    dirname = os.path.dirname(args.txt)
    print(args)
    with open(args.txt, "r") as fp:
        lines = fp.readlines()
        print(lines)
        for line in lines:
            filename = line.split(" ")[0]
            filepath = os.path.join(dirname, filename)

            basename = os.path.basename(filename)

            print(filepath)
            print(os.path.join(args.newimgpath, basename))
            shutil.copyfile(filepath,
                         os.path.join(args.newimgpath, basename))


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--newimgpath', type=str, required=True, default=None)
    parser.add_argument('--txt', type=str, required=True)
    args = parser.parse_args()
    pickImageFromTxt(args)
