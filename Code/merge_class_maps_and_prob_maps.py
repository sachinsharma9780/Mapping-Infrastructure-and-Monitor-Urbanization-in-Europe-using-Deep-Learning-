#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar  8 15:19:49 2019

@author: sachin_sharma
"""

import subprocess
import os
import argparse
import glob

def parse_args():
    parser = argparse.ArgumentParser(description="Merge class maps")
    parser.add_argument('-f', '--file', type=str, required=True, help='Path to your tiff files for retriving their names')
    parser.add_argument('-p', '--path', type=str, required=True, help='Path to your georef imgs for merge')
    return parser

if __name__ == "__main__":
    parser = parse_args()
    args = parser.parse_args()
           
# read filenames
fileNames =[]
def file_names(path):
    os.chdir(path)
    for file in glob.glob("*.tif"):
        basename, ext = os.path.splitext(file)
        #print(basename)
        fileNames.append(basename)

# call
#path = ''/home/sachin_sharma/Desktop/Test_cities''
#file_names('/home/sachin_sharma/Desktop/Test_cities')
file_names(args.file)
fileNames.sort()

# getting paths of georef imgs
paths_class = []
paths_prob = []
def get_path(path):
    for file in fileNames:
        dirpath = os.path.join(path, file)
        dirpath_1 = os.path.join(dirpath, 'georef_class_maps')
        dirpath_2 = os.path.join(dirpath, 'georef_prob')
        paths_class.append(dirpath_1)
        paths_prob.append(dirpath_2)
        
# path =''/home/sachin_sharma/Desktop/exp1a1_results''
#get_path('/home/sachin_sharma/Desktop/exp1a1_results')
get_path(args.path)
paths_class.sort()
paths_prob.sort()

def merge_class_heatmaps(path, f):
    os.chdir(path)
    print("Merging class maps based on Softmax prediction on City: ", f)
    print('Current path :', path)
    subprocess.call(r'find . -name "*.tif" > a.txt', shell=True)
    subprocess.call(r'gdalbuildvrt mosaic.vrt -input_file_list a.txt', shell=True)
    subprocess.call(r'gdal_translate -of GTiff -co COMPRESS=JPEG -co PHOTOMETRIC=RGB mosaic.vrt {}.tif'.format(f+'_class'), shell=True)

def merge_prob_heatmaps(path, f):
    os.chdir(path)
    print("Merging Probability maps based on Softmax predictions on City: ", f)
    print('Current path :', path)
    subprocess.call(r'find . -name "*.tif" > a.txt', shell=True)
    subprocess.call(r'gdalbuildvrt mosaic.vrt -input_file_list a.txt', shell=True)
    subprocess.call(r'gdal_translate -of GTiff -co COMPRESS=JPEG -co PHOTOMETRIC=RGB mosaic.vrt {}.tif'.format(f+'_prob'), shell=True)

for p,f in zip(paths_class, fileNames):
    merge_class_heatmaps(p, f) 

for p,f in zip(paths_prob, fileNames):
    merge_prob_heatmaps(p, f)























