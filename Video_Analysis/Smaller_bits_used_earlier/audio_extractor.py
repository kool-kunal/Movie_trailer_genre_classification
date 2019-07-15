import moviepy.editor as mp
import os
 

def audio_extractor(dir_path, final_path):
    os.chdir(dir_path)
    for internal_dir_path in os.listdir(dir_path):
        if internal_dir_path != ".DS_Store" :
            if os.path.exists(os.path.join(final_path, internal_dir_path)) == False:
                os.makedirs(os.path.join(final_path, internal_dir_path))
            new_internal_dir_path = os.path.join(dir_path, internal_dir_path)
            final_internal_dir_path = os.path.join(final_path, internal_dir_path)
            for path in os.listdir(new_internal_dir_path):
                new_path = os.path.join(internal_dir_path, path)
                name_of_trailer =path.split(".")[0]
                try :
                    clip = mp.AudioFileClip(new_path)
                    clip.write_audiofile(final_internal_dir_path + "/" + name_of_trailer + ".mp3")
                except :
                    print("Trailer Not Extracted :")
                    print(name_of_trailer)
        else : 
            pass

dir_path = input("enter the folder containing the videos:\n")
final_path = input("enter the path where you want to paste:\n")

audio_extractor(dir_path, final_path)