from gpiozero import Robot, LineSensor
from time import sleep

robot = Robot(left=(7, 8), right=(9, 10))
left_sensor = LineSensor(17) # left sensor
right_sensor= LineSensor(27) # right sensor
speed = 0.65 # speed of motor

def motor_speed():
    while True:
        left_detect = int(left_sensor.value) # value 1 if line detected on left sensor else 0
        right_detect = int(right_sensor.value) # value 1 if line detected on right sensor else 0

        # Speed tuning
        straight_speed = 1.0   # full speed on straight
        turn_speed = 0.7   # reduced speed for curves

        if left_detect == 0 and right_detect == 0:
            # Both sensors did not detect line, forward
            left_mot, right_mot = straight_speed, straight_speed
        elif left_detect == 0 and right_detect == 1:
            # Right detect line but not black, turn right
            left_mot, right_mot = turn_speed, -turn_speed
        elif left_detect == 1 and right_detect == 0:
            # Left detect line but not black, turn left
            left_mot, right_mot = -turn_speed, turn_speed
        else:
            # Both sensors detected line, forward
            left_mot, right_mot = straight_speed, straight_speed

        yield (right_mot, left_mot) # Robot expects (right, left)
robot.source = motor_speed()

sleep(60)
robot.stop()
robot.source = None
robot.close()
left_sensor.close() # unintializes left sensor
right_sensor.close() # unintializes right sensor
