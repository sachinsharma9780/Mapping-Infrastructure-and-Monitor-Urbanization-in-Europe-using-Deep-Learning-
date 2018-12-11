# -*- coding: utf-8 -*-
"""
Created on Tue Dec 11 20:45:32 2018

@author: Sachin Sharma
"""

import os
from osgeo import gdal,ogr
import sys 
import subprocess
import glob

def tif_shp(path):
    os.chdir(path)
    for file in glob.glob("*.tif"):
        basename, ext = os.path.splitext(file)
        subprocess.call('python gdal_polygonize.py -q {}.tif -f "ESRI Shapefile" {}.shp'.format(basename, basename), shell =True)
        
tif_shp(r"C:\Users\Sachin Sharma\Desktop\CollaborativeIntelligence_Project\Test")        