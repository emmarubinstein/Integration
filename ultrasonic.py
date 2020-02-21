from ultrasonicclass import ultrasonic
import time
import RPi.GPIO as IO

uss = ultrasonic(17, 27) # setting trigPin and echoPin as 17 and 27, respectively
uss.trigsettle()
while True:
	print("Calculating distance:")
	print(uss.ping())
	time.sleep(1)	