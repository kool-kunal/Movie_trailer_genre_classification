'''
In this program I will apply RGB function to all the videos :)
'''
import os 
import cv2
import numpy as np
import pandas as pd
#libraries imported

h = []
d = []
r = []
a = [] 

#Rgb functionality inside here 

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

# dir_path is dictory containing images ;)

def net_average_rgb(mean_rgb_list) :
    sum_red = 0
    sum_green = 0
    sum_blue = 0
    # print("hello\n")
    # print(len(mean_rgb_list))
    # print("Bye")
    for x in range(0,len(mean_rgb_list)) :
        for z in range(0,3) :
            if z==0 :
                sum_blue = sum_blue + mean_rgb_list[x][0]
            if z==1 :
                sum_green = sum_green + mean_rgb_list[x][1]
            if z==2 :
                sum_red = sum_red + mean_rgb_list[x][2]
    return (sum_red/len(mean_rgb_list), sum_green/len(mean_rgb_list), sum_blue/len(mean_rgb_list))









#Now we want to access all the audio in genres by giving a specific path or something like that 

def rgb(path_extracted_images) : 
    os.chdir(path_extracted_images)
    X=[]
    Y=[]
    for genres in os.listdir(path_extracted_images) :
        if genres != ".DS_Store" :
            x = os.path.join(path_extracted_images , genres)
            
            label_dict = {"action":0 , "romance":1 , "drama":2 , "horror" :3}

            for trailer_names in os.listdir(x) : 
                if trailer_names != ".DS_Store" :
                    y = os.path.join(x,trailer_names)
                    print(y)
                    # Make function calls below : 
                    # mean_rgb_list = []
                    mean_rgb_extractor(y)
                    print(net_average_rgb(mean_rgb_list))

                    X.append(list(net_average_rgb(mean_rgb_list)))
                    Y.append(label_dict[genres])
                    mean_rgb_list.clear()

    df_x = pd.DataFrame(X)
    df_y = pd.DataFrame(Y)
    df = pd.concat([df_x,df_y],axis=1)
    df.to_csv("/Users/dhruvchandel/Desktop/aloo.csv")




path_extracted_images = input("Enter the path of to the Extracted images :")

print(rgb(path_extracted_images))