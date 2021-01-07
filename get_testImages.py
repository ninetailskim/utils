from PIL import Image
import os.path
import glob

annotations_test_dir = "annotations/validation/"
Images_dir = "images"
test_images_dir = "val_images"
i = 0
for xmlfile in os.listdir(annotations_test_dir):
    (filepath, tempfilename) = os.path.split(xmlfile)
    (shotname, extension) = os.path.splitext(tempfilename)
    xmlname = shotname
    for pngfile in os.listdir(Images_dir):
        (filepath, tempfilename) = os.path.split(pngfile)
        (pngname, extension) = os.path.splitext(tempfilename)
        if pngname == xmlname:
             try:   
                img = Image.open(Images_dir+"/" + pngname + ".jpg")
             except:
                img = Image.open(Images_dir+"/" + pngname + ".JPG")     
             img.save(os.path.join(test_images_dir, os.path.basename(pngfile)))
             print(pngname)
             i += 1
print(i)