import cv2

img = cv2.imread("C:/Users/Ravis/Documents/Riddhima/open CV/images/image3.jpg")
cv2.imshow("run", img)
cv2.waitKey(0)

img2 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("grey", img2)
cv2.waitKey(0)

detected_circles = cv2.HoughCircles(img2, cv2.HOUGH_GRADIENT, 1, minDist = 20, param1 = 50, param2 = 30, minRadius = 10, maxRadius = 20)

