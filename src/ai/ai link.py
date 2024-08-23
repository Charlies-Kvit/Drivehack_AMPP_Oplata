import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os
import cv2
import tensorflow as tf
import glob
import plotly.express as px
import pytesseract as pt

from PIL import Image
from xml.etree import ElementTree as et
from sklearn.model_selection import train_test_split
from tensorflow.keras.preprocessing.image import load_img, img_to_array
from tensorflow.keras.applications import InceptionResNetV2
from tensorflow.keras.models import Model
from tensorflow.keras.layers import Dense, Flatten
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.callbacks import EarlyStopping

base_model = InceptionResNetV2(weights="imagenet", include_top=False, input_shape=(224, 224, 3))
x = base_model.output
x = Flatten()(x)
x = Dense(512, activation="relu")(x)
x = Dense(256, activation="relu")(x)
predictions = Dense(4, activation="sigmoid")(x)

model = Model(inputs=base_model.input, outputs=predictions)

model.compile(loss="mse", optimizer=Adam(learning_rate=1e-4))

model.load_weights(r"C:\plate_detection2.h5")

def predict_plate_coords(filepath):
    img = load_img(filepath, target_size=(224, 224))
    img_arr = img_to_array(img)
    normalized_img = img_arr / 255.0

    h, w = Image.open(filepath).height, Image.open(filepath).width
    normalized_img_arr = normalized_img.reshape(1, 224, 224, 3)

    coords = model.predict(normalized_img_arr, verbose=0)

    denorm = np.array([w, w, h, h])
    coords = coords * denorm
    coords = coords.astype(np.int32)

    return coords[0]

#def xmlFileGen(filename, minX, maxX, minY, maxY):
#    annotation = et.Element('annotation')
#    filenameElm = et.SubElement(annotation, 'filename')
#    filenameElm.text = filename
#    objectElm = et.SubElement(annotation, 'object')
#    bndboxElm = et.SubElement(objectElm, 'bndbox')
#
#    minXElm = et.SubElement(bndboxElm, 'xmin')
#    maxXElm = et.SubElement(bndboxElm, 'xmax')
#    minYElm = et.SubElement(bndboxElm, 'ymin')
#    maxYElm = et.SubElement(bndboxElm, 'ymax')
#
#    minXElm.text = str(minX)
#    maxXElm.text = str(maxX)
#    minYElm.text = str(minY)
#    maxYElm.text = str(maxY)
#
#    filePath, _ = os.path.splitext(filename)
#    filePath+=".xml"
#    file = open(filePath, "w+")
#    file.write(str(et.tostring(annotation))[2:][:-1])
#    file.close()

data_dir = "C:/photo_5348337390491657143_w.jpg"

minX, maxX, minY, maxY = predict_plate_coords(data_dir)


#xmlFileGen(image, minX, maxX, minY, maxY)
img = cv2.imread(data_dir,1)
cv2.rectangle(img,(minX,minY),(maxX,maxY),(0,255,0),2)
cropped = img[minY:maxY, minX:maxX]

imgheight=cropped.shape[0]
imgwidth=cropped.shape[1]

cv2.imshow("jadfhjkghsdfjl", cropped)
#cv2.imshow("jadfhjkghsdfjl", img)
output = pt.image_to_string(cropped)
print(output)
cv2.waitKey(0)
cv2.destroyAllWindows()

