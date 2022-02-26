import matplotlib
matplotlib.use("Agg")
from keras.preprocessing.image import ImageDataGenerator
#from keras.callbacks import LearningRateScheduler
from tensorflow.keras.optimizers import Adam
from keras.utils import np_utils
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from imutils import paths
import matplotlib.pyplot as plt
import numpy as np
import os
import tensorflow as tf
import pickle

from PneumoniaNet import config
from PneumoniaNet.Simple_B_Net import PneumoniaNet  # This line is the only variable for each model within Schema B.


model_name = 'Simple_B_Net' # This line is the only variable for each model within Schema B.

NUM_EPOCHS=200; BS=32

trainPaths=list(paths.list_images(config.TRAIN_PATH))
lenTrain=len(trainPaths)
lenVal=len(list(paths.list_images(config.VAL_PATH)))
lenTest=len(list(paths.list_images(config.TEST_PATH)))

trainLabels=[int(p.split(os.path.sep)[-2]) for p in trainPaths]
trainLabels=tf.one_hot(trainLabels, depth=2) 
classTotals=sum(trainLabels)  
classWeight=max(classTotals)/classTotals 

trainAug = ImageDataGenerator(
  rescale=1/255.0,
  featurewise_center=False,  
  samplewise_center=False,  
  featurewise_std_normalization=False,  
  samplewise_std_normalization=False,  
  zca_whitening=False,  
  rotation_range = 30,  
  zoom_range = 0.2, 
  width_shift_range=0.1,  
  height_shift_range=0.1,  
  horizontal_flip = True,  
  vertical_flip=False)

valAug=ImageDataGenerator(rescale=1 / 255.0)

trainGen = trainAug.flow_from_directory(
  config.TRAIN_PATH,
  target_size=(224,224),
  batch_size=BS,
  class_mode = 'categorical')    
valGen = valAug.flow_from_directory(
  config.VAL_PATH,
  target_size=(224, 224),
  batch_size=BS,
  class_mode='categorical')      
testGen = valAug.flow_from_directory(
  config.TEST_PATH,
  target_size=(224, 224),
  batch_size=BS,
  class_mode='categorical')      

model=Simple_B_Net.build(width=150, height=150, depth=1, classes=2) # Using different input shape for Schema B.
opt= rmsprop # Using different optimizer for Schema B.
model.compile(loss="binary_crossentropy", optimizer=opt, metrics=["accuracy", "binary_crossentropy"])

learning_rate_reduction = ReduceLROnPlateau(monitor='val_accuracy', patience = 2, verbose=1,factor=0.3, min_lr=0.000001) # Using learning rate control for Schema B.

M=model.fit(
  trainGen,
  steps_per_epoch=lenTrain//BS,
  validation_data=testGen,
  validation_steps=lenTest//BS,
  callbacks = [learning_rate_reduction],
  epochs=NUM_EPOCHS)

# Confusion matrix 
print("Now evaluating the model")
testGen.reset()
pred_indices=model.predict_generator(testGen,steps=(lenTest//BS)+1)
pred_indices=np.argmax(pred_indices,axis=1)
print(classification_report(testGen.classes, pred_indices, target_names=testGen.class_indices.keys()))

cm=confusion_matrix(testGen.classes,pred_indices)
cm = pd.DataFrame(cm , index = ['0','1'] , columns = ['0','1'])
plt.figure(figsize = (10,10))
sns.heatmap(cm,cmap= "Blues", linecolor = 'black' , linewidth = 1 , annot = True, fmt='',xticklabels = labels,yticklabels = labels)
plt.savefig('cm_' + model_name + '.png', dpi=300)

# Figures for accuracy, loss
N = NUM_EPOCHS
plt.style.use("ggplot")
plt.figure()
plt.ylim(0, 1)
plt.plot(np.arange(0,N), M.history["accuracy"], label="train_acc")
plt.plot(np.arange(0,N), M.history["val_accuracy"], label="val_acc")
plt.title("Train/Validation Accuracy on Pneumonia Dataset")
plt.xlabel("Epoch No.")
plt.ylabel("Accuracy")
plt.legend(loc="lower left")
plt.savefig('plot_' + model_name + '_acc.png', dpi=300)

# Figures for binary cross entropy (loss)
plt.style.use("ggplot")
plt.figure()
plt.plot(np.arange(0,N), M.history["binary_crossentropy"], label="train_logit")
plt.plot(np.arange(0,N), M.history["val_binary_crossentropy"], label="test_logit")
plt.title("Train/Test Loss on Pneumonia Dataset")
plt.xlabel("Epoch No.")
plt.ylabel("Logistic Loss")
plt.legend(loc="upper left")
plt.savefig('plot_' + model_name + '_logistic.png', dpi=300)

# Number of parameters
model.count_params()

# Model summary outputs
model.summary()

# Model evaluation function
model.evaluate(testGen)

# Save model
os.chdir("D:\myproject") # change directory wherever I like.
xspath = os.path.abspath("models") + "/" + model_name  # Set up path as models/'model_name'
model.save(xspath) # save the model to the path
model = tf.keras.models.load_model(xspath) # load the model to the path

# Save model history (fitting over epochs)
yspath = os.path.abspath("models") + "/" + xmodel_name + "_M" # Set up directory for the model history to the path
with open(yspath, 'wb') as file_pi:
        pickle.dump(M, file_pi)
