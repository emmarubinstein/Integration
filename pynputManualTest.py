from pynput import keyboard
from time import sleep
from motorcontrolclass import Motorcontroller

import RPi.GPIO as IO
import time
IO.setwarnings(False)

#===initialize pins===
In1 = 6
In2 = 5
En = 12
In3 = 1
In4 = 7
En2 = 13


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
	motor_controller = Motorcontroller(In1, In2, En, In3, In4, En2)
	print(str(key.char) + " was pressed")

	if key.char == 'w':
		motor_controller.forward()
		print('FORWARD')

	elif key.char == 's':
		motor_controller.backward()
		print('BACKWARD')
	
	elif key.char == 'a':
		motor_controller.turn("left")

	elif key.char == 'd':
		motor_controller.turn("right")

	elif key.char == 'q':
		motor_controller.halt_turn()

	elif key.char == 'e':
		motor_controller.halt_forward_backward()

	elif key.char == 'm':
		autonomousclass.autonomous()
		print('Switch Modes')
		
		
	elif key.char == 'c':
		p.cleanup()

def on_release_func(key):
	print(str(key.char) + " was released")

#with keyboard.Listener(on_press=on_press_func, on_release=on_release_func) as listener:
#	listener.join()

kl = keyboard.Listener( on_press = on_press_func, on_release = on_release_func)
kl.start()


while(1):
	kl.join()
	sleep(0.5)
	print(run_flag)



