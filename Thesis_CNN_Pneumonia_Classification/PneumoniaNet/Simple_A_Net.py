rom keras.models import Sequential
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

class Simple_A_Net:
  @staticmethod
  def build(width,height,depth,classes):
    model=Sequential()
    shape=(height,width,depth)
    channelDim=-1
    
    if K.image_data_format()=="channels_first":
        shape=(depth,height,width)
        channelDim=1




    model.add(Conv2D(4 , kernel_size=(3,3) , strides = 3 , padding = 'same' , activation = 'relu' , input_shape = shape, kernel_regularizer=l2(0.01)))
    model.add(BatchNormalization())
    model.add(MaxPool2D((2,2) , strides = 2 , padding = 'same'))

    model.add(Conv2D(8 , kernel_size=(3,3) , strides = 3 , padding = 'same' , activation = 'relu', kernel_regularizer=l2(0.01)))
    #model.add(Dropout(0.1))
    model.add(BatchNormalization())
    model.add(MaxPool2D((4,4) , strides = 4 , padding = 'same'))


    model.add(Conv2D(8 , kernel_size=(3,3) , strides = 3 , padding = 'same' , activation = 'relu', kernel_regularizer=l2(0.01)))
    #model.add(Dropout(0.1))
    model.add(BatchNormalization())
    model.add(MaxPool2D((4,4) , strides = 4 , padding = 'same'))


    model.add(Flatten())
    model.add(Dense(units = 32, activation = 'relu'))
    model.add(Dropout(0))
    model.add(Dense(units = 2, activation = 'sigmoid'))
    model.compile(optimizer = 'adam' , loss = 'binary_crossentropy' , metrics = ['accuracy', 'binary_crossentropy'])
    
    
    filepath = "pneumonia_classification.hdf5"
    checkpoint = ModelCheckpoint(filepath, monitor='val_loss', verbose=2, save_best_only=True, mode='min', patience=3)
    callbacks_list = [checkpoint]
    
    return model
