from positionclass import currentposition
from trigclass import trig
from ultrasonicclass import ultrasonic
#from motorcontrolclass import motorcontrol
from marvelmind import MarvelmindHedge
from time import sleep
import RPi.GPIO as IO
IO.setmode(IO.BCM)
import sys
import math


##position##
pos = currentposition()
pos.position()
x1 = pos.position()[1]
y1 = pos.position()[2]
sleep(.5)
#pos.position()
x2 = pos.position()[1]
y2 = pos.position()[2]
x3 = 5.4
y3 = 2.8
targetnumber = 2
deltaT = 1.0
hedge = MarvelmindHedge(tty="/dev/ttyACM0",adr = 16, debug=False)
hedge.start()
###TRIG###
trig = trig()

###USS###

###motorcontrol###

in1 = 6 #motor driver
in2 = 5
en = 12
in3 = 1
in4 = 7
en2 = 13

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
speed=30

#===LEDs for motors===#
forwardpin = 14 
rightpin = 15
leftpin = 18
destinationpin = 23
modeindicatorpin = 24

IO.setup(forwardpin, IO.OUT)
IO.setup(rightpin, IO.OUT)
IO.setup(leftpin, IO.OUT)
IO.setup(destinationpin, IO.OUT)
IO.setup(modeindicatorpin, IO.OUT)
IO.output(rightpin,IO.LOW)
IO.output(leftpin,IO.LOW)
IO.output(forwardpin,IO.LOW)
IO.output(destinationpin,IO.LOW)
IO.output(modeindicatorpin, IO.LOW)
#motors1 = motorcontrol(in1, in2, en, in3, in4, en2)
#motors1.setup() 

autonomous = 1

while True: 
	if autonomous == 1:
		try:
			IO.output(modeindicatorpin, IO.LOW)
			sleep(0.5)
			distance = ultrasonic(17,27)
			distance.trigsettle()
	
			if distance.ping() < 10:
				print 'ALERT!!! OBJECT DETECTED!!!'
				print('test')
			
			theta1 = trig.angle(x1,y1,x2,y2)
			theta2 = trig.angle(x2,y2,x3,y3)
			theta3 = theta2 - theta1
			x1 = x2
			y1 = y2
			pos.position()
			x2 = pos.position()[1]
			y2 = pos.position()[2]
#			pos_list = hedge.position_
#			x2 = (pos_list[0][1]+pos_list[1][1]+pos_list[2][1])/3
#			y2 = (pos_list[0][2]+pos_list[1][2]+pos_list[2][2])/3
			TangentDisplacement = math.sqrt(math.pow(x2-x1,2)+math.pow(y2-y1,2))*math.sin(theta3)
			TangentVelocity = TangentDisplacement/deltaT
			print 'X:',pos.position()[1]
			print 'Y:',pos.position()[2]
			print 'Angle:', theta3
		
			if theta3 > 20:
				print 'Turn left'
				print '\n'
				IO.output(leftpin,IO.HIGH)
				IO.output(rightpin,IO.LOW)
				IO.output(forwardpin,IO.LOW)
			elif theta3 < -20:
				print 'Turn right'
				print '\n'
				IO.output(rightpin,IO.HIGH)
				IO.output(leftpin,IO.LOW)
				IO.output(forwardpin,IO.LOW)
			else:
				print 'Continue straight'
				print '\n'
				IO.output(forwardpin,IO.HIGH)
				IO.output(rightpin,IO.LOW)
				IO.output(leftpin,IO.LOW)
			
	
			if math.fabs(x2-5.586) < 0.5 and math.fabs(y2-2.68) < 0.5 and targetnumber==2:
				print 'STOP AND TURN RIGHT!!!'
				i=0
				while i<5:
					IO.output(destinationpin,IO.HIGH)
					sleep(0.25)
					IO.output(destinationpin,IO.LOW)
					sleep(0.25)
					i=i+1
				x3=9.318
				y3= -1.58
				targetnumber=3
			if math.fabs(x2-9.318) < 1 and math.fabs(y2+1.58) < 1 and targetnumber==3:
				print 'STOP AND TURN RIGHT!!!'
				i=0
				while i<5:
					IO.output(destinationpin,IO.HIGH)
					sleep(0.25)
					IO.output(destinationpin,IO.LOW)
					sleep(0.25)
					i=i+1
				x3=5.654
				y3= -4.017
				targetnumber=4
			if math.fabs(x2-5.654) < 1 and math.fabs(y2+4.017) < 1 and targetnumber==4:
				print 'STOP AND TURN RIGHT!!!'
				i=0
				while i<5:
					IO.output(destinationpin,IO.HIGH)
					sleep(0.25)
					IO.output(destinationpin,IO.LOW)
					sleep(0.25)
					i=i+1
				x3=2.396
				y3=0.125
				targetnumber=1
			if math.fabs(x2-2.396) < 1 and math.fabs(y2-0.125) < 1 and targetnumber==1:
				print 'STOP, you have reached the target destination'
				i=0
				while i<5:
					IO.output(destinationpin,IO.HIGH)
					sleep(0.25)
					IO.output(destinationpin,IO.LOW)
					sleep(0.25)
					i=1+1
		except KeyboardInterrupt: #Not for this, use pynput
			autonomous = 0

#####manual#####
	
	if autonomous == 0:
		IO.output(modeindicatorpin, IO.HIGH)
		IO.output(rightpin,IO.LOW)
		IO.output(leftpin,IO.LOW)
		IO.output(forwardpin,IO.LOW)
		IO.output(destinationpin,IO.LOW)
		x=raw_input()
	#===STOP====#
		if x=='q':
			print("standstill")
			IO.output(in1,IO.LOW)
			IO.output(in2,IO.LOW)
			IO.output(in3,IO.LOW)
			IO.output(in4,IO.LOW)
			x='z'
	
	#===FORWARD===#
		elif x=='w':
			print("forward")
			IO.output(in1,IO.HIGH)
			IO.output(in2,IO.LOW)
			IO.output(in3,IO.HIGH)
			IO.output(in4,IO.LOW)
			n=0
			p1.ChangeDutyCycle(0)
			p2.ChangeDutyCycle(0)
			while n<speed:
				sleep(.020)
				n=n+1
				p1.ChangeDutyCycle(n)
				p2.ChangeDutyCycle(n)
			mode=1
			x='z'
	
	#===REVERSE===#
		elif x=='s':
			print("backward")
			IO.output(in1,IO.LOW)
			IO.output(in2,IO.HIGH)
			IO.output(in3,IO.LOW)
			IO.output(in4,IO.HIGH)
			n=0
			p1.ChangeDutyCycle(0)
			p2.ChangeDutyCycle(0)
			while n<speed:
				sleep(.020)
				n=n+1 
				p1.ChangeDutyCycle(n)
				p2.ChangeDutyCycle(n)
			mode=2 
			x='z'
	
	#===LEFT===#
		elif x=='a':
			print("left")
			IO.output(in1,IO.LOW)
			IO.output(in2,IO.HIGH)
			IO.output(in3,IO.HIGH)
			IO.output(in4,IO.LOW)
			n=0
			p1.ChangeDutyCycle(0)
			p2.ChangeDutyCycle(0)
			while n<speed:
				sleep(.020)
				n=n+1
				p1.ChangeDutyCycle(n)          
				p2.ChangeDutyCycle(n)
			mode=3
	
			x='z'
	        
	#===RIGHT===#
		elif x=='d':
			print("right")
			IO.output(in1,IO.HIGH)
			IO.output(in2,IO.LOW)
			IO.output(in3,IO.LOW)
			IO.output(in4,IO.HIGH)
			n=0
			p1.ChangeDutyCycle(0)
			p2.ChangeDutyCycle(0)
			while n<speed:
				sleep(.020)
				n=n+1
				p1.ChangeDutyCycle(n)
				p2.ChangeDutyCycle(n)
			mode=4
			x='z'
	        
	#===ACCELERATE===#
		elif x=='r':
			print("acclerate")
			speed=speed+5
			p1.ChangeDutyCycle(speed)
			p2.ChangeDutyCycle(speed)
			sleep(.100)
			speed=speed+5
			p1.ChangeDutyCycle(speed)
			p2.ChangeDutyCycle(speed)
			print(speed)
			x='z'
	        
	#===DECELERATE===#
		elif x=='f':
			print("decelerate")
			p1.ChangeDutyCycle(speed)
			p2.ChangeDutyCycle(speed)
			sleep(.100)
			speed=speed-5
			p1.ChangeDutyCycle(speed)
			p2.ChangeDutyCycle(speed)
			print(speed)
			x='z'
	#===EXIT===#
		elif x=='e':
			IO.cleanup()
			break
	#===TOGGLE MANUAL/AUTO===#
		elif x=='m':
			autonomous = 1
			x='z'	   
		else:
			print("<<<  wrong data  >>>")
			print("please enter direction key to the defined data to continue.....")
	

#Try: all your code

#except keyboardinterrupt:
#	GPIO.cleanup()
#	sys.exit()

