import cv2
import easyocr
import matplotlib.pyplot as plt
import numpy as np


image_path = r'C:\Users\wikto\OneDrive\Pulpit\roz_pisma\textimage\data\test3.png'

img = cv2.imread(image_path)
reader = easyocr.Reader(['pl'],gpu=False)
text_ = reader.readtext(img)

threshold = 0.25

for t_, t in enumerate(text_):
    print(t)
    bbox, text, score = t
    if score > threshold:
        cv2.rectangle(img, bbox[0], bbox[2], (0, 0, 255), 3)
        cv2.putText(img, text, bbox[0], cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 3)

plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.show()
