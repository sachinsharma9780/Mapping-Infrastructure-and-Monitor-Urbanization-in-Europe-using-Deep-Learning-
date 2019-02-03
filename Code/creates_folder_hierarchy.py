#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 19 20:30:43 2019

@author: sachin_sharma
"""
# necessary libraries
import os
import glob
import argparse

# automation
def parse_args():
    parser = argparse.ArgumentParser(description= "Create Hierarchy of folders with names of satellite images ")
    parser.add_argument('-si', '--pathimgs', type=str, required=True, help='path to folder containing satellite imgs')
    parser.add_argument('-p', '--Directory', type=str, required=True, help='path to create hierarchy of folders with city names')
    return parser

# main
if __name__ == "__main__":
    parser = parse_args()
    args = parser.parse_args() 


# read file names of satellite images from given path
fileNames =[]
def file_names(path):
    os.chdir(path)
    for file in glob.glob("*.tif"):
        basename, ext = os.path.splitext(file)
        #print(basename)
        fileNames.append(basename)

# call
file_names(args.pathimgs)
fileNames.sort()
print(fileNames)


# lets make folders
# path to make folders of cities
os.chdir(args.Directory)

def make_folder(path):
    os.makedirs(path)
    os.makedirs(os.path.join(path, 'class_maps'))
    #os.makedirs(os.path.join(path, 'cropped_imgs'))
    os.makedirs(os.path.join(path, 'georef_class_maps'))
    os.makedirs(os.path.join(path, 'georef_prob'))
    os.makedirs(os.path.join(path, 'prob_maps'))

for f in fileNames:
    make_folder(os.path.join(args.Directory, str(f)))