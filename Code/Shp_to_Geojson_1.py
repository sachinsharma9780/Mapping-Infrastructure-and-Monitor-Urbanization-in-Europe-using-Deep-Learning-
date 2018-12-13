# Importing necessrary Libraries
import gdal
import subprocess
import os
import glob

# Converting shp file to kml
def shp_to_GeoJson(path):
    os.chdir(path)
    for file in glob.glob("*.shp"):
        basename, ext = os.path.splitext(file)
        print(r'ogr2ogr -f GeoJSON {}.geojson {}.shp'.format(basename, basename))
        subprocess.call(r'ogr2ogr -f GeoJSON -t_srs EPSG:4326 -s_srs EPSG:3035 {}.geojson {}.shp '.format(basename, basename))


# Calling Function          
shp_to_GeoJson(r"C:\Users\Sachin Sharma\Desktop\CollaborativeIntelligence_Project\Test")     
  