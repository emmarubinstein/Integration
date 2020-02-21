from pynput import keyboard
from time import sleep
import RPi.GPIO as IO
import time
IO.setwarnings(False)

#===initialize pins===
in1 = 24
in2 = 23
en = 25
in3 = 17
in4 = 27
en2 = 22


IO.setmode(IO.BCM)
IO.setup(in1,IO.OUT)
IO.setup(in2,IO.OUT)
IO.setup(en,IO.OUT)
IO.setup(in3,IO.OUT)
IO.setup(in4,IO.OUT)
IO.setup(en2,IO.OUT)
IO.output(in1,IO.LOW)
IO.output(in2,IO.LOW)
IO.output(in3,IO.LOW)
IO.output(in4,IO.LOW)
p1=IO.PWM(en,1000)
p2=IO.PWM(en2,1000)
p1.start(30)
p2.start(30)
speed = 30
mode = 2


run_flag = True


def on_press_func(key):
	print(str(key.char) + " was pressed")

	if key.char == 'w':
		mode = 1

	elif key.char == 't':
		mode = 2
	
	elif key.char == 's':
		mode = 3
		
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
	if mode == 1:
		print('FORWARD')
		IO.output(in1,IO.HIGH)
		IO.output(in2,IO.LOW)
		IO.output(in3,IO.HIGH)
		IO.output(in4,IO.LOW)
		n=0
		p1.ChangeDutyCycle(0)
		p2.ChangeDutyCycle(0)
		while n<speed:
			time.sleep(.020)
			n=n+1
			p1.ChangeDutyCycle(n)
			p2.ChangeDutyCycle(n)
	elif mode == 2:
		print('STOP')
		IO.output(in1,IO.LOW)
		IO.output(in2,IO.LOW)
		IO.output(in3,IO.LOW)
		IO.output(in4,IO.LOW)
	elif mode == 3:
		print('BACKWARD')
		IO.output(in1,IO.LOW)
		IO.output(in2,IO.HIGH)
		IO.output(in3,IO.LOW)
		IO.output(in4,IO.HIGH)
		n=0
		p1.ChangeDutyCycle(0)
		p2.ChangeDutyCycle(0)
		while n < speed:
			time.sleep(.020)
			n=n+1
			p1.ChangeDutyCycle(n)
			p2.ChangeDutyCycle(n)
	elif mode == 4:
		print('RIGHT')
		IO.output(in1,IO.HIGH)
		IO.output(in2,IO.LOW)
		IO.output(in3,IO.LOW)
		IO.output(in4,IO.HIGH)
		n=0
		p1.ChangeDutyCycle(0)
		p2.ChangeDutyCycle(0)
		while n<speed:
			time.sleep(.020)
			n=n+1
			p1.ChangeDutyCycle(n)
			p2.ChangeDutyCycle(n)
	elif mode == 5:
		print("LEFT")
		IO.output(in1,IO.LOW)
		IO.output(in2,IO.HIGH)
		IO.output(in3,IO.HIGH)
		IO.output(in4,IO.LOW)
		n=0
		p1.ChangeDutyCycle(0)
		p2.ChangeDutyCycle(0)
		while n<speed:
			time.sleep(.020)
			n=n+1
			p1.ChangeDutyCycle(n)
			p2.ChangeDutyCycle(n)
	elif mode == 6:
		print("accelerate")
		speed=speed+5
		p1.ChangeDutyCycle(speed)
		p2.ChangeDutyCycle(speed)
		time.sleep(.100)
		speed=speed+5
		p1.ChangeDutyCycle(speed)
		p2.ChangeDutyCycle(speed)
		print(speed)
	elif mode == 7:
		print("decelerate")
		speed=speed-5
		p1.ChangeDutyCycle(speed)
		p2.ChangeDutyCycle(speed)
		time.sleep(.100)
		speed=speed-5
		p1.ChangeDutyCycle(speed)
		p2.ChangeDutyCycle(speed)
		print(speed)
	elif mode == 8:
		print('Toggle manual controls')
		global run_flag
		if run_flag == True:
			run_flag = False
		else:
			run_flag = True
	sleep(0.5)
	print(run_flag)


