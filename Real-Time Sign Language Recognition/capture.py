import cv2
import os

label = input("Enter Letter (A-Z): ").upper()

path = f"dataset/{label}"

os.makedirs(path, exist_ok=True)

camera = cv2.VideoCapture(0)

count = 0

while True:

    ret, frame = camera.read()

    if not ret:
        break

    cv2.imshow("Capture", frame)

    key = cv2.waitKey(1)

    if key == ord("s"):

        cv2.imwrite(
            f"{path}/{count}.jpg",
            frame
        )

        count += 1

        print("Saved :", count)

    elif key == ord("q"):
        break

camera.release()

cv2.destroyAllWindows()