from keras.models import Sequential
#from keras.layers.normalization import BatchNormalization
from tensorflow.keras.layers import *
from tensorflow.keras.callbacks import ModelCheckpoint
from tensorflow.keras.regularizers import l2
from keras.layers.convolutional import Conv2D
from keras.layers.convolutional import MaxPooling2D
from keras.layers.core import Activation
from keras.layers.core import Flatten
from keras.layers.core import Dropout
from keras.layers.core import Dense
from keras import backend as K

class Covid19Net:
  @staticmethod
  def build(width,height,depth,classes):
    model=Sequential()
    shape=(height,width,depth)
    channelDim=-1

    if K.image_data_format()=="channels_first":
      shape=(depth,height,width)
      channelDim=1

    model.add(Conv2D(filters=16, kernel_size=(3, 3), input_shape=shape, activation='relu', kernel_regularizer=l2(0.01)))
    model.add(MaxPool2D(pool_size=(2, 2)))

    model.add(Conv2D(filters=32, kernel_size=(3, 3), input_shape=(224, 224, 3), activation='relu', kernel_regularizer=l2(0.01)))
    model.add(MaxPool2D(pool_size=(2, 2)))

    model.add(Conv2D(filters=64, kernel_size=(3, 3), input_shape=(224, 224, 3), activation='relu', kernel_regularizer=l2(0.01)))
    model.add(MaxPool2D(pool_size=(2, 2)))

    model.add(Conv2D(filters=64, kernel_size=(3, 3), input_shape=(224, 224, 3), activation='relu', kernel_regularizer=l2(0.01)))
    model.add(MaxPool2D(pool_size=(2, 2)))

    model.add(Flatten())

    model.add(Dense(224))
    model.add(Activation('relu'))

    model.add(Dropout(0.5))

    model.add(Dense(2))
    model.add(Activation('sigmoid'))

    model.compile(loss='binary_crossentropy',
                  optimizer='adam',
                  metrics=['accuracy'])
    filepath = "covid_detection.hdf5"
    checkpoint = ModelCheckpoint(filepath, monitor='val_loss', verbose=2, save_best_only=True, mode='min', patience=3)
    callbacks_list = [checkpoint]

    return model

