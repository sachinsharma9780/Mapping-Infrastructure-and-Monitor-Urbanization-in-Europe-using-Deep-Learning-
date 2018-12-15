# Importing necessrary Libraries
import gdal
import subprocess
import os
import glob
import argparse
import webbrowser,sys
from git import Repo
import git



# Converting shp file to Geojson
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
       
# Calling Conversion of file
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
webbrowser.open_new_tab('Multiple_cities_visln_updated.html')

