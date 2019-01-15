
#Importing necessary libraries 
import keras
import numpy as np
import pandas as pd
from keras.applications import VGG16, inception_v3, resnet50, mobilenet
from keras import models
from keras import layers
from keras import optimizers
from sklearn.metrics import classification_report, confusion_matrix
import matplotlib.pyplot as plt
import os 
import glob
import tifffile as tif
from sklearn.preprocessing import OneHotEncoder, LabelEncoder
from tempfile import TemporaryFile
from sklearn import model_selection
from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten
from keras.layers import Conv2D, MaxPooling2D
from keras.layers.normalization import BatchNormalization
from keras.preprocessing.image import ImageDataGenerator
from keras.regularizers import l1

# dataset
dataset = []
paths = []
labels = []
input_size = 64
input_size = 64
num_channel = 13
# getting paths of stored images 
def read_files(path):
    for dirpath, dirnames, filenames in os.walk(path):
    #print('Current path: ', dirpath)
    #print('Directories: ', dirnames)
    #print('Files: ', filenames)
    #print(dirpath)
       #os.chdir(dirpath)
       paths.append(dirpath)
       
     
read_files('/home/sachin_sharma/Desktop/tif_data')
paths.sort()
paths = paths[1:]
file_names = []
# Converting 13 channel images to np array
def img_array(paths):
    print('{}'.format(paths))
    os.chdir('{}'.format(paths))
    for file in glob.glob("*.tif"):
            print('name of file: '+ file)
            file_names.append(file)
            x = tif.imread('{}'.format(file))
            basename, ext = os.path.splitext(file)
            labels.append(basename)
            x = np.resize(x, (64, 64, 13))
            dataset.append(x)

#calling
for pths in paths:
    img_array(pths)

# Getting the list of max pixel value in each image
max_pixel_val = []
def max_pixel(data):
    max_pixel_val.append(np.amax(data))
   
# calling 
for data in dataset:
    max_pixel(data)

# max of all pixel values
max_all_pixel_value = max(max_pixel_val) 

# Normalizing
X_nparray = np.array(dataset) / max_all_pixel_value
X = X_nparray.reshape((len(dataset), input_size, input_size, num_channel))

# label encoding
lbl_encoder = LabelEncoder()
ohe = OneHotEncoder()
    
# assigning labels to each image
labels_1 = []
for l in labels:
    labels_1.append(l.split("_")[0])

lbl_list = lbl_encoder.fit_transform(labels_1)
Y = ohe.fit_transform(lbl_list.reshape(-1,1)).toarray().astype(int)

outX = TemporaryFile()
outY = TemporaryFile()
np.save(outX, X)
np.save(outY, Y)

# splitting the dataset into training set test set
train_data, test_data, train_labels, test_labels = model_selection.train_test_split(X, Y, test_size = 0.2, random_state = 0)

# hyperparameters
batch_size = 50
num_classes = 9
epochs = 10
input_shape = (input_size, input_size, num_channel)
l1_lambda = 0.00003

# model
model = Sequential()
model.add(BatchNormalization(input_shape=input_shape))         
model.add(Conv2D(64, (2,2), W_regularizer=l1(l1_lambda), activation='relu'))    
model.add(Conv2D(64, (2,2), W_regularizer=l1(l1_lambda), activation='relu'))
model.add(MaxPooling2D(pool_size=(2,2)))
model.add(Dropout(0.3))
model.add(Flatten())
model.add(Dense(512, activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(num_classes, activation='softmax'))
model.summary()

opt = keras.optimizers.Adam()
model.compile(loss='categorical_crossentropy', optimizer=opt, metrics=['accuracy'])

# fitting model
history = model.fit(train_data, train_labels,
          batch_size=batch_size,
          epochs=epochs,
          verbose=1,
          validation_data=(test_data, test_labels),
          )
         

score = model.evaluate(test_data, test_labels, verbose=0)
print('Test loss:', score[0])
print('Test accuracy:', score[1])

# Confusion Matrix and Classification report
Y_pred = model.predict(test_data)
y_pred = np.argmax(Y_pred, axis=1) # predictions
print('Confusion Matrix')
cm = confusion_matrix(test_labels.argmax(axis=1), y_pred)
print(cm)

def cm2df(cm, labels):
    df = pd.DataFrame()
    # rows
    for i, row_label in enumerate(labels):
        rowdata={}
        # columns
        for j, col_label in enumerate(labels): 
            rowdata[col_label]=cm[i,j]
        df = df.append(pd.DataFrame.from_dict({row_label:rowdata}, orient='index'))
    return df[labels]

df = cm2df(cm, ["AnnualCrop", "Buildup", "Forest", "HerbaceousVegetation", "Highway", "Pasture", "PermanentCrop", "River", "SeaLake"])
print(df)

print('Classification Report')
target_names = ['AnnualCrop','Buildup','Forest', 'HerbaceousVegetation', 'Highway', 'Pasture', 'PermanentCrop', 'River', 'SeaLake']
classificn_report = classification_report(test_labels.argmax(axis=1), y_pred, target_names=target_names)
print(classificn_report)

# Plotting the Loss and Classification Accuracy
model.metrics_names
print(history.history.keys())
#  "Accuracy"
plt.plot(history.history['acc'])
plt.plot(history.history['val_acc'])
plt.title('Model Accuracy')
plt.ylabel('Accuracy')
plt.xlabel('Epoch')
plt.legend(['train', 'test'], loc='upper left')
plt.show()
plt.savefig('classifcn.png')

# "Loss"
plt.plot(history.history['loss'])
plt.plot(history.history['val_loss'])
plt.title('Model loss')
plt.ylabel('Loss')
plt.xlabel('Epoch')
plt.legend(['train', 'test'], loc='upper left')
plt.show()





