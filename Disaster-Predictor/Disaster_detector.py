#----Finding the probability and type of the disaster using the trained model----

from PIL import Image
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import img_to_array

#Testing on new data
img = Image.open('Test_image-1.jpg')#Enter the relative path of the image
img = img.resize((224,224))
img = img_to_array(img)
img = np.expand_dims(img, axis=0)

#Loading the fine tuned model
model = load_model("CNN_Model/vgg16_dd.h5")

#Types of disaster the model can predict
classes = ["Cyclone","Earthquake","Flood","WildFire"]

#Inferencing the model for the given image
predict = model.predict(img)
max = np.argmax(predict)

#Probability and type of disaster shown in the image
print("{:.0f}% is a {}".format(predict[0][max]*100, classes[max]))

