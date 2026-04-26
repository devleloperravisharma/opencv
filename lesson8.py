import cv2
import numpy as np
import os

# ---------------- PATHS ----------------
path_haarcascade = "C:/Users/Ravis/Documents/Riddhima/open CV/face recognition/haarcascade_frontalface_default.xml"
path_data_sets = "C:/Users/Ravis/Documents/Riddhima/open CV/face recognition/data sets !"

WIDTH = 200
HEIGHT = 200

images = []
labels = []
namess = {}

label_id = 0

# ---------------- LOAD DATASET ----------------
for (subdir, dirs, files) in os.walk(path_data_sets):
    for dir_name in dirs:

        namess[label_id] = dir_name
        folder_path = os.path.join(path_data_sets, dir_name)

        for file_name in os.listdir(folder_path):
            img_path = os.path.join(folder_path, file_name)
            img = cv2.imread(img_path)

            if img is None:
                continue

            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            gray = cv2.resize(gray, (WIDTH, HEIGHT))

            images.append(gray)
            labels.append(label_id)

        label_id += 1

labels = np.array(labels)

# ---------------- TRAIN MODEL ----------------
model = cv2.face.LBPHFaceRecognizer_create()
model.train(images, labels)

# ---------------- FACE DETECTOR ----------------
face_cascade = cv2.CascadeClassifier(path_haarcascade)
webcam = cv2.VideoCapture(0)

# ---------------- SETTINGS ----------------
THRESHOLD = 60
MAX_CAPTURE = 30
capture_count = 0

# ---------------- LOOP ----------------
while True:
    ret, frame = webcam.read()
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray_frame, 1.3, 5)

    for (x, y, w, h) in faces:

        face = gray_frame[y:y + h, x:x + w]
        face_resized = cv2.resize(face, (WIDTH, HEIGHT))

        label, confidence = model.predict(face_resized)

        # DEFAULT = UNKNOWN (RED)
        color = (0, 0, 255)
        text = f"Unknown ({int(confidence)})"

        # KNOWN FACE (GREEN)
        if confidence < THRESHOLD:
            name = namess.get(label, "Unknown")
            text = f"{name} ({int(confidence)})"
            color = (0, 255, 0)

            # increment only for recognized faces
            if capture_count < MAX_CAPTURE:
                capture_count += 1

        # DRAW BOX
        cv2.rectangle(frame, (x, y), (x + w, y + h), color, 2)

        # LABEL
        cv2.putText(
            frame,
            text,
            (x, y - 10),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.7,
            color,
            2
        )

    # ---------------- COUNTER DISPLAY ----------------
    cv2.putText(
        frame,
        f"Captured: {capture_count} / {MAX_CAPTURE}",
        (10, 30),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.9,
        (0, 255, 0),
        2
    )

    cv2.imshow("Face Recognition", frame)

    key = cv2.waitKey(10)
    if key == 27 or capture_count >= MAX_CAPTURE:
        break

webcam.release()
cv2.destroyAllWindows()