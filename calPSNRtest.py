from skimage.measure import compare_ssim as ssim
from skimage.measure import compare_psnr as psnr
import argparse
import glob
import os
import cv2




if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', help='sample output dir')
    parser.add_argument('--size', help='sample output dir', default=False)
    args = parser.parse_args()

    outfilename = os.path.join(args.input, 'result.txt')
    fo = open(outfilename,'w+')

    list_files = os.walk(args.input)
    dirPSNR = 0
    dirSSIM = 0
    for root, dirs, files in list_files:
        for d in dirs:
            temppath = os.path.join(root, d)
            tempimages = glob.glob(os.path.join(temppath, '*.png'))
            if len(tempimages) == 0:
                tempimages = glob.glob(os.path.join(temppath, '*.jpg'))
            sencePSNR = 0
            senceSSIM = 0
            senceGTPSNR = 0
            senceGTSSIM = 0
            fsence = open(os.path.join(args.input, d, 'sence.txt'), 'w+')
            index = 0
            idx = [5,8,11,15,18,21,24,28,31,34,38,41,44,47,51,54,57,60,64,67,70,74,77,80,83,87,90,93,97]
            images = []
            for image in tempimages:
                if int(int(image.split('\\')[-1].split('.')[0])) in idx:
                    images.append(image)
            print(len(images))
            for image in images:
                
                GTpath = os.path.join('GT', d,'GT','%05d' %(int(image.split('\\')[-1].split('.')[0])) +'.jpg')
                Bpath = os.path.join('GT', d,'input','%05d' %(int(image.split('\\')[-1].split('.')[0])) +'.jpg')
                print(image)
                print(GTpath)
                #print(Bpath)

                out = cv2.imread(image)
                H, W, C = out.shape
                
                #print(H,W,C)

                if args.size:
                    if H == 720:
                        H = 704
                        W = 1280
                    else:
                        H = 1280
                        W = 704
                out = out[:H, :W, :]
                GT = cv2.imread(GTpath)[:H, :W, :]

                OR = cv2.imread(Bpath)[:H, :W, :]
                #print(out.shape, GT.shape, OR.shape)

                tempPSNR = psnr(out, GT)
                tempSSIM = ssim(out, GT, multichannel=True)
                oPSNR = psnr(OR, GT)
                oSSIM = ssim(OR, GT, multichannel=True)
                #print('output', tempPSNR, tempSSIM)
                #print('input', oPSNR, oSSIM)
                fsence.write(str(index)+':'+image + '  psnr:' + str(oPSNR) +'/'+str(tempPSNR) + '/'+ str(tempPSNR - oPSNR) +'  ssim:' + str(oSSIM)+'/'+str(tempSSIM)+ '/'+ str(tempSSIM - oSSIM) + '\n')
                fsence.flush()
                '''
                cv2.imshow('output', out)
                cv2.imshow('GT',GT)
                cv2.imshow('OR',OR)
                cv2.waitKey(0)
                cv2.destroyAllWindows()
                '''
                sencePSNR += tempPSNR
                senceSSIM += tempSSIM
                senceGTPSNR += oPSNR
                senceGTSSIM += oSSIM
                print(index)
                index+=1
            #print(index)
            fsence.write('average:  psnr:' +str(senceGTPSNR/index)+'/'+str(sencePSNR/index) + '   ssim:' + str(senceGTSSIM/index)+'/'+str(senceSSIM/index)+ '\n')
            fsence.flush()
            fsence.close()
            dirPSNR += sencePSNR/index
            dirSSIM += senceSSIM/index
    fo.write('average:      psnr:' + str(dirPSNR/10) + '       ssim:' + str(dirSSIM/10)+ '\n')    
    fo.close()