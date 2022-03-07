import glob
import shutil
import os
import argparse



def pickImageFromTxt(args):
    txtpath = glob.glob(args.txt+"/*.txt")
    print(txtpath)
    
    if args.newimgpath:
        os.makedirs(args.newimgpath,exist_ok=True)

    for xp in txtpath:
        basename = os.path.basename(xp)
        filename, ext = os.path.splitext(basename)
        if filename == 'classes':
            continue
        
        shutil.copyfile(os.path.join(args.oldimgpath, filename+'.png'),
                         os.path.join(args.newimgpath, filename+'.png'))


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--oldimgpath', type=str, required=True)
    parser.add_argument('--newimgpath', type=str, required=True, default=None)
    parser.add_argument('--txt', type=str, required=True)
    args = parser.parse_args()
    pickImageFromTxt(args)
