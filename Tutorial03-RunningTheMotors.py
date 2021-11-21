# CamJam EduKit 3 - Robotics
# Worksheet 3 - Motor Test Code
import time # Import the Time library
from gpiozero import CamJamKitRobot # Import the CamJam GPIO Zero Library
robot = CamJamKitRobot()
time.sleep(5)
# Turn the motors on
robot.forward()
# Wait for 1 seconds
time.sleep(2)
# Turn the motors off
robot.stop()
