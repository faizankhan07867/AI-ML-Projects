import tensorflow as tf
import numpy as np

IMG_SIZE = 128

model = tf.keras.models.load_model("model/crop_model.keras")

classes = [
    "Healthy",
    "Bacterial_Blight",
    "Leaf_Spot",
    "Rust",
    "Mosaic"
]

def predict(image_path):

    img = tf.keras.utils.load_img(
        image_path,
        target_size=(IMG_SIZE, IMG_SIZE)
    )

    img = tf.keras.utils.img_to_array(img)

    img = np.expand_dims(img, axis=0)

    pred = model.predict(img)

    index = np.argmax(pred)

    confidence = float(np.max(pred) * 100)

    return classes[index], round(confidence, 2)