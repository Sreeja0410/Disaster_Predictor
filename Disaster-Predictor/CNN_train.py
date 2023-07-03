#Finetuning VGG-16 for classfying the type of disaster using computer vision

#Necessary modules
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.metrics import CategoricalCrossentropy
from tensorflow.keras.layers import Dense
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.regularizers import l2

#Loading standard VGG-16 without output layer
model = load_model("vgg16_multiclassifier.h5")

#Adding a softmax output layer of 4 classes with l2 regularization
model.add(Dense(units = 4,activation = 'softmax',kernel_regularizer=l2(0.01)))

#Traning only the output layer
model.layers[-1].trainable = True

#Compiling the model
model.compile(optimizer = Adam(learning_rate=0.0001),loss = 'CategoricalCrossentropy',metrics = ['accuracy'])
train_batches = ImageDataGenerator(preprocessing_function = tf.keras.applications.vgg16.preprocess_input,rotation_range = 1,width_shift_range=0.1,height_shift_range=0.1,
                shear_range = 0.1,zoom_range=0.0,channel_shift_range=2,horizontal_flip = True,
                vertical_flip = True)\
    .flow_from_directory(directory='Finedata/train' , target_size = (224,224),batch_size = 10)
valid_batches = ImageDataGenerator(preprocessing_function = tf.keras.applications.vgg16.preprocess_input)\
    .flow_from_directory(directory='Finedata/valid' , target_size = (224,224),batch_size = 10)
    
#Training the model
model.fit(x = train_batches,epochs=10,verbose=1,validation_data=valid_batches)

#Saving the model in relative folder
model.save('CNN_Model/vgg16_dd.h5')