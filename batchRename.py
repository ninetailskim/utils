import argparse
import os
import sys
import glob

def main(args):
    sindex = args.sindex
    # filenames = os.listdir(args.tpath)
    # for name in filenames:
    #     postfix = name.split('/')[-1].split('.')[-1]
    #     newname = args.prefix + '_' + str(sindex) + '.' + postfix
    #     os.renames(os.path.join(args.tpath, name), os.path.join(args.tpath, newname))
    #     sindex += 1

    for fpath, dirs, fs in os.walk(args.tpath):
        for file in fs:
            if file.split('.')[0] != '':
                postfix = file.split('.')[-1]
                newname = args.prefix + '_' + str(sindex) + '.' + postfix
                os.renames(os.path.join(fpath, file), os.path.join(fpath, newname))
                sindex += 1

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--prefix',type=str, default="")
    parser.add_argument('--sindex', type=int, default=0)
    parser.add_argument('--tpath', type=str, required=True)
    args = parser.parse_args()
    main(args)