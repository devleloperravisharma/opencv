import cv2
import os
from PIL import Image

path = "C:/Users/Ravis/Documents/Riddhima/open CV/images"
os.chdir(path)
width_img = 200
length_img = 200
for take_image_file_one_by_one in os.listdir("."):
    if take_image_file_one_by_one.endswith(".jpg"):
        resized_images = take_image_file_one_by_one.resize((width_img, length_img))
        resized_images.save(take_image_file_one_by_one, "JPEG", quality = 100)
        