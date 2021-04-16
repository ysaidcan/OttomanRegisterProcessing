import numpy as np
import cv2

batch_size = 3
num_classes = 2
epochs = 200

from PIL import Image
import glob
image_list = []
for filename in glob.glob("iznik/train/images/*.jpg"): #assuming png
    frame = cv2.imread(filename)
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # hsv hue sat value
    # lower_red= np.array([0,70,50])
    # upper_red= np.array([10,255,255])

    lower_red1 = np.array([170, 70, 50])
    upper_red1 = np.array([180, 255, 255])
    # dark_red= np.uint8([[[12,22,121]]])
    # dark_red=cv2.cvtColor(dark_red,cv2.COLOR_BGR2HSV)

    # mask=cv2.inRange(hsv, lower_red,upper_red)
    mask1 = cv2.inRange(hsv, lower_red1, upper_red1)

    # res=cv2.bitwise_and(frame,frame, mask=mask)
    res = cv2.bitwise_and(frame, frame, mask=mask1)

    im = Image.fromarray(res)
    im.save(filename[:-4]+"_masked"+".jpg")


