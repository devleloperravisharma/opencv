import cv2
import time
import numpy as np

videoo = cv2.VideoCapture("C:/Users/Ravis/Documents/Riddhima/open CV/images/video.mp4")
storing_bg_img = 0
for i in range(60):
    boolean, storing_bg_img = videoo.read()
    if boolean is False:
        continue

storing_bg_img = np.flip(storing_bg_img, axis = 1)

while (videoo.isOpened()):
    boolean, img = videoo.read()
    if boolean is False:
        break
    img = np.flip(img, axis = 1)
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    lower_red = np.array([100, 40, 40])
    upper_red = np.array([100, 255, 255])
    mask1 = cv2.inRange(hsv, lower_red, upper_red)
    lower_red = np.array([155, 40, 40])
    upper_red = np.array([180, 255, 255])
    mask2 = cv2.inRange(hsv, lower_red, upper_red)
    mask1 = mask1 + mask2
    mask1 = cv2.morphologyEx(mask1, cv2.MORPH_OPEN, np.ones((3,3)), iterations = 2)
    mask1 = cv2.dilate(mask1, np.ones((3,3)), iterations = 1)
    mask2 = cv2.bitwise_not(mask1)
    result1 = cv2.bitwise_and(storing_bg_img, storing_bg_img, mask = mask1)
    result2 = cv2.bitwise_and(img, img, mask = mask2)
    final_result = cv2.addWeighted(result1, 1, result2, 1, 0)
    cv2.imshow("invisible man !!!!!", final_result)
    k = cv2.waitKey(10)
    if k == 27:
        break

    