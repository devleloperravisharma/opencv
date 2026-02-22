import cv2
import os
from PIL import Image
# iterate using (means...) for loop :(
path = "C:/Users/Ravis/Documents/Riddhima/open CV/images"
os.chdir(path)
width_img = 200
length_img = 200
for take_image_file_one_by_one in os.listdir("."):
    if take_image_file_one_by_one.endswith(".jpg"):
        img = Image.open(os.path.join(".", take_image_file_one_by_one))
        resized_images = img.resize((width_img, length_img))
        resized_images.save(take_image_file_one_by_one, "JPEG", quality = 100)

video_file = "flowers.mp4"
os.chdir(path)
images = []
for read_images_one_by_one in os.listdir("."):
    if read_images_one_by_one.endswith(".jpg"):
        images.append(read_images_one_by_one)
videoo = cv2.VideoWriter(video_file, cv2.VideoWriter_fourcc(*"mp4v"), 1, (width_img, length_img))

for imagess in images:
    videoo.write(cv2.imread(os.path.join(".", imagess)))
videoo.release()








