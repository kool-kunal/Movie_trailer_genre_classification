'''
INPUT :- READ CSV FILE
OUTPUT:- TRAIN MODEL AND FINALLY LOAD THE MODEL
'''

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
df=pd.read_csv("/Users/dhruvchandel/Desktop/hell/action.csv")
data=df.values
X=data[:,:-1]
Y=data[:,-1]
print(X.shape)
print(Y.shape)
from sklearn.utils import shuffle
d=(list)(zip(X,Y))
d=shuffle(d)
X,Y=zip(*d)

X=list(X)
Y=(list)(Y)
X=np.array(X)
Y=np.array(Y)
from keras.utils import np_utils
Y=np_utils.to_categorical(Y)

X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.1)
import tensorflow
from keras.models import Sequential
from keras.layers import Dense
from keras.optimizers import Adam

model=Sequential()

model.add(Dense(128,activation="relu",input_shape=(3,)))
model.add(Dense(64,activation="relu"))
model.add(Dense(4,activation="softmax"))

adam=Adam(lr=0.001)

model.compile(optimizer=adam,loss="categorical_crossentropy",metrics=["accuracy"])

hist=model.fit(X_train,Y_train,epochs=200,batch_size=16,validation_split=0.1)

# saving model
import h5py
model.save("/Users/dhruvchandel/Desktop/hell/naya0.h5")

h=hist.history
plt.plot(h['val_loss'],label="Validation loss ")
plt.plot(h['loss'],label="Training loss")
plt.xlabel("Epoch")
plt.ylabel("Loss")
plt.legend()
plt.show()


plt.plot(h['val_acc'],label="Validation Accuracy ")
plt.plot(h['acc'],label="Training Accuracy")
plt.xlabel("Epoch")
plt.ylabel("Accuracy")
plt.legend()
plt.show()


