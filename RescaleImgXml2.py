import glob
import sys
from PIL import Image
import os

newxmlpath = "newxml"
newimgpath = "newimg"

xmlfiles = glob.glob("images/*.xml")
#print(xmlfiles)
for xmlfile in xmlfiles:
    res = ""
    with open(xmlfile) as fp:
        print(xmlfile)
        basename = os.path.basename(xmlfile)
        with open(os.path.join(newxmlpath, basename),'a') as wfp:
            scale = 1
            imgwStr = ""
            imghStr = ""
            imgwInt = 0
            imghInt = 0
            for line in fp.readlines():
                #print(line[0],"--",line[1],"--",line[2],"--",line[3],"--",line[4],"--",line[5])
                if line.find('width') > -1:
                    #print(line)
                    imgwStr = line[9:-9]
                    #print(imgwStr)
                    imgwInt = int(imgwStr)
                    #print(imgwInt)
                    tmpWidLine = line
                elif line.find('height') > -1:
                    imghStr = line[10:-10]
                    imghInt = int(imghStr)
                    #print(imghInt)
                    maxwh = max(imgwInt,imghInt)

                    while(maxwh > 1000):
                        scale *= 2
                        maxwh /= 2
                    
                    neww = round(imgwInt/scale)
                    newh = round(imghInt/scale)

                    wfp.writelines(tmpWidLine.replace(imgwStr,str(neww)))
                    wfp.writelines(line.replace(imghStr, str(newh)))

                elif line.find("xmin") > -1 or line.find("ymin") > -1 or line.find("xmax") > -1 or line.find("ymax") > -1: 
                    #print(line)  
                    #print(line[-1])
                    tmpNumStr = line[9:-8]
                    #print(tmpNumStr)
                    tmpNumInt = round(int(tmpNumStr)/scale)
                    #print(tmpNumInt)
                    wfp.writelines(line.replace(tmpNumStr, str(tmpNumInt)))

                else:
                    wfp.writelines(line)      
            CoImgPath = os.path.join('images',basename[:-4]+".jpg")
            if not os.path.exists(CoImgPath):
                CoImgPath = os.path.join('images',basename[:-4]+".JPG")
            im = Image.open(CoImgPath)
            im = im.resize((neww, newh), Image.ANTIALIAS)
            im.save(os.path.join(newimgpath,os.path.basename(CoImgPath)), quality=95)
    
    #input()