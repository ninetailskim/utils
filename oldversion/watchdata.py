import cv2
import os
import argparse
import matplotlib.pyplot as plt
import glob




def main():

    parser = argparse.ArgumentParser()
    parser.add_argument('--input')
    args = parser.parse_args()

    inputs = args.input
    print(inputs)
    d = inputs.split('\\')[-1]
    print(d)
    gt = os.path.join('GT', d,'GT')
    blur = os.path.join('GT', d,'input')
    dvdres = os.path.join('DVDresult', d)
    blend = os.path.join('Inference', d)

    images = glob.glob(os.path.join(args.input,'*.jpg'))
    if len(images) == 0:
        images = glob.glob(os.path.join(args.input,'*.png'))

    for image in images:
        idx = image.split('\\')[-1].split('.')[0]
        print(idx)
        GTpath = os.path.join(gt, idx+'.jpg')
        print(GTpath)
        Bpath = os.path.join(blur, idx+'.jpg')
        print(Bpath)
        #print(int(idx)+1)
        Dvdpath = os.path.join(dvdres, '%05d.jpg' %(int(idx)+1))
        print(Dvdpath)
        blendpath = os.path.join(blend, '%05d.png' %(int(idx)+1))
        print(blendpath)
        
        GT = cv2.imread(GTpath)
        B = cv2.imread(Bpath)
        D = cv2.imread(Dvdpath)
        Blend = cv2.imread(blendpath)
        My = cv2.imread(image)

        H, W, _ = My.shape
        My = My[:H, :W, :]
        GT = GT[:H, :W, :]
        B = B[:H, :W, :]
        Blend = Blend[:H, :W, :]
        D = D[:H, :W, :]

        fig = plt.figure()
        fig.add_subplot(1,1,1)
        plt.imshow(GT)
        fig.add_subplot(2,1,2)
        plt.imshow(B)
        fig.add_subplot(3,2,1)
        plt.imshow(Blend)
        fig.add_subplot(4,2,2)
        plt.imshow(My)
        plt.show()

        '''
        cv2.imshow('output', My)
        cv2.imshow('GT',GT)
        cv2.imshow('OR',B)
        cv2.imshow('D',D)
        cv2.imshow('blend',Blend)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        '''

if __name__ == '__main__':
    main()
