from positionclass import currentposition
from trigclass import trig
from ultrasonicclass import ultrasonic
from marvelmind import MarvelmindHedge
from time import sleep
import RPi.GPIO as IO
IO.setmode(IO.BCM)
import sys
import math


class autonomous():
	def __init__(self):

		##position##
		self.pos = currentposition()
		self.pos.position()
		self.x1 = pos.position()[1]
		self.y1 = pos.position()[2]
		sleep(.5)
#		self.pos.position()
		self.x2 = pos.position()[1]
		self.y2 = pos.position()[2]
		self.x3 = 5.4
		self.y3 = 2.8
		self.targetnumber = 2
		self.deltaT = 1.0
		self.hedge = MarvelmindHedge(tty="/dev/ttyACM0",adr = 16, debug=False)
		self.hedge.start()

		###TRIG###
		self.trig = trig()
		
		###USS###

		

	def runautonomous(self):
		self.IO.output(modeindicatorpin, IO.LOW)
		sleep(0.5)
		self.distance = ultrasonic(17,27)
		self.distance.trigsettle()
	
		if distance.ping() < 10:
			print 'ALERT!!! OBJECT DETECTED!!!'
			print('test')
			
		self.theta1 = trig.angle(x1,y1,x2,y2)
		self.theta2 = trig.angle(x2,y2,x3,y3)
		self.theta3 = theta2 - theta1
		self.x1 = x2
		self.y1 = y2
		self.pos.position()
		self.x2 = pos.position()[1]
		self.y2 = pos.position()[2]
#		self.pos_list = hedge.position_
#		self.x2 = (pos_list[0][1]+pos_list[1][1]+pos_list[2][1])/3
#		self.y2 = (pos_list[0][2]+pos_list[1][2]+pos_list[2][2])/3
		self.TangentDisplacement = math.sqrt(math.pow(x2-x1,2)+math.pow(y2-y1,2))*math.sin(theta3)
		self.TangentVelocity = TangentDisplacement/deltaT
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