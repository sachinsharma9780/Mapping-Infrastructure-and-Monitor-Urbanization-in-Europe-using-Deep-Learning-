#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 14 23:18:33 2019

@author: sachin_sharma
"""

import subprocess
import os
import argparse
import glob

def parse_args():
    parser = argparse.ArgumentParser(description='Copying files and renaming them')
    parser.add_argument('-sp', '--source_dir', type=str, required=True, help='Path to the souce directory where heatmaps are')
    parser.add_argument('-dp', '--destn_path', type=str, required=True, help='Destination path to store results')
    parser.add_argument('-f', '--file', type=str, required=True, help='fileNames')
    return parser

if __name__ == "__main__":
    parser = parse_args()
    args = parser.parse_args()

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
    
def mv_class_heatmaps(inp_path):
    os.chdir(inp_path)
    subprocess.call(r'mv *_class.tif {}'.format(args.destn_path), shell=True)

def mv_prob_heatmaps(inp_path):
    os.chdir(inp_path)
    subprocess.call(r'mv *_prob.tif {}'.format(args.destn_path), shell=True)

def get_paths(path):
    for f in fileNames:
        print('Current City is:', f)
        dirpath = os.path.join(path, f)
        dirpath_1 = os.path.join(dirpath, 'georef_class_maps')
        dirpath_2 = os.path.join(dirpath, 'georef_prob')
        mv_class_heatmaps(dirpath_1)
        mv_prob_heatmaps(dirpath_2)

# call
# path ='/home/sachin_sharma/Desktop/exp1a1_results'
get_paths(args.source_dir)

#print('hi {}'.format('/home/sachin_sharma/Desktop/Visln_results'))