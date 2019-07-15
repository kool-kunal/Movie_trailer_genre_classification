import os 
import IPython.display as ipd
import librosa 
import librosa.display
import numpy as np
#libraries imported

h = []
d = []
r = []
a = []
ht = []
dt = []
rt = []
at = [] 

def time_differ(onset_frames,x,sr,onset_envelope) :
    N = len(x)
    T = N/float(sr)
    t = numpy.linspace(0, T, len(onset_envelope))
    td=t[onset_frames]
    time_difference = []
    for x in range(1,td.shape[0]):
        t=td[x]-td[x-1]
        time_difference.append(t)
    time_difference=np.array(time_difference)
    avg_time=time_difference.mean()
    return avg_time


#Now we want to access all the audio in genres by giving a specific path or something like that 
def feature_finder(path) :
    os.chdir(path)
    for internal_dir_path in os.listdir(path) :
        if internal_dir_path != ".DS_Store" :
            z = os.path.join(path,internal_dir_path)
            for y in os.listdir(z) :
                print(y)
                x = os.path.join(z,y)
                # print(x)
                try :
                    rom, ar = librosa.load(x , sr = 1000) 
                    onset_envelope = librosa.onset.onset_strength(rom , sr = ar)
                    onset_frames = librosa.util.peak_pick(onset_envelope, 4, 4, 4, 4, 0.5, 5)
                    avg_time=time_differ(onset_frames,rom,ar,onset_envelope)
                    if internal_dir_path == "drama" :
                        d.append(onset_frames.shape)
                        dt.append(avg_time)
                    if internal_dir_path == "action" :
                        a.append(onset_frames.shape)
                        at.append(avg_time)
                    if internal_dir_path == "romance" :
                        r.append(onset_frames.shape)
                        rt.append(avg_time)
                    if internal_dir_path == "horror" :
                        h.append(onset_frames.shape)
                        ht.append(avg_time)
                except :
                    pass
        else :
            pass


feature_finder("/Users/dhruvchandel/Desktop/extracted_audios")