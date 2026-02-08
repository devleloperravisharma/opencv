import cv2
import numpy as np

img = cv2.imread("C:/Users/Ravis/Documents/Riddhima/open CV/images/image3.jpg")
cv2.imshow("run", img)
cv2.waitKey(0)

img2 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img2 = cv2.blur(img2, (3,3))
cv2.imshow("grey", img2)
cv2.waitKey(0)

detected_circles = cv2.HoughCircles(img2, cv2.HOUGH_GRADIENT, 1, 20, param1 = 50, param2 = 30, minRadius = 1, maxRadius = 50)
if detected_circles is not None:
    detected_circles = np.uint16(np.around(detected_circles))
    print(detected_circles)
    for take_list_one_by_one in detected_circles[0, :]:
        x = take_list_one_by_one[0]
        y = take_list_one_by_one[1]
        size = take_list_one_by_one[2]
        circle = cv2.circle(img, (x, y), size, (0, 0, 0), 4)
        cv2.imshow("circle", img)
        cv2.waitKey(0)
blob_circles = cv2.SimpleBlobDetector_Params()
blob_circles.filterByArea = True
blob_circles.minArea = 110
blob_circles.filterByCircularity = True
blob_circles.minCircularity = 0.5
variables_together = cv2.SimpleBlobDetector_create(blob_circles)
key_points = variables_together.detect(img)
circles = cv2.drawKeypoints(img, key_points, img, (255, 0, 0), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
cv2.imshow("simple blob circles", circles)
cv2.waitKey(0)