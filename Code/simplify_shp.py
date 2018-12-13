# -*- coding: utf-8 -*-
"""
Created on Wed Dec 12 14:10:58 2018

@author: Sachin Sharma
"""

import gdal
import subprocess
import os
import subprocess
import webbrowser
import glob

# Converting shp file to kml
def shp_to_simple_shp(path):
    os.chdir(path)
    for file in glob.glob("*.shp"):
        basename, ext = os.path.splitext(file)
        subprocess.call(r'ogr2ogr {}.shp {}.shp -simplify 0.00000000000000001 '.format(basename +'new', basename))


# Calling Function          
shp_to_simple_shp(r"C:\Users\Sachin Sharma\Desktop\CollaborativeIntelligence_Project\simplifying_shp")     