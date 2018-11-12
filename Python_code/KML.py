# Importing necessrary Libraries
import gdal
import cv2
import subprocess
import os
import subprocess
import webbrowser
import glob

# Converting shp file to kml
def shp_to_kml(path):
    os.chdir(path)
    for file in glob.glob("*.shp"):
        basename, ext = os.path.splitext(file)
        print(r'ogr2ogr -f KML {}.kml {}.shp'.format(basename, basename))
        subprocess.call(r'ogr2ogr -f KML {}.kml {}.shp'.format(basename, basename))

# Visualizing Kml file on Google Earth
def visulaize_kml(path):
    for file in os.listdir(path):
        basename_kml, ext = os.path.splitext(file)
        os.startfile("{}.kml".format(basename_kml))
          

shp_to_kml(r"C:/Users/Sachin Sharma/Desktop/CollaborativeIntelligence_Project/Boundary_clean")     
visulaize_kml(r"C:\Users\Sachin Sharma\Desktop\CollaborativeIntelligence_Project\KMl_files")   