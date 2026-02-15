import cv2
import numpy as np

# used chatgpt to do this black background for me !
img = np.zeros((500, 300, 3), dtype=np.uint8)

# rectangle
cv2.rectangle(img, (100, 50), (200, 450), (50, 50, 50), -1)

# red light
cv2.circle(img, (150, 150), 40, (0, 0, 255), -1)

# yellow light
cv2.circle(img, (150, 250), 40, (0, 255, 255), -1)

# green light
cv2.circle(img, (150, 350), 40, (0, 255, 0), -1)

# display
cv2.imshow("Traffic Signal", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
