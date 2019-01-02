# import libraries
import argparse
import os, glob
import subprocess
import numpy as np

# Command line args  
def parse_args():
    parser = argparse.ArgumentParser(description="create class maps")
    parser.add_argument('-m', '--model', type=str, required=True, help='Path to your pretrained model')
    parser.add_argument('-out', '--outputDirectory', type=str, required=True, help='path to store class maps')
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

# Creating a Heatmap of 10 different classes given 10 different colors
def create_class_color(class_pred, f):
    os.chdir(args.outputDirectory)
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
    elif class_pred == 9:
         color = color_values(0.8)
         class_img = np.ones((64,64,3))*255
         class_img[:,:,0] = (class_img[:,:,0]*color[0]).astype(int)
         class_img[:,:,1] = (class_img[:,:,1]*color[1]).astype(int)
         class_img[:,:,2] = (class_img[:,:,2]*color[2]).astype(int)
         image_name_1 = f.split("/")[1]
         cv2.imwrite("{}".format(image_name_1) ,class_img)    
         

for c , f in zip(predicted_classes, fnames): 
    #print(c, f.split("/")[1])
    create_class_color(c, f)   













