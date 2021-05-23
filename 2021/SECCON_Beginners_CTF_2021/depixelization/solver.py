import cv2
import numpy as np
import os
import string

images = cv2.imread(os.path.dirname(__file__)+"/output.png", 1)
height, width, _ = images.shape

for i in range(width//85):

    for char in string.printable:
        # char2img
        img = np.full((100, 85, 3), (255,255,255), dtype=np.uint8)
        cv2.putText(img, char, (0, 80), cv2.FONT_HERSHEY_PLAIN, 8, (0, 0, 0), 5, cv2.LINE_AA)

        # pixelization
        cv2.putText(img, "P", (0, 90), cv2.FONT_HERSHEY_PLAIN, 7, (0, 0, 0), 5, cv2.LINE_AA)
        cv2.putText(img, "I", (0, 90), cv2.FONT_HERSHEY_PLAIN, 8, (0, 0, 0), 5, cv2.LINE_AA)
        cv2.putText(img, "X", (0, 90), cv2.FONT_HERSHEY_PLAIN, 9, (0, 0, 0), 5, cv2.LINE_AA)
        simg = cv2.resize(img, None, fx=0.1, fy=0.1, interpolation=cv2.INTER_NEAREST) # WTF :-o
        img = cv2.resize(simg, img.shape[:2][::-1], interpolation=cv2.INTER_NEAREST)

        # compare
        if(np.array_equal(img,images[0:height,85*i:85*(i+1)])):
            print(char,end='')
            break
