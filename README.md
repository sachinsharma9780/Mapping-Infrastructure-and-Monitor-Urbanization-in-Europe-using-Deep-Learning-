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
3. Make one folder called cropped_imgs in your machine all results during sliding window approach will get stored in this folder. sliding_window_on_Big_Tiff_image.py will automatically create hierarchy of appropriate subfolders and store results accordingly. Now we have a big tiff image(shown in right side of fig2) of 10k 10k pixels, break this image into a small patches of 64*64 pixels as done using sliding_window_on_Big_Tiff_image.py file. 
4. Create Hierarchy of folders using creates_folder_hierarchy.py file to store the results in appropriate folders.
5. Give these cropped images to already trained classifier to get the predictions on 9 classes(can be achieved using script class_map_automation_exp1):
![cnn](https://user-images.githubusercontent.com/40523048/53294039-921b2d00-37df-11e9-9fde-04bfc92acc8b.JPG)
                                  fig1: CNN classification visualization on Satellite images

fig1: reference: https://arxiv.org/pdf/1709.00029.pdf


Note: Buildup class is collection of images from Residential and Intdustrial area. Step 5 and 6 can be achieved using class_map_automation(1).py file.

6. Now we'll add georeference to these images which can be done using adding_georef_automation _exp1.py.
7. Finally, Merge all Classfication prediction maps to make one big image using merge_class_maps_and_prob_maps.py which will look like as following,(Right side image is what I fed to the trained classifier to get the predictions) below are the predictions done on Graz city of Austria: 

![graz_classification](https://user-images.githubusercontent.com/40523048/64496798-124f3e80-d2a9-11e9-994a-215e5a801210.jpg)
                        fig2: Classification Heatmap of Graz city(left) and its corresponding satellite image.

8. You can retrive all Classification and Probability Heatmaps stored in different folders using retrieve_heatmaps.py file.

Note: For generating Probability Heatmaps all data preprocessing steps are same just in 6th step I have used create_prob_maps_of_n_tiff_files.py to generate probability heatmaps.

Probability Heatmap of Graz and Innsbruck cities looks like following where darker colors represents prediction of particular class with very high probability like 99%(i.e. Dark blue color on the bar), as we move probabilty of predicted classes decreases(like yellow or red color):

![hm2](https://user-images.githubusercontent.com/40523048/64496878-b933da80-d2a9-11e9-9cd5-60dbbe5b7ea5.jpg)


* Experiment 2:
1. In this experiment from 10 classes I have separated Industrial and Residential as 2 classes and rest of the classes as Else class.
2. Train your classifier with this dataset using the techniques describe in the blog. Script for this is available in code section under the name exp2_a_1.1.ipynb.
3. 3 to 6 steps are same as experiment 1.

4. same as step 7 and 8 of experiment 1. Following is the Classification Heatmap of experiment 2 on Graz city:

![Screenshot from 2019-09-09 13-03-11](https://user-images.githubusercontent.com/40523048/64525938-53277180-d302-11e9-93e0-9dae88721aa2.png)
      
fig3: Classification Heatmap of Graz city(conducted with experiment2,left) and corresponding satellite image(right). 

5. Now I have moved all the results to Open Street Map(OSM) by converting the results from tif->shp->geoJson files. Below you can see the resuls of experiment2 on OSM. To run the results in your browser you just need to download the classification_heatmap.html file and run it in your local browser.

![Screenshot from 2019-09-09 14-42-29](https://user-images.githubusercontent.com/40523048/64531561-1e221b80-d310-11e9-8075-0b1edb4c3c9c.png)
     fig4: Real Life Application of the project on Open Street Map. Fig shows the results of 5 cities of Austria: Graz, Innsbruck, Wien, Linz.



