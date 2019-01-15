#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan  7 01:27:12 2019

@author: sachin_sharma
"""


import os
import shutil
import glob
import argparse

# autoamtion
def parse_args():
    parser = argparse.ArgumentParser(description='Copying files and renaming them')
    parser.add_argument('-sp', '--source_dir', type=str, required=True, help='Path to the souce directory')
    parser.add_argument('-dp', '--dest_dir', type=str, required=True, help='Path to your destination folder')
    return parser

#dest_dir = '/home/sachin_sharma/Desktop/jpg_data/buildup'
#source_dir ='/home/sachin_sharma/Desktop/euro_patch_test'

# Copying files
def cpy_files(path):
    for dirpath, dirnames, filenames in os.walk(path):
    #print('Current path: ', dirpath)
    #print('Directories: ', dirnames)
    #print('Files: ', filenames)
    #print(dirpath)
       os.chdir(dirpath)
       print('Copying files from Current directory: ' +dirpath + ' to Destination: '+args.dest_dir)
       for file in glob.glob("*.tif"):
           shutil.copy(file, args.dest_dir)

if __name__ == "__main__":
    parser = parse_args()
    args = parser.parse_args()
    
           
# copying
cpy_files(args.source_dir)

#  Renaming all files with Else

def rename_files(des_path):
    os.chdir(des_path)
    c = 0
    for files in glob.glob("*.tif"):
        c = c + 1
        basename, ext = os.path.splitext(files)
        os.rename('{}.tif'.format(basename), '{}.tif'.format('Else_'+str(c)))
    return None

# call
rename_files(args.dest_dir)
