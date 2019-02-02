#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 25 17:32:58 2019

@author: sachin_sharma
"""
# libraries
import argparse
import os, glob
import subprocess
import numpy as np
from matplotlib import pyplot as plt
from matplotlib import colors
from matplotlib import cm as cmx
import cv2

# Command line args  
def parse_args():
    parser = argparse.ArgumentParser(description="create class maps")
    parser.add_argument('-m', '--model', type=str, required=True, help='Path to your pretrained model')
    parser.add_argument('-out', '--outputDirectory', type=str, required=True, help='path to store class maps')
    parser.add_argument('-inp', '--inputDirectory', type=str, required=True, help='path where cropped images are')
    parser.add_argument('-f', '--file', type=str, required=True, help='path to get the names of tif file')
    return parser

if __name__ == "__main__":
    parser = parse_args()
    args = parser.parse_args()
    
    


# importing pretrained wts 
path_wts = os.path.dirname(args.model)
path_wts = str(path_wts)
os.chdir(path_wts)
from keras.models import load_model
wts = os.path.basename(args.model)
print('Wts are '+wts)
model = load_model('{}'.format(wts))
#model = load_model('ci_a_1.h5')

# Fitting the CNN to the images(Image Augmentation, Image Preprocessing)
from keras.preprocessing.image import ImageDataGenerator
train_datagen = ImageDataGenerator(  
        rescale=1./255,
        shear_range=0.2,             
        zoom_range=0.2,              
        horizontal_flip=True)


# Normalizing the test set
test_datagen = ImageDataGenerator(rescale=1./255)

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

# getting output paths to store class maps
outpath = []
def output_path(path):
    for file in fileNames:
        dirpath = os.path.join(path, file)
        dirpath = os.path.join(dirpath, 'class_maps')
        outpath.append(dirpath)

#call
#output_path('/home/sachin_sharma/Desktop/exp1a1_results')
output_path(args.outputDirectory)
outpath.sort()

# getting input path of cropped tif imgs
inpath = []
def inp_path(path):
    for file in fileNames:
        dirpath = os.path.join(path, file)
        inpath.append(dirpath)


#inp_path('/home/sachin_sharma/Desktop/cropped_imgs')
inp_path(args.inputDirectory)

# Function to return color values based on probabilities
def color_values(prob):
    jet = plt.get_cmap('jet')
    cnorm = colors.Normalize(vmin=0, vmax=1)    
    scalarMap = cmx.ScalarMappable(norm=cnorm, cmap=jet)
    b = scalarMap.to_rgba(prob)
    print("prob", prob)
    return b

# Creating a Heatmap of 10 different classes given 10 different colors
def class_maps(class_pred, f, outpath):
    os.chdir(outpath)
    if class_pred == 0:
       color = color_values(0.4)
       class_img = np.ones((64,64,3))*255
       class_img[:,:,0] = (class_img[:,:,0]*color[0]).astype(int)
       class_img[:,:,1] = (class_img[:,:,1]*color[1]).astype(int)
       class_img[:,:,2] = (class_img[:,:,2]*color[2]).astype(int)
       image_name_1 = f.split("/")[1]
       cv2.imwrite("{}".format(image_name_1) ,class_img)
    elif class_pred == 1:
         color = color_values(0.5)
         class_img = np.ones((64,64,3))*255
         class_img[:,:,0] = (class_img[:,:,0]*color[0]).astype(int)
         class_img[:,:,1] = (class_img[:,:,1]*color[1]).astype(int)
         class_img[:,:,2] = (class_img[:,:,2]*color[2]).astype(int)
         image_name_1 = f.split("/")[1]
         cv2.imwrite("{}".format(image_name_1) ,class_img)
    elif class_pred == 2:
         color = color_values(0.3)
         class_img = np.ones((64,64,3))*255
         class_img[:,:,0] = (class_img[:,:,0]*color[0]).astype(int)
         class_img[:,:,1] = (class_img[:,:,1]*color[1]).astype(int)
         class_img[:,:,2] = (class_img[:,:,2]*color[2]).astype(int)
         image_name_1 = f.split("/")[1]
         cv2.imwrite("{}".format(image_name_1) ,class_img)  
    elif class_pred ==3:
         color = color_values(0.9)
         class_img = np.ones((64,64,3))*255
         class_img[:,:,0] = (class_img[:,:,0]*color[0]).astype(int)
         class_img[:,:,1] = (class_img[:,:,1]*color[1]).astype(int)
         class_img[:,:,2] = (class_img[:,:,2]*color[2]).astype(int)
         image_name_1 = f.split("/")[1]
         cv2.imwrite("{}".format(image_name_1) ,class_img)
    elif class_pred == 4:
         color = color_values(0)
         class_img = np.ones((64,64,3))*255
         class_img[:,:,0] = (class_img[:,:,0]*color[0]).astype(int)
         class_img[:,:,1] = (class_img[:,:,1]*color[1]).astype(int)
         class_img[:,:,2] = (class_img[:,:,2]*color[2]).astype(int)
         image_name_1 = f.split("/")[1]
         cv2.imwrite("{}".format(image_name_1) ,class_img)
    elif class_pred == 5:
         color = color_values(0.1)
         class_img = np.ones((64,64,3))*255
         class_img[:,:,0] = (class_img[:,:,0]*color[0]).astype(int)
         class_img[:,:,1] = (class_img[:,:,1]*color[1]).astype(int)
         class_img[:,:,2] = (class_img[:,:,2]*color[2]).astype(int)
         image_name_1 = f.split("/")[1]
         cv2.imwrite("{}".format(image_name_1) ,class_img)
    elif class_pred == 6:
         color = color_values(0.2)
         class_img = np.ones((64,64,3))*255
         class_img[:,:,0] = (class_img[:,:,0]*color[0]).astype(int)
         class_img[:,:,1] = (class_img[:,:,1]*color[1]).astype(int)
         class_img[:,:,2] = (class_img[:,:,2]*color[2]).astype(int)
         image_name_1 = f.split("/")[1]
         cv2.imwrite("{}".format(image_name_1) ,class_img)
    elif class_pred == 7:
         color = color_values(0.6)
         class_img = np.ones((64,64,3))*255
         class_img[:,:,0] = (class_img[:,:,0]*color[0]).astype(int)
         class_img[:,:,1] = (class_img[:,:,1]*color[1]).astype(int)
         class_img[:,:,2] = (class_img[:,:,2]*color[2]).astype(int)
         image_name_1 = f.split("/")[1]
         cv2.imwrite("{}".format(image_name_1) ,class_img)
    elif class_pred == 8:
         color = color_values(0.7)
         class_img = np.ones((64,64,3))*255
         class_img[:,:,0] = (class_img[:,:,0]*color[0]).astype(int)
         class_img[:,:,1] = (class_img[:,:,1]*color[1]).astype(int)
         class_img[:,:,2] = (class_img[:,:,2]*color[2]).astype(int)
         image_name_1 = f.split("/")[1]
         cv2.imwrite("{}".format(image_name_1) ,class_img)  
         
    """elif class_pred == 9:
         color = color_values(0.8)
         class_img = np.ones((64,64,3))*255
         class_img[:,:,0] = (class_img[:,:,0]*color[0]).astype(int)
         class_img[:,:,1] = (class_img[:,:,1]*color[1]).astype(int)
         class_img[:,:,2] = (class_img[:,:,2]*color[2]).astype(int)
         image_name_1 = f.split("/")[1]
         cv2.imwrite("{}".format(image_name_1) ,class_img)    """
         

# Creates Class maps based on predicted class
def creates_class_color(inp_path, out_path):
    print('I/p direc is: ' +inp_path)
    print('O/p direc is: ' +out_path)
    #out_path = inp_path.replace("cropped_imgs","exp1a1_results")
    #out_path = out_path+"/class_maps"
    #print("out_path is:")
    #print(out_path)
    test_set_gen = test_datagen.flow_from_directory(
        inp_path,
        target_size=(64,64),
        batch_size=50,
        class_mode=None, # only data, no labels
        shuffle=False)
    fnames = test_set_gen.filenames
    len_f = len(fnames)
    print('# of files are: ',len_f)
    predictions = model.predict_generator(test_set_gen, verbose=1)
    predicted_classes = np.argmax(predictions,axis=1)
    #len_p = len(predictions)
    for c , f in zip(predicted_classes, fnames): 
        #print('class is: ', c)
        #print('file is: ', f)
        #print('outpath is', out_path)
        class_maps(c, f, out_path)    
 
# call
for inp, out in zip(inpath, outpath):
    #print(inp, out)
    creates_class_color(inp, out)

       