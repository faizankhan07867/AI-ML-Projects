from tensorflow.keras.models import load_model
import numpy as np
from PIL import Image

model = load_model("model.h5")

img = Image.open("digit.png").convert("L")

img = img.resize((28,28))

img = np.array(img)

img = img / 255.0

img = img.reshape(1,28,28)

prediction = model.predict(img)

print("Prediction :", np.argmax(prediction))