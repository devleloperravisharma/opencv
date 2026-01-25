import cv2
import numpy as np

img = cv2.imread("C:/Users/Ravis/Documents/Riddhima/open CV/opencvclass1.jpg", cv2.IMREAD_COLOR)
cv2.imshow("image run", img)
cv2.waitKey(0)

kernel = np.ones((7,7), np.uint8)
store_eroded = cv2.erode(img, kernel)
cv2.imshow("eroded image !!!", store_eroded)
cv2.waitKey(0)

# gaussian blur !!
blur_type1 = cv2.GaussianBlur(img, (11, 11), 0)
cv2.imshow("gaussian blur !!",blur_type1)
cv2.waitKey(0)

# median blur !!
blur_type2 = cv2.medianBlur(img, 3)
cv2.imshow("median blur !!", blur_type2)
cv2.waitKey(0)

# bilateral blur !!
blur_type3 = cv2.bilateralFilter(img, 11, 9, 9)
cv2.imshow("bilateral blur !!", blur_type3)
cv2.waitKey(0)

# reflect border !!
border_image2 = cv2.copyMakeBorder(img, 50, 50, 50, 50, cv2.BORDER_REFLECT)
cv2.imshow("reflect border !!", border_image2  )
cv2.waitKey(0)
