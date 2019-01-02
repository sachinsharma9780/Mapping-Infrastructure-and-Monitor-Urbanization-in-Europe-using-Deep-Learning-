#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 25 21:26:53 2018

@author: sachin
"""
# Adding georefrences to probability patches

from osgeo import gdal
from osgeo import gdal_array
from osgeo import osr
import csv
import subprocess
import argparse
import os, glob
import errno
import cv2
from io import BytesIO
import tempfile
import numpy as np
from PIL import Image
import argparse

def parse_args():
    parser = argparse.ArgumentParser(description="adding georefrences to images")
    parser.add_argument('-t', '--tif', type=str, required=True, help='Path where your tiff files are for adding georef')
    parser.add_argument('-g', '--georef', type=str, required=True, help='Path where you want to store your georef imgs' )
    parser.add_argument('-i', '--img', type=str, required=True, help='path to imgs in which u want to add georef')
    
    return parser
    
def array2raster(newRasterfn, dataset, array, dtype):
    """
    save GTiff file from numpy.array
    input:
        newRasterfn: save file name
        dataset : original tif file
        array : numpy.array
        dtype: Byte or Float32.
    """
    dataset = gdal.Open(dataset)
    cols = array.shape[1]
    rows = array.shape[0]
    originX, pixelWidth, b, originY, d, pixelHeight = dataset.GetGeoTransform() 

    driver = gdal.GetDriverByName('GTiff')

    # set data type to save.
    GDT_dtype = gdal.GDT_Unknown
    if dtype == "Byte": 
        GDT_dtype = gdal.GDT_Byte
    elif dtype == "Float32":
        GDT_dtype = gdal.GDT_Float32
    elif dtype == "Int32":
        GDT_dtype = gdal.GDT_Int32
    elif dtype == "Byte":
        GDT_dtype = gdal.GDT_Byte        
    else:
        print("Not supported data type.")

    # set number of band.
    if array.ndim == 2:
        band_num = 1
    else:
        band_num = array.shape[2]

    outRaster = driver.Create(newRasterfn, cols, rows, band_num, GDT_dtype)
    outRaster.SetGeoTransform((originX, pixelWidth, 0, originY, 0, pixelHeight))

    # Loop over all bands.
    for b in range(band_num):
        outband = outRaster.GetRasterBand(b + 1)
        # Read in the band's data into the third dimension of our array
        if band_num == 1:
            outband.WriteArray(array)
        else:
            outband.WriteArray(array[:,:,b])

    # setteing srs from input tif file.
    prj=dataset.GetProjection()
    outRasterSRS = osr.SpatialReference(wkt=prj)
    outRaster.SetProjection(outRasterSRS.ExportToWkt())
    outband.FlushCache()


def export_pred(img, outputpath, array):
    f = open(img, 'rb')
    original_im = Image.open(BytesIO(f.read()))
    #print(original_im)
    #flipped_im = original_im.transpose(Image.FLIP_TOP_BOTTOM)
    #except IOError:
    # print('Corrupted file')
    
    file_name = os.path.basename(img)    
    array2raster(os.path.join(outputpath, file_name),img, array, 'Byte')
  
if __name__ == "__main__":
    parser = parse_args()
    args = parser.parse_args()
    print(args)
    os.chdir(args.img)
    

#export pred     
#pred_path = "/home/sachin/Desktop/Ci_project1/test_tif_files"
#prob_patch_path = "/home/sachin/Desktop/Ci_project1/test_prob_maps"
#output_path = "/home/sachin/Desktop/Ci_project1/georef_prob_maps"

image_paths = glob.glob(os.path.join(args.tif,'*.tif')) #path with resample images
array = glob.glob(os.path.join(args.img, '*.tif'))
image_paths.sort()
array.sort()

for x, a in zip(image_paths, array):
    a = os.path.basename(a)
    a = Image.open('{}'.format(a))
    a = np.array(a)
    export_pred(x, args.georef, a)
    
def mergepred(pred_path):
    os.chdir(args.georef)
    gdal.BuildVRT(os.path.join(os.path.dirname(pred_path),"mosaic.vrt"), glob.glob(os.path.join(pred_path,'*.tif')))
    print(pred_path)
    subprocess.check_output(['gdal_translate',os.path.join(os.path.dirname(pred_path),"mosaic.vrt"), os.path.join(os.path.dirname(pred_path),"pred_merge.tif")])
   
# creating heatmap
mergepred(args.georef)   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   