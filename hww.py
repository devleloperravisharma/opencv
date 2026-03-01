import cv2
import os

# Folder containing images
folder = "C:/Users/Ravis/Documents/Riddhima/open CV/images"

# Get all image file names
images = sorted(os.listdir(folder))

# Video settings
width = 400
height = 300
fps = 2

# Create video writer
fourcc = cv2.VideoWriter_fourcc(*'XVID')
video = cv2.VideoWriter("output.avi", fourcc, fps, (width, height))

for img_name in images:
    img_path = os.path.join(folder, img_name)
    
    img = cv2.imread(img_path)
    if img is None:
        continue
    
    # Resize image
    img = cv2.resize(img, (width, height))
    
    # Write frame
    video.write(img)

video.release()
print("Video created successfully!")