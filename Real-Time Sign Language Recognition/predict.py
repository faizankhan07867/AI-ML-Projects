import cv2
import numpy as np
from tensorflow.keras.models import load_model

model = load_model("model.h5")

labels = [
'A','B','C','D','E','F','G','H','I','J',
'K','L','M','N','O','P','Q','R','S','T',
'U','V','W','X','Y','Z'
]

img = cv2.imread("test.jpg")

img = cv2.resize(img,(64,64))

img = img/255.0

img = np.expand_dims(img,axis=0)

prediction = model.predict(img)

print(labels[np.argmax(prediction)])