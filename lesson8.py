import cv2
import numpy
import os

# detect who exactly is at the webcam -- making only the people with photos being able to be recognized
path_haarcascade = "C:/Users/Ravis/Documents/Riddhima/open CV/face recognition/haarcascade_frontalface_default.xml"
path_data_sets = "C:/Users/Ravis/Documents/Riddhima/open CV/face recognition/data sets !"

WIDTH = 500
HEIGHT = 350

images = []

labels = []

namess = {}

id = 0

for (subdir, dir, files) in os.walk(path_data_sets):
    for subdir in dir:
        namess[id] = subdir
        folders = path_data_sets + "/" + subdir # this is also done by os.path.join
        for files in folders:
            new_path_for_images = os.path.join(folders, files)
            images.append(cv2.imread(new_path_for_images))
            labels.append(id)
        id = id + 1
images = numpy.array(images)
labels = numpy.array(labels)
model = cv2.face.LBPHFaceRecognizer_create()
model.train(images, labels)

var_cascade_classifier = cv2.CascadeClassifier(path_haarcascade)  # **
var_webcam = cv2.VideoCapture(0)

# if external cam put 1

# taking 30 pictures for me
while True:
   booleann, img = var_webcam.read()
   grayscale_image =  cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
   var_face = var_cascade_classifier.detectMultiScale(grayscale_image, 1.3, 4)
   for (x,y,w,h) in var_face:
      cv2.rectangle(img, (x,y), (x+w, y+h), (2, 9, 79), 3)
      cropped_face = grayscale_image[y : y + h, x : x + w]
      resized_cropped_face = cv2.resize(cropped_face, (WIDTH, HEIGHT)) # **
      prediction_result = model.predict(resized_cropped_face)
      if prediction_result[1] < 120:
        text = cv2.putText(img, "%s-%.0f"%(namess[prediction_result[0]], prediction_result[1]), (x+10, y-10), cv2.FONT_ITALIC, 5 , (16, 16, 66), 2)
   cv2.imshow("text", img)
   key = cv2.waitKey(10)
   if key == 27:
       break
      