import RPi.GPIO as IO
import time

IO.setmode(IO.BCM)
IO.setwarnings(False)

class ultrasonic():

	trigPin = 17
	echoPin = 27

	def __init__(self, trigPin, echoPin):
		self.trigPin = trigPin
		self.echoPin = echoPin
		IO.setup(self.trigPin, IO.OUT)
		IO.setup(self.echoPin, IO.IN)

	def trigsettle(self): 
		IO.output(self.trigPin, IO.LOW)
		#print("Waiting for sensor to settle..")
		time.sleep(0.01)

	def ping(self): 
		#print "Calculating distance..."
		IO.output(self.trigPin, IO.HIGH)
		time.sleep(0.0001)
		IO.output(self.trigPin, IO.LOW)

		while IO.input(self.echoPin) == 0:
			startTime = time.time()

		while IO.input(self.echoPin) == 1:
			endTime = time.time()

		duration = endTime - startTime
		distance = (duration * 34300) / 2
		if distance < 1000:
			print 'Distance:', distance, 'cm'
		else:
			print 'Bad ultrasonic data!'
		return distance # in cm
