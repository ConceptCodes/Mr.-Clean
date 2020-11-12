import os
import cv2
import argparse
from tqdm import tqdm


# helper variables
exts = ('.jpg', '.jpeg', '.gif', '.png')
output_dir = ''
input_dir = ''
imgs = []

# parse cmd-line to grab the input directory
parser = argparse.ArgumentParser(prog="mr_clean", description='EXIF Data Scrubber')
parser.add_argument('--input_directory', metavar='--input_directory', type=str, help='Folder where original images are located')
parser.add_argument('--output_directory', metavar='--output_directory', type=str, help='Folder where scrubbed images should be saved')

input_dir = parser.parse_args().input_directory
output_dir = os.path.join(parser.parse_args().output_directory, 'clean')

# check if output dir exist, if not create it 
if not os.path.exists(output_dir):
    print('Creating Output directory => "{}"'.format(output_dir))
    try:
        os.mkdir(output_dir)
    except ValueError:
        print('Error with output directory please specify another one')
        raise

print('Searching "{}" for images..'.format(input_dir))
for file in tqdm(os.listdir(input_dir)):
    #filer through all non image file formats
    if file.lower().endswith(exts):
        imgs.append(file)
print('\nFound {} images in "{}\n"'.format(len(imgs),input_dir))


# loop through and create clean copies of images
print('\nScrubbing images..')
for file in tqdm(imgs):
    try:
        img = cv2.imread(os.path.join(input_dir,file))
        if img is not None:
            cv2.imwrite(os.path.join(output_dir, file), img)
    except ValueError:
        print('Error with opening {}, moving on to next image'.format(file))
print('\nDone, scrubbed images are located at "{}"'.format(output_dir))

