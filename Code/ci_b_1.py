#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan  7 00:05:46 2019

@author: sachin_sharma
"""

# Importing the Keras libraries and packages
from keras.models import Sequential 
from keras.layers import Convolution2D
from keras.layers import MaxPooling2D
from keras.layers import Flatten
from keras.layers import Dense 
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np
from sklearn.metrics import classification_report, confusion_matrix
import pandas as pd
# Initialize CNN
model = Sequential()

# building model
model.add(Convolution2D(64, 3, 3, input_shape = (64, 64, 3), activation = 'relu'))
# pooling
model.add(MaxPooling2D(pool_size = (2,2)))

# adding a second convol layer
model.add(Convolution2D(64, 3, 3, activation='relu'))
model.add(MaxPooling2D(pool_size=(2,2)))

# Flattening
model.add(Flatten())

# Full connection
model.add(Dense(units=128, activation='relu'))
# output layer
model.add(Dense(units=9, activation='softmax'))

# compile
model.compile(optimizer = 'adam', loss='categorical_crossentropy', metrics=['accuracy'])

# Fitting the CNN to the images(Image Augmentation, Image Preprocessing)
from keras.preprocessing.image import ImageDataGenerator
train_datagen = ImageDataGenerator(  
        rescale=1./255,
        shear_range=0.2,             
        zoom_range=0.2,              
        horizontal_flip=True)

# normalizing
test_datagen = ImageDataGenerator(rescale=1./255)

# This section will create Training set( Training_Set:TestSet ratio 80:20)
training_set = train_datagen.flow_from_directory(
        'TrainingSet', 
        target_size=(64, 64),   
        batch_size=32,          
        class_mode='categorical') 

# This section will create the Test set
test_set = test_datagen.flow_from_directory( 
        'TestSet',
        target_size=(64, 64),
        batch_size=32,
        class_mode='categorical', 
        shuffle=False)

history = model.fit_generator(training_set, 
                        steps_per_epoch=(training_set.samples/32),
                        epochs=25,
                        validation_data=test_set, 
                        validation_steps=(test_set.samples/32)) 
# save model
model.save('Eurosat_b_1.h5')

# Visualizing the mapping between labels
training_set.class_indices

# Confusion Matrix and Classification report
Y_pred = model.predict_generator(test_set, test_set.samples//32 +1 )
y_pred = np.argmax(Y_pred, axis=1)
print('Confusion Matrix')
cm = confusion_matrix(test_set.classes, y_pred)
#visulaizing
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

#calling
df = cm2df(cm, ["AnnualCrop", "Buildup", "Forest", "HerbaceousVegetation", "Highway", "Pasture", "PermanentCrop", "River", "SeaLake"])
print(df)

print('Classification Report')
target_names = ['AnnualCrop','Buildup','Forest', 'HerbaceousVegetation', 'Highway', 'Pasture', 'PermanentCrop', 'River', 'SeaLake']
classificn_report = classification_report(test_set.classes, y_pred, target_names=target_names)

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

# "Loss"
plt.plot(history.history['loss'])
plt.plot(history.history['val_loss'])
plt.title('Model loss')
plt.ylabel('Loss')
plt.xlabel('Epoch')
plt.legend(['train', 'test'], loc='upper left')
plt.show()


