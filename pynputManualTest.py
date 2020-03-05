from pynput import keyboard
from time import sleep
from motorcontrolclass import Motorcontroller
from autonomousclass import autonomous

import RPi.GPIO as IO
import time
IO.setwarnings(False)

# Manual
In1 = 15
In2 = 18
En = 2
In3 = 23
In4 = 24
En2 = 25

motor_controller = Motorcontroller(In1, In2, En, In3, In4, En2)

# Autonomous
#forwardpin = 14 
#rightpin = 3
#leftpin = 4
#destinationpin = 17
#modeindicatorpin = 27

#autonomous = autonomous(forwardpin, rightpin, leftpin, destinationpin, modeindicatorpin)


def on_press_func(key):
	
	print(str(key.char) + " was pressed")

	global auto_running

	if not auto_running:
		if key.char == 'w':
			motor_controller.forward()
			print('FORWARD')
	
		elif key.char == 's':
			motor_controller.backward()
			print('BACKWARD')
		
		elif key.char == 'a':
			motor_controller.turn("right")
	
		elif key.char == 'd':
			motor_controller.turn("left")
	
		elif key.char == 'q':
			motor_controller.halt_turn()
	
		elif key.char == 'e':
			motor_controller.halt_forward_backward()
		
		elif key.char == 'm':
			auto_running = not auto_running
#			motor_controller.halt_turn()
#			motor_controller.halt_forward_backward()
#			print('switching to autonomous')
#			autonomous.runautonomous()
#			autonomous.allow_run = 1 


	else:
		if key.char == 'm':
			auto_running = not auto_running
			autonomous.allow_run = 0
			print('switching to manual!!')

	if key.char == 'p':
		print('closing')
		motor_controller.halt_turn()
		motor_controller.halt_forward_backward()
#		keyboard.Listener.stop()


def on_release_func(key):
	print(str(key.char) + " was released")


kl = keyboard.Listener( on_press = on_press_func, on_release = on_release_func)

auto_running = False #switching modes

kl.start()

while(1):
	kl.join()
	sleep(0.5)
	print(auto_running)



