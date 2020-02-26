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


class autonomous():
	#def __init__(self):

	def runautonomous(self):
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
#		pos_list = hedge.position_
#		x2 = (pos_list[0][1]+pos_list[1][1]+pos_list[2][1])/3
#		y2 = (pos_list[0][2]+pos_list[1][2]+pos_list[2][2])/3
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