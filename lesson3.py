import cv2

img = cv2.imread("C:/Users/Ravis/Documents/Riddhima/open CV/images/snowday_2020.JPG")
img_resized = cv2.resize(img, (200, 250))
cv2.imshow("image run", img)
cv2.waitKey(0)

img2 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("greyscale different method", img2)
cv2.waitKey(0)

row, column = img_resized.shape[0:2]

for i in range(0, row):
    for j in range(0, column):
        img_resized[i, j] = sum(img_resized[i, j]) * 0.5
cv2.imshow("long weird for loop result", img)
cv2.waitKey(0)

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

# lesson 4 
line = cv2.line(img, (0,0), (100, 100), (0, 0, 0 ), 2)
cv2.imshow("line", line)
cv2.waitKey(0)

rectangle = cv2.rectangle(img, (0,0), (150, 150), (0, 0, 0), 3)
cv2.imshow("rectangle", rectangle)
cv2.waitKey(0)

filled_rectangle = cv2.rectangle(img, (0, 0), (200, 200), (0, 0, 0), -1)
cv2.imshow("filled rectangle", filled_rectangle)
cv2.waitKey(0)

circle = cv2.circle(img, (350, 350), 100, (0, 0, 0), 3)
cv2.imshow("circle", circle)
cv2.waitKey(0)

filled_circle = cv2.circle(img, (400, 400), 100, (0, 0, 0), -1 )
cv2.imshow("filled circle", filled_circle)
cv2.waitKey(0)

text = cv2.putText(img, "megumi", (500, 500), cv2.FONT_ITALIC, 5 , (16, 16, 66), 2)
cv2.imshow("text", text)
cv2.waitKey(0)

