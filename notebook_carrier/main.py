import cv2
from helpers import Line

cap = cv2.VideoCapture(0)

if not cap.isOpened():
        print("Error: Could not open camera.")
        exit()
        
ret, frame = cap.read()
if not ret:
    exit()

line = Line(frame)
