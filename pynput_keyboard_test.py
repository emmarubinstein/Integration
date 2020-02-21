from pynput import keyboard
from time import sleep


run_flag = True


def on_press_func(key):
	print(str(key.char) + " was pressed")
	if key.char == 'w':
		print("forward")
		#motor1.changedutycycle(forward)
		#motor2.

	elif key.char == 'd':
		print('right')
		#motor class commands for turning right

	elif key.char == 'a':
		print('left')
		#motor class commands for turning left

	elif key.char == 's':
		print('backward')
		#motor class commands for move backword 

	elif key.char == 'm':
		print('Toggle manual controls')
		global run_flag
		if run_flag == True:
			run_flag = False
		else:
			run_flag = True
	
		

def on_release_func(key):
	print(str(key.char) + " was released")




kl = keyboard.Listener( on_press = on_press_func, on_release = on_release_func)
kl.start()

while(1):
	sleep(0.5)
	print(run_flag)






