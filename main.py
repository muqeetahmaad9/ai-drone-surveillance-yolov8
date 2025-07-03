
from ultralytics import YOLO
import cv2
import numpy as np
from utils.video_comparator import extract_labels

# Load YOLOv8 model
model = YOLO('yolov8s.pt')

# Load baseline and current video
cap1 = cv2.VideoCapture('baseline_video.mp4')
cap2 = cv2.VideoCapture('current_video.mp4')

while cap1.isOpened() and cap2.isOpened():
    ret1, frame1 = cap1.read()
    ret2, frame2 = cap2.read()

    if not ret1 or not ret2:
        break

    frame1 = cv2.resize(frame1, (640, 480))
    frame2 = cv2.resize(frame2, (640, 480))

    results1 = model(frame1)
    results2 = model(frame2)

    labels1 = extract_labels(results1)
    labels2 = extract_labels(results2)

    new_objects = set(labels2) - set(labels1)

    print("New objects detected:", new_objects)

cap1.release()
cap2.release()
cv2.destroyAllWindows()
