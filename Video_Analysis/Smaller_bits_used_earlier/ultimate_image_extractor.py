#multiple video exractor

import cv2
import os

def extractframes(dir_path, ex_path):
    for internal_dir_path in os.listdir(dir_path):
        if internal_dir_path != ".DS_Store" :
            if os.path.exists(os.path.join(ex_path, internal_dir_path)) == False:
                os.makedirs(os.path.join(ex_path, internal_dir_path))
            new_internal_dir_path = os.path.join(dir_path, internal_dir_path)
            ex_internal_dir_path = os.path.join(ex_path, internal_dir_path)
            for folder_path in os.listdir(new_internal_dir_path):
                name = folder_path.split("\\")[-1].split(".")[0]
                if os.path.exists(os.path.join(ex_internal_dir_path, name))==False:
                    os.makedirs(os.path.join(ex_internal_dir_path, name))
                new_folder_path = os.path.join(new_internal_dir_path, folder_path)
                new_path = os.path.join(ex_internal_dir_path, name)
                vidobj = cv2.VideoCapture(new_folder_path)
                count = 0
                success = 1
            
                while success:
                    vidobj.set(cv2.CAP_PROP_POS_MSEC, count*500)
                    success, frame = vidobj.read()
                    final_ex_path = os.path.join(new_path, "%s%d.jpg"%(name,count))
                    cv2.imwrite(final_ex_path,frame)
                
                    count+=1
        
                os.remove(final_ex_path)

dir_path = input("enter the path of the video:\n")
ex_path = input("enter the folder where to extract:\n")
final_ex_path = extractframes(dir_path, ex_path)
