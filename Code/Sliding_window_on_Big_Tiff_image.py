
# libraries
import subprocess
import cv2
import numpy as np
import argparse
import os, glob
import errno

# from script.py -h you can take the help about kind of arguments to be passed

def parse_args():
    parser = argparse.ArgumentParser(description="create new chunk images")
    parser.add_argument('-i', '--image', type=str, required=True, help='Path to your input images')
    parser.add_argument('-out', '--outputDirectory', type=str, required=True, help='Path to the output which will contain cropped tif images')
    parser.add_argument('-n','--nworkers', type=int, default=None, help='Number of workers (by default none)')
    parser.add_argument('-probmaps', '--outputProb', type=str, required=True, help='Path to output which contain prob patches')
    parser.add_argument('-r', '--retile', type=str, required=True, help='path to 10,000*10,000 geotif files for retiling')
    #parser.add_argument('-c', '--classout', type=str, required=True, help='path to store class maps')
    #parser.add_argument('-m', '--model', type=str, required=True, help='Path to your pretrained model')
   #parser.add_argument('-f', '--file', type=str, required=True, help='Path to ur big tif files for getting names')
    parser.add_argument('-x', '--sizex', type=int, default=64)
    parser.add_argument('-y', '--sizey', type=int, default=64)
    parser.add_argument('-b', '--bands', type=str, default='1,2,3')
    parser.add_argument('-o', '--overlap', type=int, default=1)
    
    return parser

"""def create_dir(path):
    try:
        os.makedirs(path)
    except OSError as e:
        if e.errno != errno.EEXIST:
            raise """

def retile(path, x, y, image, bands, overlap):
    os.chdir(args.retile)
    subprocess.check_output([
        'python',
        'gdal_retile.py',		
        '-v',
		'-ot',
        'Byte',
        '-co',
        'PHOTOMETRIC=RGB',
        '-targetDir',
        path,
        '-overlap',
        str(overlap),
        '-ps',
        str(x),
        str(y),
        image
    ])
    
if __name__ == "__main__":
    parser = parse_args()
	
    args = parser.parse_args()
    print(args)
    print("Image is  ",args.image)
    bands = []
    for a in args.bands.split(","):
        bands = bands + [a]


# creating list of paths where images are stored
imgpath = []
def img_path(path):
    os.chdir(path)
    for f in glob.glob("*.tif"):
       imgpath.append(os.path.abspath('{}'.format(f)))

img_path(args.image)
imgpath.sort()

# creates paths to store cropped imgs
def make_path(path):
    os.chdir(path)
    for f in imgpath:
        basename = os.path.basename(f)
        b, ext = os.path.splitext(basename)
        os.makedirs(b)
        
        
#make_path('/home/sachin_sharma/Desktop/cropped_imgs')
make_path(args.outputDirectory)


# getting paths to store cropped imgs
cropimgs = []

def crop_path(path):
    for dirpath, dirnames, filenames in os.walk(path):
        print(dirpath)
        #os.chdir(dirpath)
        #os.makedirs('cropimgs')
        cropimgs.append(dirpath)
        #print('Directories: ', dirnames)
        #print('Files: ', filenames)
        #print(dirpath)

#crop_path('/home/sachin_sharma/Desktop/cropped_imgs')
crop_path(args.outputDirectory)
cropimgs = cropimgs[1:]
cropimgs.sort()
print(cropimgs)

# making dirs to store cropped imgs
def make_dirs(f):
    os.chdir(f)
    os.makedirs('crop_imgs')

for f in cropimgs:
    make_dirs(f)

# call retile
for img, path in zip(imgpath, cropimgs):
    print('imgpath: '+img ,'Path to cropimgs: '+path)
    #print(os.path.join(path+'/crop_imgs'))
    #print(os.path.join(path, 'crop_imgs'))
    retile(os.path.join(path, 'crop_imgs'), args.sizex, args.sizey, img, bands, args.overlap)

# del black imgs
def del_black_imgs(path):
    for dirpath, dirnames, filenames in os.walk(path):
        print('Current path: ', dirpath)
        os.chdir(dirpath)
        for file in glob.glob("*.tif"):
            #print(file)
            img = cv2.imread("{}".format(file))
            if np.argmax(img) == 0:
                print("Deleting Black Image", file)
                os.remove(file)
            else:
                print("Not a Black Image", file)

#call
del_black_imgs(args.outputDirectory)











