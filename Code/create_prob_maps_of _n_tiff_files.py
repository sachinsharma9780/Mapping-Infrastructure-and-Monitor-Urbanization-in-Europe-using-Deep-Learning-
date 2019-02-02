#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 27 15:57:53 2019

@author: sachin_sharma
"""

import subprocess
import cv2
import numpy as np
import argparse
import os, glob
import errno
from matplotlib import pyplot as plt
from matplotlib import colors
from matplotlib import cm as cmx


def parse_args():
    parser = argparse.ArgumentParser(description="Create Probability patches based on Softmax Predictions")
    parser.add_argument('-f', '--file', type=str, required=True, help='Path to your big tif images')
    parser.add_argument('-out', '--outputDirectory', type=str, required=True, help='Path to the output which will contain prob patches')
    parser.add_argument('-in', '--inputDirectory', type=str, required=True, help='Path to cropped tif imgs')
    parser.add_argument('-n','--nworkers', type=int, default=None, help='Number of workers (by default none)')
    parser.add_argument('-m', '--model', type=str, required=True, help='Path to your pretrained model')
    return parser


# main
if __name__ == "__main__":
    parser = parse_args()
	
    args = parser.parse_args()
    print(args)

""" Creating 64*64 img patches and coloring them based on softmax probability predictions """

# read filenames
fileNames =[]
def file_names(path):
    os.chdir(path)
    for file in glob.glob("*.tif"):
        basename, ext = os.path.splitext(file)
        #print(basename)
        fileNames.append(basename)

# call
#path = '/home/sachin_sharma/Desktop/Test_cities'
#file_names(path)
file_names(args.file)
fileNames.sort()
 
# getting input paths of cropped imgs
cropimgs = []

def crop_path(path):
    for file in fileNames:
        dirpath = os.path.join(path, file)
        cropimgs.append(dirpath)
        
        
#crop_path('/home/sachin_sharma/Desktop/cropped_imgs')
crop_path(args.inputDirectory)
#cropimgs = cropimgs[1:]
cropimgs.sort()
#print(cropimgs)


# getting output paths to store prob patches for probability heatmaps
outputpath = []
def out_path(path):
     for file in fileNames:
         dirpath = os.path.join(path, file)
         dirpath = os.path.join(dirpath, 'prob_maps')
         outputpath.append(dirpath)

# call         
#out_path('/home/sachin_sharma/Desktop/exp1a1.1_results')
out_path(args.outputDirectory)
#outputpath = outputpath[1:]
outputpath.sort()
#print(outputpath)
  
# importing pretrained wts 
path_wts = os.path.dirname(args.model)
path_wts = str(path_wts)
os.chdir(path_wts)
from keras.models import load_model
wts = os.path.basename(args.model)
print('Wts are '+wts)
model = load_model('{}'.format(wts))

# Fitting the CNN to the images(Image Augmentation, Image Preprocessing)
from keras.preprocessing.image import ImageDataGenerator
train_datagen = ImageDataGenerator(  
        rescale=1./255,
        shear_range=0.2,             
        zoom_range=0.2,              
        horizontal_flip=True)


# Normalizing the test set
test_datagen = ImageDataGenerator(rescale=1./255)


# Function to return color values based on probabilities
def color_values(prob):
    jet = plt.get_cmap('jet')
    cnorm = colors.Normalize(vmin=0, vmax=1)    
    scalarMap = cmx.ScalarMappable(norm=cnorm, cmap=jet)
    b = scalarMap.to_rgba(prob)
    print("prob is: ", prob)
    return b    

# Making predictions on new Cropped tif images obtained from 10000*10000 tiff image
# Create a generator for prediction
def creates_prob_patch(inp_path, out_path):
    print('I/p direc is: ' +inp_path)
    print('O/p direc is: ' +out_path)
    test_set_gen = test_datagen.flow_from_directory(
        inp_path,
        target_size=(64,64),
        batch_size=50,
        class_mode=None, # only data, no labels
        shuffle=False)
    fnames = test_set_gen.filenames
    len_f = len(fnames) 
    predictions = model.predict_generator(test_set_gen, verbose=1)
    predicted_classes = np.argmax(predictions,axis=1)
    max_probs = []
    for i in range(0,len_f):
        max_probs.append(max(predictions[i]))
    os.chdir(out_path)
    #os.makedirs('prob_maps')
    for f, p in zip(fnames, max_probs):
    #print(f, p)
       color = color_values(p)
       img = np.ones((64,64,3))*255
       img = img.astype(int)
       img[:,:,0] = (img[:,:,0]*color[0]).astype(int)
       img[:,:,1] = (img[:,:,1]*color[1]).astype(int)
       img[:,:,2] = (img[:,:,2]*color[2]).astype(int)
       image_name = f.split("/")[1]
       cv2.imwrite("{}".format(os.path.join(out_path, image_name)), img)

# call prob_patch
for img_path, out_path2 in zip(cropimgs, outputpath):
    creates_prob_patch(img_path, out_path2)