# Collaborative_Intelligence_Project at DFKI: Mapping Infrastructure and Monitor Urbanization in Europe

# Description:
An automated mapping and monitoring of urban enviornments through an AI-based analysis using orbital or airborne remote sensed data is of crucial importance to urban areas. In this project, I have used satellite or aerial imagery and state-of-the-art deep learning methods to map urban areas, in particular infrastructure(eg. residential houses, streets, industry).

For detailed information regarding kind of dataset used you can refer to the article written by me in the below link: 
https://medium.com/@sachinsharma9780/hands-on-experience-on-achieving-state-of-the-art-results-on-classifying-eurosat-satellite-images-91a9897f7433

# Installation:
1) Clone this repository into your Local Machine
2) Install the necessary libraries like Gdal, Keras, Image processing libraries(openCV) etc. Do this by making a new Enviornment in Conda.

Note about Gdal: The Geospatial Data Abstraction Library is a computer software library for reading and writing raster and vector geospatial data formats, and is released under the permissive X/MIT style free software license by the Open Source Geospatial Foundation.
Install Gdal using: conda install gdal

# Usage:
* Getting state of the art results on EuroSAT dataset is really important since we want our mapping to be as accurate as possible. Therefore,  I have written a separate Blog to explain you on how to achieve ~97% accuracy on EuroSat dataset.  
Link to the Blog: https://medium.com/@sachinsharma9780/hands-on-experience-on-achieving-state-of-the-art-results-on-classifying-eurosat-satellite-images-91a9897f7433

* I have conducted 2 experiments in this project each for RGB Images and Multispectral Images:
 * Experiment1: 
 1. Prepare data in a such a manner that Industrial and Residential is considered as one class and name it else and rest of the classes will be as it is.
2. Train your classifier with this dataset using the techniques describe in the blog. Script for this is available in code section under the name Experiment_a_1.py 
3. Make one folder called cropped_imgs in your machine all results during sliding window approach will get stored in this folder. sliding_window_on_Big_Tiff_image.py will automatically create hierarchy of appropriate subfolders and store results accordingly. Now we have a big tiff image(Ground Truth) of 10k 10k pixels, break this image into a small patches of 64*64 pixels as done using sliding_window_on_Big_Tiff_image.py file. 
4. Create Hierarchy of folders using creates_folder_hierarchy.py file to store the results in appropriate folders.
5. Give these cropped images to already trained classifier to get the predictions on 9 classes(can be achieved using script class_map_automation_exp1):
![cnn](https://user-images.githubusercontent.com/40523048/53294039-921b2d00-37df-11e9-9fde-04bfc92acc8b.JPG)
                                  fig1: CNN classification visualization on Satellite images

fig1: reference: https://arxiv.org/pdf/1709.00029.pdf

6. A unique color image is created for each class, following is the color coding used:  

![Classes](https://user-images.githubusercontent.com/40523048/54064993-9c471d80-421a-11e9-9251-d80dc10dcebb.JPG)

Note: Buildup class is collection of images from Residential and Intdustrial area. Step 5 and 6 can be achieved using class_map_automation(1).py file.

7. Now we'll add georeference to these images which can be done using adding_georef_automation _exp1.py.
8. Finally, Merge all Classfication prediction maps to make one big image using merge_class_maps_and_prob_maps.py which will look like as following, below are the predictions done on Graz city of Austria: 

![heatmaps](https://user-images.githubusercontent.com/40523048/64496589-f3e84380-d2a6-11e9-96fa-fe4081e137d2.JPG)

9. You can retrive all Classification and Probability Heatmaps stored in different folders using retrieve_heatmaps.py file.

Note: For generating Probability Heatmaps all data preprocessing steps are same just in 6th step I have used create_prob_maps_of_n_tiff_files.py to generate probability heatmaps.

Probability Heatmap of Graz city looks like following where darker colors represents prediction of particular class with very high probability like 99%(i.e. Dark blue color, blue), light colors like yellow represent prediction with low probability 60%-70%(yellow, orange):

![prob_heatmap](https://user-images.githubusercontent.com/40523048/54076734-dc57e000-42ae-11e9-9292-57a7ca2202f8.JPG)

* Experiment 2:
1. In this experiment from 10 classes we have separated Industrial and Residential as 2 classes and rest of the classes as Else class.
2. Train your classifier with this dataset using the techniques describe in the blog. Script for this is available in code section under the name exp2_a_1.1.ipynb.
3. 3 to 5 steps are same as experiment 1.
6. Following is the Color coding for experiment 2:

![exp2](https://user-images.githubusercontent.com/40523048/55692055-9329a780-59a4-11e9-807e-c7b7652e6a60.JPG)

7. same as step 7 and 8 of experiment 1. Following is the Classification Heatmap of experiment 2 on Graz city:

![exp2_graz](https://user-images.githubusercontent.com/40523048/55692167-a6894280-59a5-11e9-9903-5ae44da3b31d.JPG)


