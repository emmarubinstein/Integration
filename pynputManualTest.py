vfrom pynput import keyboard
from time import sleep
from motorcontrolclass import Motorcontroller:

import RPi.GPIO as IO
import time
IO.setwarnings(False)

#===initialize pins===
in1 = 6
in2 = 5
en = 12
in3 = 1
in4 = 7
en2 = 13


#IO.setmode(IO.BCM)
#IO.setup(in1,IO.OUT)
#IO.setup(in2,IO.OUT)
#IO.setup(en,IO.OUT)
#IO.setup(in3,IO.OUT)
#IO.setup(in4,IO.OUT)
#IO.setup(en2,IO.OUT)
#IO.output(in1,IO.LOW)
#IO.output(in2,IO.LOW)
#IO.output(in3,IO.LOW)
#IO.output(in4,IO.LOW)
#p1=IO.PWM(en,1000)
#p2=IO.PWM(en2,1000)
#p1.start(30)
#p2.start(30)
#speed = 30
#mode = 2


run_flag = True


def on_press_func(key):
	motor_controller = MotorController()
	print(str(key.char) + " was pressed")

	if key.char == 'w':
		motor_controller.forward()
		print('FORWARD')

	elif key.char == 's':
		motor_controller.backward
		print('BACKWARD')
	
	elif key.char == 'a':
		motor_controller.left_right_speed()
		
		
	elif key.char == 'd':
		mode = 4
	
	elif key.char == 'a':
		mode = 5

	elif key.char == 'r':
		mode = 6

	elif key.char == 'f':
		mode = 7

	elif key.char == 'm':
		mode = 8

def on_release_func(key):
	print(str(key.char) + " was released")

kl = keyboard.Listener( on_press = on_press_func, on_release = on_release_func)
kl.start()

while(1):
	sleep(0.5)
	print(run_flag)


