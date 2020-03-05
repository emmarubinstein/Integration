import RPi.GPIO as IO


class motorcontrol():

		
	def __init__(self, In1, In2, En, In3, In4, En2):
		self.In1 = In1
		self.In2 = In2
		self.In3 = In3
		self.In4 = In4
		self.En  = En
		self.En2 = En2
		
		self.speed1 = 0
		self.speed2 = 0
		
		self.dir1 = 1 # 1 = forward, 0 = back
		self.dir2 = 1

		self.p1 = IO.PWM(   #self.En, 100)
		self.p2 = IO.PWM(   #self.En2, 100)

	def setup(self):
		IO.setmode(IO.BCM)
		IO.setup(self.In1, IO.OUT)
		IO.setup(self.In2, IO.OUT)
		IO.setup(self.In3, IO.OUT)
		IO.setup(self.In4, IO.OUT)
		IO.setup(self.En, IO.OUT)
		IO.setup(self.En2, IO.OUT)

		self.p1 = IO.PWM(self.En, 100) #PMWs
		self.p2 = IO.PWM(self.En2, 100)

	
	def changeSpeed(self, speed, motor_num):


	def run(self):
		
		self.p1.ChangeDutyCycle(speed)
		self.p2.ChangeDutyCycle(speed)


		if self.dir1 == 1: #FORWARD
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
			return forward

		elif self.dir1 == #????: #STOP
			IO.output(in1, IO.LOW)
			IO.output(in2, IO.LOW)
			IO.output(in3, IO.LOW)
			IO.output(in4, IO.LOW)

		elif self.dir1 == : #BACKWARD
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

		elif self.dir1 == : #RIGHT
			IO.output(in1, IO.HIGH)
			IO.output(in2, iO.LOW)
			IO.output(n3, IO.LOW)
			IO.output(in4, IO.HIGH)
			n=0
			p1.ChangeDutyCycle(0)
			p2.ChangeDutyCycle(0)
			while n<speed:
				time.sleep(0.02)
				n=n+1
				p1.ChangeDutyCycle(n)
				p2.ChangeDutyCycle(n)

		elif self.dir1 == : #LEFT
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



		
		if self.dir2 == 1: # forward
		else self.dri2 == 0: # backword	
			


	