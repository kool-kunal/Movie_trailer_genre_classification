import os 
import IPython.display as ipd
import librosa 
import librosa.display
#libraries imported

h = []
d = []
r = []
a = [] 

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
                    rom, ar = librosa.load(x) 
                    onset_envelope = librosa.onset.onset_strength(rom)
                    if internal_dir_path == "drama" :
                        d.append(onset_envelope.shape)
                    if internal_dir_path == "action" :
                        a.append(onset_envelope.shape)
                    if internal_dir_path == "romance" :
                        r.append(onset_envelope.shape)
                    if internal_dir_path == "horror" :
                        h.append(onset_envelope.shape)
                except :
                    pass
        else :
            pass


feature_finder("/Users/dhruvchandel/Desktop/extracted_audios")    #Editable part of the code