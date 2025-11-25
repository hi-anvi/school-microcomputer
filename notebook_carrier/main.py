import cv2
from helpers import Line
from gpiozero import Robot
from time import sleep

# Initate the camera
cap = cv2.VideoCapture(0)

if not cap.isOpened():
        print("Error: Could not open camera.")
        exit()

# Define GPIO pins for robot
left_motors = (17, 18, 22, 23)
right_motors = (24, 25, 27, 20)
robot = Robot(left=left_motors, right=right_motors)
robot.stop()

while True:
    classroom = input("Enter class and section: ").lower()

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        line = Line(frame)
        if not line.processImage():
            break
        line.getLineData()
        line.QRCodeCheck(classroom)
        if not line.moveToTarget():
            break
    
    print("Bot has reached target or line is discontinued...")
    robot.right(speed=0.5)
    sleep(1)
    robot.stop()
