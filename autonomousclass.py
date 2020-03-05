from positionclass import currentposition
from trigclass import trig
from ultrasonicclass import ultrasonic
from marvelmind import MarvelmindHedge
from motorcontrolclass import Motorcontroller
from time import sleep

import RPi.GPIO as IO
import sys
import math

IO.setmode(IO.BCM)

class autonomous():
	def __init__(self, forwardpin, leftpin, rightpin, destinationpin, modeindicatorpin):

		##position##
		self.pos = currentposition()
		self.pos.position()
		self.x1 = self.pos.position()[1]
		self.y1 = self.pos.position()[2]
		sleep(.5)
		self.x2 = self.pos.position()[1]
		self.y2 = self.pos.position()[2]
		self.x3 = 5.4
		self.y3 = 2.8
		self.targetnumber = 2
		self.deltaT = 1.0
		self.hedge = MarvelmindHedge(tty="/dev/ttyACM0",adr = 16, debug=False)
		self.hedge.start()

		###TRIG###
		self.trig = trig()
		
		###USS###

		# IO setup 
		self.forwardpin = forwardpin
		self.rightpin = rightpin
		self.leftpin = leftpin
		self.destinationpin = destinationpin
		self.modeindicatorpin = modeindicatorpin

		IO.setmode(IO.BCM)
		IO.setup(self.forwardpin, IO.OUT)
		IO.setup(self.rightpin, IO.OUT)
		IO.setup(self.leftpin, IO.OUT)
		IO.setup(self.destinationpin, IO.OUT)
		IO.setup(self.modeindicatorpin, IO.OUT)

#		self.motor_controller = Motorcontroller(In1, In2, En, In3, In4, En2)
#		self.allow_run = 0

	def runautonomous(self):
		while self.allow_run: 

			IO.output(self.rightpin,IO.LOW)
			IO.output(self.leftpin,IO.LOW)
			IO.output(self.forwardpin,IO.LOW)
			IO.output(self.destinationpin,IO.LOW)
			IO.output(self.modeindicatorpin, IO.LOW)

			IO.output(self.modeindicatorpin, IO.LOW)
			sleep(0.5)
			self.distance = ultrasonic(17,27)
			self.distance.trigsettle()
			
			#ultrasonic sensor
			if self.distance.ping() < 10:
				print 'ALERT!!! OBJECT DETECTED!!!'
				print('test')
			
			#angle correction	
			self.theta1 = self.trig.angle(self.x1,self.y1,self.x2,self.y2)
			self.theta2 = self.trig.angle(self.x2,self.y2,self.x3,self.y3)
			self.theta3 = self.theta2 - self.theta1
			self.x1 = self.x2
			self.y1 = self.y2
			self.pos.position()
			self.x2 = self.pos.position()[1]
			self.y2 = self.pos.position()[2]
	#		self.pos_list = hedge.position_
	#		self.x2 = (pos_list[0][1]+pos_list[1][1]+pos_list[2][1])/3
	#		self.y2 = (pos_list[0][2]+pos_list[1][2]+pos_list[2][2])/3
			self.TangentDisplacement = math.sqrt(math.pow(self.x2-self.x1,2)+math.pow(self.y2-self.y1,2))*math.sin(self.theta3)
			self.TangentVelocity = self.TangentDisplacement/self.deltaT
			print 'X:',self.pos.position()[1]
			print 'Y:',self.pos.position()[2]
			print 'Angle:', self.theta3

			# start out moving forward
			motor_controller.forward()
		
			if self.theta3 > 20:
				print 'Turn left'
				print '\n'
				IO.output(self.leftpin,IO.HIGH)
				IO.output(self.rightpin,IO.LOW)
				IO.output(self.forwardpin,IO.LOW)
				motor_controller.turn("right")
			elif self.theta3 < -20:
				print 'Turn right'
				print '\n'
				IO.output(self.rightpin,IO.HIGH)
				IO.output(self.leftpin,IO.LOW)
				IO.output(self.forwardpin,IO.LOW)
				motor_controller.turn("left")
			else:
				print 'Continue straight'
				print '\n'
				IO.output(self.forwardpin,IO.HIGH)
				IO.output(self.rightpin,IO.LOW)
				IO.output(self.leftpin,IO.LOW)
				motor_controller.halt_turn()
		
			if math.fabs(self.x2-5.586) < 0.5 and math.fabs(self.y2-2.68) < 0.5 and self.targetnumber==2:
				print 'STOP AND TURN RIGHT!!!'
				i=0
				while i<5:
					IO.output(self.destinationpin,IO.HIGH)
					sleep(0.25)
					IO.output(self.destinationpin,IO.LOW)
					sleep(0.25)
					i=i+1

#				motor_controller.turn("left")
#				x = 0.25 #time to turn for
#				sleep(x)
#				motor_controller.halt_turn()

				self.x3=9.318
				self.y3= -1.58
				self.targetnumber=3
			if math.fabs(self.x2-9.318) < 1 and math.fabs(self.y2+1.58) < 1 and self.targetnumber==3:
				print 'STOP AND TURN RIGHT!!!'
				i=0
				while i<5:
					IO.output(self.destinationpin,IO.HIGH)
					sleep(0.25)
					IO.output(self.destinationpin,IO.LOW)
					sleep(0.25)
					i=i+1

#				motor_controller.turn("left")
#				x = 0.25 #time to turn for
#				sleep(x)
#				motor_controller.halt_turn()

				self.x3=5.654
				self.y3= -4.017
				self.targetnumber=4
			if math.fabs(self.x2-5.654) < 1 and math.fabs(self.y2+4.017) < 1 and self.targetnumber==4:
				print 'STOP AND TURN RIGHT!!!'
				i=0
				while i<5:
					IO.output(self.destinationpin,IO.HIGH)
					sleep(0.25)
					IO.output(self.destinationpin,IO.LOW)
					sleep(0.25)
					i=i+1

#				motor_controller.turn("left")
#				x = 0.25 #time to turn for
#				sleep(x)
#				motor_controller.halt_turn()

				self.x3=2.396
				self.y3=0.125
				self.targetnumber=1
			if math.fabs(self.x2-2.396) < 1 and math.fabs(self.y2-0.125) < 1 and self.targetnumber==1:
				print 'STOP, you have reached the target destination'
				i=0
				while i<5:
					IO.output(self.destinationpin,IO.HIGH)
					sleep(0.25)
					IO.output(self.destinationpin,IO.LOW)
					sleep(0.25)
					i=1+1

#				motor_controller.turn("left")
#				x = 0.25 #time to turn for
#				sleep(x)
#				motor_controller.halt_turn()
