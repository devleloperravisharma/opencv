import cv2
import numpy
import os

haar_cascade = "C:/Users/Ravis/Documents/Riddhima/open CV/face recognition/haarcascade_frontalface_default.xml"
path_data_sets = "C:/Users/Ravis/Documents/Riddhima/open CV/face recognition/data sets !"

images = []

labels = []

namess = {}

id = 0

for (subdir, dir, files) in os.walk(path_data_sets):
    for subdir in dir:
        namess[id] = subdir
        