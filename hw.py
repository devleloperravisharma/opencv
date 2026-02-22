import cv2
import numpy as np

img = cv2.imread('C:/Users/Ravis/Documents/Riddhima/open CV/images/coins.jpg')

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

gray_blur = cv2.GaussianBlur(gray, (9, 9), 2)

circles = cv2.HoughCircles(
    gray_blur,
    cv2.HOUGH_GRADIENT,
    dp=1.2,
    minDist=120,
    param1=100,
    param2=30,
    minRadius=83,
    maxRadius=120
)
if circles is not None:
    circles = np.uint16(np.around(circles))
    for circle in circles[0, :]:
        x, y, r = circle
        # Draw outer circle
        cv2.circle(img, (x, y), r, (0, 255, 0), 2)
        # Draw center
        cv2.circle(img, (x, y), 2, (0, 0, 255), 3)

# 6. Display result
cv2.imshow('Detected Circles', img)
cv2.waitKey(0)
cv2.destroyAllWindows()