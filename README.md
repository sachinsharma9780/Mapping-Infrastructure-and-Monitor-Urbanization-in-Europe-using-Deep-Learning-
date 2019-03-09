# Collaborative_Intelligence_Project at DFKI: Mapping Infrastructure and Monitor Urbanization in Europe

# Description:
An automated mapping and monitoring of urban enviornments through an AI-based analysis using orbital or airborne remote sensed data is of crucial importance to urban areas. In this project, I have used satellite or aerial imagery and state-of-the-art deep learning methods to map urban areas, in particular infrastructure(eg. residential houses, streets, industry).

For detailed information regarding kind of dataset used you can refer to the link: 
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
 * Exp1: 
 1. Prepare data in a such a manner that Industrial and Residential is considered as one class and name it else and rest of the classes will be as it is.
2. Train your classifier with this dataset using the techniques describe in the blog. Script for this is available in code section under the name Ci_a_1.py
3. Now we have a big tiff image of 10k*
