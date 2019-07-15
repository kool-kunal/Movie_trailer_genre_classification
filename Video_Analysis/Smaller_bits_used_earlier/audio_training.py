import librosa
import os
import numpy as np
from keras.models import load_model
from pathlib import Path
import moviepy.editor as mp

label_dict={"action":0,"romance":1,"drama":2,"horror":3}
label_to_genre={0:"action",1:"romance",2:"drama",3:"horror"}


def time_differ(onset_frames,x,sr,onset_envelope) :
    N = len(x)
    T = N/float(sr)
    t = np.linspace(0, T, len(onset_envelope))
    td=t[onset_frames]
    time_difference = []
    for i in range(1,td.shape[0]):
        z=td[i]-td[i-1]
        time_difference.append(z)
    time_difference=np.array(time_difference)
    avg_time=time_difference.mean()
    return avg_time


def get_mfcc(data,sr,n_mfcc=13):
    mfcc=librosa.feature.mfcc(data,sr,n_mfcc=n_mfcc)
    mfcc_mean=np.zeros((n_mfcc,))
    for i in range(mfcc.shape[0]):
        mfcc_mean[i]=(mfcc[i].mean())
    return mfcc_mean
    


def predict_genre():
   
   
    path=input("Enter path of Directory in which videos are located :-")
    os.chdir(path)
    
    print("Extracting Audio File From Video...")
    audio_path_dir=os.path.join(path,"Extracted_Audios")
    for video_path in os.listdir(path):
        if video_path != ".DS_Store" :
            print(video_path)
            name=video_path.split(".")[0]
            clip=mp.AudioFileClip(os.path.join(path,video_path))
            if os.path.exists(os.path.join(path,"Extracted_Audios")) == False:
                os.makedirs(os.path.join(path,"Extracted_Audios"))
            clip.write_audiofile(audio_path_dir+'/'+name+".mp3")
         
    
            audio_path=audio_path_dir+'/'+name+".mp3"
            audio_path=Path(audio_path)
            print("Loading Audio File....")
            data1,sr1=librosa.load(audio_path)
            data2,sr2=librosa.load(audio_path,sr=1000)
            
            # feature extraction
            if(data1.shape[0]==0 or data2.shape[0]==0):
                print("Audio Inappropriate")
                exit()
            else:
                X=np.array([])
                print("Extracting Audio Features...")
                mfcc=get_mfcc(data1,sr1)
                rms=librosa.feature.rms(y=data1).mean()
                onset_envelope = librosa.onset.onset_strength(data2 , sr = sr2)
                onset_frames = librosa.util.peak_pick(onset_envelope, 4, 4, 4, 4, 0.5, 5)
                avg_time=time_differ(onset_frames,data2,sr2,onset_envelope)
                X=np.append(X,mfcc)
                X=np.append(X,rms)
                X=np.append(X,onset_frames.shape[0])
                X=np.append(X,avg_time)
                X=np.reshape(X,(-1,X.shape[0]))
                print("Features Extracted Successfully")
                
                print("Loading Model..")
                model=load_model("/Users/dhruvchandel/Desktop/Final_files/model_1.h5")
                
                y_pred=model.predict(X)
                y_pred=np.reshape(y_pred,(4,))
                for i in range(y_pred.shape[0]):
                    print(label_to_genre[i]+":-%0.2f percent"%(y_pred[i]*100))
               
                os.remove("Extracted_Audios\\"+name+".mp3")
                os.rmdir("Extracted_Audios")

predict_genre()