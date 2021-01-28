import argparse
import os
import glob
import xml.etree.ElementTree as ET

def VOC2YOLO(xmlPath):
    xmlfiles = glob.glob(xmlPath+"/*.xml")
    for xmlfile in xmlfiles:
        



if __name__ == '__main__':
    paser = argparse.ArgumentParser()
    paser.add_argument("--xmlPath", type=str, required=True)
    args = paser.parse_args()
    VOC2YOLO(args.xmlPath)
