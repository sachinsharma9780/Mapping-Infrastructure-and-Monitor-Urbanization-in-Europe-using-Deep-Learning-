#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan  1 14:42:24 2019

@author: sachin
"""
# Deleting black images from folder

import glob
import os 
import numpy as np
import cv2
import argparse

# Automation
def parse_args():
    parser = argparse.ArgumentParser(description="Deleting black images")
    parser.add_argument('-path', '--inputDirectory', type=str, required=True, help='Path to folder containing black images')
    return parser
    


def del_black_imgs(path):
    for file in glob.glob("*.tif"):
        #print(file)
        img = cv2.imread("{}".format(file))
        if np.argmax(img) == 0:
            print("Deleting Black Image ", file)
            os.remove(file)
        else:
            print("Non Black Image", file)
        
if __name__ == "__main__":
    parser = parse_args()
    args = parser.parse_args()
    os.chdir(args.inputDirectory)
        
        
del_black_imgs(args.inputDirectory)    
