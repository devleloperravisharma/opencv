# add files in data sets
# 33314 lines total (never count again)
import cv2
import os

path_haarcascade = "C:/Users/Ravis/Documents/Riddhima/open CV/face recognition/haarcascade_frontalface_default.xml"
path_data_sets = "C:/Users/Ravis/Documents/Riddhima/open CV/face recognition/data sets !"
path_mimi = "C:/Users/Ravis/Documents/Riddhima/open CV/face recognition/data sets !/mimi"

path = os.path.join(path_data_sets, path_mimi)

WIDTH = 500
HEIGHT = 350

var_cascade_classifier = cv2.CascadeClassifier(path_haarcascade)
var_webcam = cv2.VideoCapture(0)
# if external cam put 1

# taking 30 pictures for me
for i in range(30):
   booleann, img = var_webcam.read()
   grayscale_image =  cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
   var_face = var_cascade_classifier.detectMultiScale(grayscale_image, 1.3, 4)
   for (x,y,w,h) in var_face:
      cv2.rectangle(img, (x,y), (x+w, y+h), (2, 9, 79), 3)
      cropped_face = grayscale_image[y : y + h, x : x + w]
      resized_cropped_face = cv2.resize(cropped_face, (WIDTH, HEIGHT))
      cv2.imwrite("%s/%s.png", (path, i), resized_cropped_face)
