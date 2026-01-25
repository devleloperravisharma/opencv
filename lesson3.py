import cv2

img = cv2.imread("C:/Users/Ravis/Documents/Riddhima/open CV/images/snowday_2020.JPG")
#cv2.imshow("image run", img)
#cv2.waitKey(0)

img2 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#cv2.imshow("greyscale different method", img2)
#cv2.waitKey(0)

#row, column = img.shape[0:2]

#for i in range(0, row):
    #for j in range(0, column):
        #img[i, j] = sum(img[i, j]) * 0.5
#cv2.imshow("long weird for loop result", img)
#cv2.waitKey(0)

# rotating an image

img3 = cv2.resize(img, (150, 150))
matrix_rotation = cv2.getRotationMatrix2D((75, 75), 180, 1)
rotated_img = cv2.warpAffine(img3, matrix_rotation, (150, 150))
cv2.imshow("rotated image", rotated_img)
cv2.waitKey(0)

edge_detected_image = cv2.Canny(img3, 100, 200)
cv2.imshow("edge detection", edge_detected_image)
cv2.waitKey(0)

img2 = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
cv2.imshow("hsv", img2)
cv2.waitKey(0)

