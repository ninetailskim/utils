import os
import argparse
import glob
import cv2


if __name__ == '__main__':

    parse = argparse.ArgumentParser()
    parse.add_argument('--input')

    args = parse.parse_args()

    idir = args.input

    for seq in ['IMG_0003', "720p_240fps_2", "IMG_0021", "IMG_0030", "IMG_0031", "IMG_0032", "IMG_0033", "IMG_0037", "IMG_0039"]:
        print(seq)
        for i in range(-2,3):
            output = 'data/'+ seq +'/image_'
            odir = output + str(i)
            if not os.path.isdir(odir):
                os.makedirs(odir)
        
        imgs = sorted(glob.glob(os.path.join(args.input, seq, 'input/*.jpg')))
        

        for ind,img in enumerate(imgs):
            print(ind)
            pic = cv2.imread(img)
            for i in range(-2, 3):
                output = 'data/'+ seq +'/image_'
                odir = output + str(i)
                cv2.imwrite(os.path.join(odir, "%05d.jpg" %(min(99, max(ind-i, 0)))), pic)
            if ind == 0:
                output = 'data/'+ seq +'/image_'
                cv2.imwrite(os.path.join(output + "-1", "00000.jpg"), pic)
                cv2.imwrite(os.path.join(output + "-2", "00000.jpg"), pic)
                cv2.imwrite(os.path.join(output + "-2", "00001.jpg"), pic)
            if ind == 99:
                output = 'data/'+ seq +'/image_'
                cv2.imwrite(os.path.join(output + "1", "00099.jpg"), pic)
                cv2.imwrite(os.path.join(output + "2", "00099.jpg"), pic)
                cv2.imwrite(os.path.join(output + "2", "00098.jpg"), pic)
                
