# -*- coding: utf-8 -*-
"""
Created on Tue Dec 11 20:45:32 2018

@author: Sachin Sharma
"""
# Importing necessary libraries
import os
from osgeo import gdal,ogr
import sys 
import subprocess
import glob
import argparse
import webbrowser

# Function to convert tif to shp
def tif_shp(path):
    os.chdir(path)
    for file in glob.glob("*.tif"):
        basename, ext = os.path.splitext(file)
        subprocess.call('python gdal_polygonize.py -q {}.tif -f "ESRI Shapefile" {}.shp'.format(basename, basename), shell =True)

# Function to convert shp to Geojson
def shp_to_GeoJson(path):
    os.chdir(path)
    for file in glob.glob("*.shp"):
        basename, ext = os.path.splitext(file)
        print(r'ogr2ogr -f GeoJSON {}.geojson {}.shp'.format(basename, basename))
        subprocess.call(r'ogr2ogr -f GeoJSON -t_srs EPSG:4326 -s_srs EPSG:3035 {}.geojson {}.shp '.format(basename, basename))

# Getting the path from command Line
def create_arg_parser():
    """"Creates and returns the ArgumentParser object."""

    parser = argparse.ArgumentParser(description='Shp_Geojson')
    parser.add_argument('inputDirectory',
                    help='Path to the input directory.')
    return parser

if __name__ == "__main__":
    arg_parser = create_arg_parser()
    parsed_args = arg_parser.parse_args(sys.argv[1:])
    
    if os.path.exists(parsed_args.inputDirectory):
       print("File exist")

# Calling Functions
tif_shp(parsed_args.inputDirectory)   
shp_to_GeoJson(parsed_args.inputDirectory)    

"""Git code for files updation on Fly"""

#subprocess.call(r'git config --global user.name "sachinsharma9780"', shell=True)
#subprocess.call(r'git config --global user.email sachinsharma9780@gmail.com',shell=True)
#subprocess.call('git status')
#subprocess.call('git init')
#subprocess.call('cd Geojson_updated', shell=True)

subprocess.call('git add *.geojson', shell=True)
subprocess.call('git commit -m "Geojson_File"')
subprocess.call('git push')


# Opening file on webbrowser
webbrowser.open_new_tab('Geotif_visln.html') 
