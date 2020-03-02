from pynput import keyboard
from time import sleep
from motorcontrolclass import Motorcontroller
from autonomousclass import autonomous

import RPi.GPIO as IO
import time
IO.setwarnings(False)

# Manual
In1 = 6
In2 = 5
En = 12
In3 = 1
In4 = 7
En2 = 13

motor_controller = Motorcontroller(In1, In2, En, In3, In4, En2)

# Automatic
forwardpin = 14 
rightpin = 15
leftpin = 18
destinationpin = 23
modeindicatorpin = 24

autonomous = autonomous(forwardpin, rightpin, leftpin, destinationpin, modeindicatorpin)


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
			motor_controller.halt_turn()
			motor_controller.halt_forward_backward()
			print('switching to autonomous')
			autonomous.runautonomous()

	else:
		if key.char == 'm':
			auto_running = not auto_running
			print('switching to manual!!')

	if key.char == chr(27):
		print('closing this shit')
		keyboard.Listener.stop()


def on_release_func(key):
	print(str(key.char) + " was released")


kl = keyboard.Listener( on_press = on_press_func, on_release = on_release_func)

auto_running = False #switching modes

kl.start()

while(1):
	kl.join()
	sleep(0.5)
	print(auto_running)



