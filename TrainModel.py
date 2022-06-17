from keras import datasets, Sequential
from keras.layers import Conv2D, MaxPooling2D, Dropout, Dense, Flatten, Activation, AveragePooling2D
from keras.callbacks import ModelCheckpoint
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import train_test_split
import numpy as np
from keras.utils import np_utils
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.preprocessing import  image
from tensorflow.keras.preprocessing.image import load_img, img_to_array,array_to_img,ImageDataGenerator
import os
from sklearn.model_selection import train_test_split

x = np.load(r'D:\AI\ProjectCK\Data_X.npy')
y = np.load(r'D:\AI\ProjectCK\Data_Y.npy')

x_train, x_test, y_train, y_test = train_test_split(x,y, test_size=3000, random_state=1200)

print(x_train.shape, y_train.shape)
print(x_train.shape, y_train.shape)


model = Sequential()

model.add(Conv2D(filters=32,
                 kernel_size=(2,2),
                 activation='relu',
                 kernel_initializer='he_uniform',
                 padding='same',
                 input_shape=(128,128,3),
                 strides=(1,1)))
model.add(Dropout(0.2))
model.add(MaxPooling2D(pool_size=(2,2)))

model.add(Conv2D(filters=64,
                 kernel_size=(5,5),
                 activation='relu',
                 padding='same',
                 strides=(1,1)))

model.add(Conv2D(filters=128,
                 kernel_size=(3,3),
                 padding='same',
                 activation='relu',
                 strides=(2,2)))

model.add(Conv2D(filters=256,
                 kernel_size=(2,2),
                 padding='same',
                 activation='relu',
                 strides=(1,1)))



model.add(Flatten())

model.add(Dense(512, activation='relu',input_shape=(128*128*3,), name='layer1')) 
model.add(Dropout(0.2))
model.add(Dense(1028, activation='relu', name='layer2'))
model.add(Dropout(0.2))
model.add(Dense(2056, activation='relu', name='layer3'))
model.add(Dropout(0.2))
model.add(Dense(2056, activation='relu', name='layer5'))
model.add(Dropout(0.2))
model.add(Dense(1028, activation='relu', name='layer6'))
model.add(Dropout(0.2))
model.add(Dense(15, activation='softmax', name='layer7'))

model.summary()

model.compile(loss = 'categorical_crossentropy', optimizer = Adam(lr=0.000001),metrics = ['accuracy'])               

checkpoint = ModelCheckpoint('best_model_improved.h5',     # model filename
                             monitor='val_loss',           # quantity to monitor
                             verbose=1,                    # verbosity - 0 or 1
                             save_best_only= False,        # The latest best model will not be overwritten
                             mode='auto')                  # The decision to overwrite model is made 
                                                           
                                                      
history = model.fit(x_train, y_train,
                    epochs = 1000,
                    callbacks=[checkpoint],
                    validation_data=(x_test, y_test),                          # number of iterations
                    verbose=1)

model.save('Model_Training.h5')
