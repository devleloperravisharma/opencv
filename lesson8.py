import cv2
import numpy
import os
# detect who exactly is at the webcam -- making only the people with photos being able to be recognized
haar_cascade = "C:/Users/Ravis/Documents/Riddhima/open CV/face recognition/haarcascade_frontalface_default.xml"
path_data_sets = "C:/Users/Ravis/Documents/Riddhima/open CV/face recognition/data sets !"

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
