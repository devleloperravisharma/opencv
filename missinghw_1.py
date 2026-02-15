import cv2

# read the images
img1 = cv2.imread(r"C:/Users/Ravis/Documents/Riddhima/open CV/images/snowday_2020.JPG")
img2 = cv2.imread(r"C:/Users/Ravis/Documents/Riddhima/open CV/images/image.jpg")
img2 = cv2.resize(img2, (img1.shape[1], img1.shape[0]))

blended = cv2.addWeighted(img1, 0.7, img2, 0.3, 20)

# display result
cv2.imshow("blend", blended)
cv2.waitKey(0)

