#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 31 00:18:07 2018

@author: sachin
"""
import argparse
import os, glob
import subprocess
import numpy as np

# Command line args 1. model 2. path to store prob patches 3. path to 
def parse_args():
    parser = argparse.ArgumentParser(description="create prob patches")
    parser.add_argument('-m', '--model', type=str, required=True, help='Path to your pretrained model')
    parser.add_argument('-out', '--outputDirectory', type=str, required=True, help='path to store prob patches')
    parser.add_argument('-inp', '--inputDirectory', type=str, required=True, help='path where cropped images are')
    return parser

if __name__ == "__main__":
    parser = parse_args()
    args = parser.parse_args()
    
    


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

# Making predictions on new Cropped Jpg images obtained from big tiff image
# Create a generator for prediction
print('I/p direc is ' +args.inputDirectory)
test_set_gen = test_datagen.flow_from_directory(
        args.inputDirectory,
        target_size=(64,64),
        batch_size=50,
        class_mode=None, # only data, no labels
        shuffle=False)

# Getting the filenames from the generator
fnames = test_set_gen.filenames
len_f = len(fnames) 

# Visualizing the mapping between labels

# Get the predictions from the model using the generator
predictions = model.predict_generator(test_set_gen, verbose=1)
predicted_classes = np.argmax(predictions,axis=1)
#print(predictions.shape)

# Getting the max of probabilities from each class prediction
max_probs = []
for i in range(0,len_f):
    max_probs.append(max(predictions[i]))
"""max_probs = np.array(max_probs)
max_probs = np.append(max_probs, 1)
max_probs = np.resize(max_probs, 171138).reshape(7779,22) """

# Creating a Probability map of predictions/Confidence score

# Function to return color values based on probabilities
from matplotlib import pyplot as plt
from matplotlib import colors
from matplotlib import cm as cmx
import cv2

def color_values(prob):
    jet = plt.get_cmap('jet')
    cnorm = colors.Normalize(vmin=0, vmax=1)    
    scalarMap = cmx.ScalarMappable(norm=cnorm, cmap=jet)
    b = scalarMap.to_rgba(prob)
    print("prob", prob)
    return b

for f, p in zip(fnames, max_probs):
    #print(f, p)
    color = color_values(p)
    img = np.ones((64,64,3))*255
    img = img.astype(int)
    img[:,:,0] = (img[:,:,0]*color[0]).astype(int)
    img[:,:,1] = (img[:,:,1]*color[1]).astype(int)
    img[:,:,2] = (img[:,:,2]*color[2]).astype(int)
    image_name = f.split("/")[1]
    cv2.imwrite("{}".format(os.path.join(args.outputDirectory, image_name)), img)

 
