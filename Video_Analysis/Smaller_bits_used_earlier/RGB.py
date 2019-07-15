# Importing All the required libraries
import numpy as np
import cv2
from matplotlib import pyplot as plt
import os

# Extracting images from a Video 

'''
# Function to extract frames 
def ExtractFrames(path) :
    vidObj = cv2.VideoCapture(path) 
    count = 0
    success = 1
      
    while success: 
        vidObj.set(cv2.CAP_PROP_POS_MSEC,count*500)
        success, image = vidObj.read() 
        # Saves the frames at the address with frame-count 
        cv2.imwrite("/Path/where/frames/are/to/be/stored/frame%d.jpg" % count, image) 
        count += 1
    os.remove("/Same/Path/as/written/in/cv2.imwrite/ok/"+"frame%d.jpg"%(count-1))

ExtractFrames('Path of Video')
'''


# Funtion for finding mean rgb of an image
def mean_image_color(imgedit) :
    '''
    Total = 0 
    Red = 0
    Blue = 0
    Green = 0 
    for x in range(0,28):
        for y in range(0,28):
            Total = Total+1
            for z in range(0,3):
                if z==0 : 
                    Blue = Blue + imgedit[x][y][z]
                elif z==1 :
                    Green = Green + imgedit[x][y][z]
                elif z==2 :
                    Red = Red + imgedit[x][y][z]
    return (Red/Total , Green/Total , Blue/Total)
    '''
    red=np.mean(imgedit[:,:,0])
    green=np.mean(imgedit[:,:,1])
    blue=np.mean(imgedit[:,:,2])
    return (red,green,blue)
mean_rgb_list = []


def mean_rgb_extractor(dir_path):
    os.chdir(dir_path)
    for internal_dir_path in os.listdir(dir_path):
        if internal_dir_path != ".DS_Store" :
            img = cv2.imread(os.path.join(dir_path, internal_dir_path))
            imgedit = cv2.resize(src=img , dsize = (28,28))
            mean_rgb_list.append(mean_image_color(imgedit))
        else : 
            pass

dir_path = input("enter the folder containing the extracted images:\n")

mean_rgb_extractor(dir_path)


# Below is the function which will tell us the net average color of the video :)
def net_average_rgb(mean_rgb_list) :
    sum_red = 0
    sum_green = 0
    sum_blue = 0
    for x in range(0,len(mean_rgb_list)) :
        for z in range(0,3) :
            if z==0 :
                sum_blue = sum_blue + mean_rgb_list[x][0]
            if z==1 :
                sum_green = sum_green + mean_rgb_list[x][1]
            if z==2 :
                sum_red = sum_red + mean_rgb_list[x][2]
    return (sum_red/len(mean_rgb_list), sum_green/len(mean_rgb_list), sum_blue/len(mean_rgb_list))


print(net_average_rgb(mean_rgb_list))
print("\n")








