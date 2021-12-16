import matplotlib
matplotlib.use("Agg")

from keras.preprocessing.image import ImageDataGenerator
#from keras.callbacks import LearningRateScheduler
from tensorflow.keras.optimizers import Adam
from keras.utils import np_utils
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from Covid19Net.Covid19Net import Covid19Net
from Covid19Net import config
from imutils import paths
import matplotlib.pyplot as plt
import numpy as np
import os

NUM_EPOCHS=25; BS=32

trainPaths=list(paths.list_images(config.TRAIN_PATH))
lenTrain=len(trainPaths)
lenVal=len(list(paths.list_images(config.VAL_PATH)))
lenTest=len(list(paths.list_images(config.TEST_PATH)))

trainLabels=[int(p.split(os.path.sep)[-2]) for p in trainPaths]
trainLabels=np_utils.to_categorical(trainLabels)
classTotals=trainLabels.sum(axis=0)
classWeight=classTotals.max()/classTotals

trainAug = ImageDataGenerator(
  rescale=1/255.0,
  shear_range=0.2,
  zoom_range=0.2,
  horizontal_flip=True)

valAug=ImageDataGenerator(rescale=1 / 255.0)

trainGen = trainAug.flow_from_directory(
  config.TRAIN_PATH,
  target_size=(224,224),
  batch_size=BS,
  class_mode = 'binary')
valGen = valAug.flow_from_directory(
  config.VAL_PATH,
  target_size=(224, 224),
  batch_size=BS,
  class_mode='binary')
testGen = valAug.flow_from_directory(
  config.TEST_PATH,
  target_size=(224, 224),
  batch_size=BS,
  class_mode='binary')

model=Covid19Net.build(width=224,height=224,depth=3,classes=2)
opt= Adam(.001)
model.compile(loss="binary_crossentropy",optimizer=opt,metrics=["accuracy"])

folders = os.listdir(config.TRAIN_PATH)
image_data = []
labels = []
from keras.preprocessing import image

for ix in folders:
    path = os.path.join(config.TRAIN_PATH,ix)
    for im in os.listdir(path):
        img = image.load_img(os.path.join(path,im),target_size=((224,224)))
        img_array = image.img_to_array(img)
        image_data.append(img_array)
        labels.append(ix)
        
x_train = np.array(image_data)
y_train = np.array(labels)

hist = model.fit(x_train, y_train,
                    batch_size=32,
                    epochs = 25,
                    validation_split = 0.10 ) #callbacks=callbacks_list)

# M=model.fit_generator(
#   trainGen,
#   steps_per_epoch=lenTrain//BS,
#   validation_data=valGen,
#   validation_steps=lenVal//BS,
#   class_weight=classWeight,
#   epochs=NUM_EPOCHS)
#
# print("Now evaluating the model")
# testGen.reset()
# pred_indices=model.predict_generator(testGen,steps=(lenTest//BS)+1)
#
# pred_indices=np.argmax(pred_indices,axis=1)
#
# print(classification_report(testGen.classes, pred_indices, target_names=testGen.class_indices.keys()))

# cm=confusion_matrix(testGen.classes,pred_indices)
# total=sum(sum(cm))
# accuracy=(cm[0,0]+cm[1,1])/total
# specificity=cm[1,1]/(cm[1,0]+cm[1,1])
# sensitivity=cm[0,0]/(cm[0,0]+cm[0,1])
# print(cm)
# print(f'Accuracy: {accuracy}')
# print(f'Specificity: {specificity}')
# print(f'Sensitivity: {sensitivity}')
#
# N = NUM_EPOCHS
# plt.style.use("ggplot")
# plt.figure()
# plt.plot(np.arange(0,N), M.history["loss"], label="train_loss")
# plt.plot(np.arange(0,N), M.history["val_loss"], label="val_loss")
# plt.plot(np.arange(0,N), M.history["acc"], label="train_acc")
# plt.plot(np.arange(0,N), M.history["val_acc"], label="val_acc")
# plt.title("Training Loss and Accuracy on the IDC Dataset")
# plt.xlabel("Epoch No.")
# plt.ylabel("Loss/Accuracy")
# plt.legend(loc="lower left")
# plt.savefig('plot.png')

plt.figure(1, figsize = (15, 5))
plt.subplot(1,2,1)
plt.xlabel("Epochs")
plt.ylabel("Loss")
plt.plot( hist.history["loss"], label = "Training Loss")
plt.plot( hist.history["val_loss"], label = "Validation Loss")
plt.grid(True)
plt.legend()

plt.subplot(1,2,2)
plt.xlabel("Epochs")
plt.ylabel("Accuracy")
plt.plot( hist.history["accuracy"], label = "Training Accuracy")
plt.plot( hist.history["val_accuracy"], label = "Validation Accuracy")
plt.grid(True)
plt.legend()
plt.show()