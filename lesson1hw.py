import cv2
import os
img=cv2.imread("C:/Users/Ravis/Documents/Riddhima/open CV/opencvclass2.jpg",cv2.IMREAD_COLOR)
cv2.imshow("Background Image",img)#colored image
cv2.waitKey(0)
img2 = cv2.imread("C:/Users/Ravis/Documents/Riddhima/open CV/opencvclass2.jpg", 0)
cv2.imshow("greyscale", img2)
cv2.waitKey(0)
path = "C:/Users/Ravis/Documents/Riddhima/open CV/images"
os.chdir(path)
cv2.imwrite("image.jpg", img)
read = cv2.imread("C:/Users/Ravis/Documents/Riddhima/open CV/opencvclass2.jpg", 1)
b,g,r = cv2.split(img)
cv2.imshow("split b", b)
cv2.waitKey(0)
cv2.imshow("split g", g)
cv2.waitKey(0)
cv2.imshow("split r", r)
cv2.waitKey(0)

image_storing = cv2.addWeighted(img, 0.3, read, 0.3, 0)
cv2.imshow("image storing with colored and greyscale", image_storing)
cv2.waitKey(0)