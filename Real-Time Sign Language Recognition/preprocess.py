import cv2
import os

dataset = "dataset"

for folder in os.listdir(dataset):

    folder_path = os.path.join(dataset, folder)

    for image in os.listdir(folder_path):

        img_path = os.path.join(folder_path, image)

        img = cv2.imread(img_path)

        img = cv2.resize(img, (64,64))

        cv2.imwrite(img_path, img)

print("Preprocessing Complete")