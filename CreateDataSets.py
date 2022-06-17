import cv2 as cv
import numpy as np
from keras.utils import np_utils
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.preprocessing import  image
from tensorflow.keras.preprocessing.image import load_img, img_to_array,array_to_img
import os
import matplotlib.pyplot as plt

direc = r'D:\AI\ProjectCK\DataSet'
labels = []
paths = []
indexlabel = []
features = []
count = 0
x_train = []
Total = 0
num = 0

for i in os.listdir(direc):
    path = os.path.join(direc, i)
    for j in os.listdir(path):
        Total += 1 

for i in os.listdir(direc):
    labels.append(i)
    path = os.path.join(direc, i)
    labels.append(i)
    
    for j in os.listdir(path):
        
        img_path = os.path.join(path, j)
        img = cv.imread(img_path)

        if img.shape[0]>500 and img.shape[1]>500:

            indexlabel.append(count)

            img = img[img.shape[0]//2-250:img.shape[0]//2+250, img.shape[1]//2-250:img.shape[1]//2+250] 

            img = cv.resize(img, (128,128), interpolation=cv.INTER_AREA)
            img = img_to_array(img)
            img = img.reshape(128,128,3)
            img = img.astype('float32')
            img /= 255
            features.append(img) 
            num += 1 
            print('Loading...', num,'/',Total)

    count = count+1

x = np.asarray(features)
y = np.asarray(indexlabel)
y = y.reshape(-1,1)
y = np_utils.to_categorical(y, 15)

np.save('D:\AI\ProjectCK\Data_X.npy', x)
np.save('D:\AI\ProjectCK\Data_Y.npy', y)  

print(x.shape)
print(y.shape)

print(".........Completed..........")