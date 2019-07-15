# Importing All the required libraries
import numpy as np
import cv2
from matplotlib import pyplot as plt
import os
import h5py
from keras.models import load_model
import shutil

label_to_genre={0:"action",1:"romance",2:"drama",3:"horror"}

# Enter the path of video directory 
vid_path = input("Enter the path of the Video Directory that you want to Analyse:")
os.chdir(vid_path) 
if(os.path.exists(os.path.join(vid_path,"extracted_frames"))==False) :
    os.makedirs(os.path.join(vid_path,"extracted_frames"))
dir_path = os.path.join(vid_path,"extracted_frames")#path to directory of extracted images

count2=0
# Function to extract frames 
def ExtractFrames(path) :
    vidObj = cv2.VideoCapture(path) 
    success = 1
    count=0  
    while success: 
        vidObj.set(cv2.CAP_PROP_POS_MSEC,count*500)
        success, image = vidObj.read() 
        # Saves the frames at the address with frame-count 
        cv2.imwrite(dir_path + "/frame%d.jpg" % count, image) 
        count += 1
    os.remove(dir_path+"/frame%d.jpg"%(count-1))
    count2=count

for videos in os.listdir(vid_path):
    ExtractFrames(os.path.join(vid_path,videos))



# Funtion for finding mean rgb of an image
def mean_image_color(imgedit) :
    Red=np.mean(imgedit[:,:,0])
    Green=np.mean(imgedit[:,:,1])
    Blue=np.mean(imgedit[:,:,2])
    return (Red,Green,Blue)

mean_rgb_list = []

def mean_rgb_extractor(dir_path):
    os.chdir(dir_path)
    for internal_dir_path in os.listdir(dir_path):
        if internal_dir_path != ".DS_Store" :
            img = cv2.imread(os.path.join(dir_path, internal_dir_path))
            imgedit = cv2.resize(src=img , dsize = (28,28))
            mean_rgb_list.append(mean_image_color(imgedit))
            # print(mean_rgb_list)
        else : 
            pass

mean_rgb_extractor(dir_path)

# dir_path is dictory containing images ;)

def net_average_rgb(mean_rgb_list=mean_rgb_list) :
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

def predict_genre():
    print("Loading Model..")
    X=np.array([])
    X = np.append(X,net_average_rgb()[0])
    X = np.append(X,net_average_rgb()[1])
    X = np.append(X,net_average_rgb()[2])
    X=np.reshape(X,(-1,X.shape[0]))
    print(X)

    model=load_model("/Users/dhruvchandel/desktop/Video_Analysis/Visual Analysis/naya_nice_accuracy.h5")

    y_pred=model.predict(X)
    y_pred=np.reshape(y_pred,(4,))
            
    for i in range(y_pred.shape[0]):
        print(label_to_genre[i]+":-%0.2f percent"%(y_pred[i]*100))

def del_extracted_frames(vid_path= vid_path , dir_path=dir_path) :
    os.chdir(dir_path)
    for frame in os.listdir(dir_path):
        os.remove(frame)
    os.chdir(vid_path)
    os.rmdir(dir_path)

print(net_average_rgb(mean_rgb_list))
print("\n")
predict_genre()
del_extracted_frames()








