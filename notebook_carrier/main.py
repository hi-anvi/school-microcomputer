import cv2
from helpers import Line

cap = cv2.VideoCapture(0)

if not cap.isOpened():
        print("Error: Could not open camera.")
        exit()

classroom = input("Enter class and section: ").lower()

while True:
    ret, frame = cap.read()
    if not ret:
        break

    line = Line(frame)
    if not line.processImage():
        break
    line.getLineData()
    line.QRCodeCheck()
