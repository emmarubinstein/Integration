import RPi.GPIO as IO
from time import sleep

class Motorcontroller:
	def __init__(self, In1, In2, En, In3, In4, En2):
		# motor drive controller pins
		# motor 1
		self.In1 = In1
		self.In2 = In2
		self.En  = En
		# motor 2
		self.In3 = In3
		self.In4 = In4
		self.En2 = En2

		# speed1 is forward
		self.forward_backward_speed = 0
		self.left_right_speed = 0
	
		self.forward_backward_speed_limit = 0
		self.left_right_speed_limit = 0

		IO.setmode(IO.BCM)
		IO.setup(self.In1, IO.OUT)
		IO.setup(self.In2, IO.OUT)
		IO.setup(self.In3, IO.OUT)
		IO.setup(self.In4, IO.OUT)
		IO.setup(self.En, IO.OUT)
		IO.setup(self.En2, IO.OUT)
	
		self.p1 = IO.PWM(self.En, 100) #PMWs
		self.p2 = IO.PWM(self.En2, 100)

	def set_pin_mode(self, mode, In1, In2, En, In3, In4, En2):
		# 1 is forward, 2 is backward, 3 is hard-left, 4 is hard-right
		if mode == 1:
			IO.output(In1,IO.HIGH)
			IO.output(In2,IO.LOW)
			IO.output(In3,IO.HIGH)
			IO.output(In4,IO.LOW)
		elif mode == 2:
			IO.output(In1,IO.LOW)
			IO.output(In2,IO.HIGH)
			IO.output(In3,IO.LOW)
			IO.output(In4,IO.HIGH)
		elif mode == 3:
			IO.output(In1,IO.LOW)
			IO.output(In2,IO.HIGH)
			IO.output(In3,IO.HIGH)
			IO.output(In4,IO.LOW)
		elif mode == 4:
			IO.output(In1,IO.HIGH)
			IO.output(In2,IO.LOW)
			IO.output(In3,IO.LOW)
			IO.output(In4,IO.HIGH)
		else:
			print("mode != to anything idiot")

	def motor_controller_l(self, i):
		print('left @ ', i)
		self.p1.ChangeDutyCycle(i)

	def motor_controller_r(self, i):
		print('right @ ', i)
		self.p2.ChangeDutyCycle(i)

	def halt_turn(self, In1, In2, En, In3, In4, En2):
		# hard turns
		if self.forward_backward_speed == 0:
			if self.left_right_speed < 0:
				#hard left turn
				print('halting hard left')
				self.set_pin_mode(3)
				while self.left_right_speed < 0:
					sleep(0.020)
					self.left_right_speed += 1
					self.motor_controller_l(-1 * self.left_right_speed)
					self.motor_controller_r(-1 * self.left_right_speed)
			elif self.left_right_speed > 0:
				#hard right turn
				print('halting hard right')
				self.set_pin_mode(self.set_pin_mode(4))
				while self.left_right_speed > 0:
					sleep(0.020)
					self.left_right_speed -= 1
					self.motor_controller_l(self.left_right_speed)
					self.motor_controller_r(self.left_right_speed)
			else:
				print('not turning')
		# forward turns
		elif self.forward_backward_speed > 0:
			if self.left_right_speed < 0:
				#forward left turn
				print('halting forward left turn, resuming to forward')
				self.set_pin_mode(self.set_pin_mode(1))
				speed_offset = self.forward_backward_speed_limit - self.left_right_speed_limit
				while self.left_right_speed < 0:
					sleep(0.020)
					self.left_right_speed += 1
					self.motor_controller_l(speed_offset + (self.left_right_speed_limit - (-1 * self.left_right_speed)))
			elif self.left_right_speed > 0:
				#forward right turn
				print('halting forward right turn, resuming to forward')
				self.set_pin_mode(self.set_pin_mode(1))
				speed_offset = self.forward_backward_speed_limit - self.left_right_speed_limit
				while self.left_right_speed > 0:
					sleep(0.020)
					self.left_right_speed -= 1
					self.motor_controller_r(speed_offset + (self.left_right_speed_limit - self.left_right_speed))
			else:
				print('not turning')
		# backward turns
		elif self.forward_backward_speed < 0:
			if self.left_right_speed < 0:
				# backward left turn
				print('halting backward left turn, resuming to backward')
				self.set_pin_mode(self.set_pin_mode(2))
				speed_offset = self.forward_backward_speed_limit - self.left_right_speed_limit
				while self.left_right_speed < 0:
					sleep(0.020)
					self.left_right_speed += 1
					self.motor_controller_l(speed_offset + (self.left_right_speed_limit - (-1 * self.left_right_speed)))
			elif self.left_right_speed > 0:
				# backward right turn
				print('halting backward right turn, resuming to backward')
				self.set_pin_mode(self.set_pin_mode(2))
				speed_offset = self.forward_backward_speed_limit - self.left_right_speed_limit
				while self.left_right_speed > 0:
					sleep(0.020)
					self.left_right_speed -= 1
					self.motor_controller_r(speed_offset + (self.left_right_speed_limit - self.left_right_speed))
			else:
				print('not turning')

	def turn(self, direction, In1, In2, En, In3, In4, En2):
		if direction == "left":
			if self.left_right_speed < 0:
				print('already turning left')
			elif self.left_right_speed > 0:
				print('already turning right')
				self.halt_turn()
				self.turn("left")
			else:
				# hard left turn
				if self.forward_backward_speed == 0:
					print('starting hard left')
					self.set_pin_mode(self.set_pin_mode(3))
					while self.left_right_speed > (-1 * self.left_right_speed_limit):
						sleep(0.020)
						self.left_right_speed -= 1
						self.motor_controller_l(-1 * self.left_right_speed)
						self.motor_controller_r(-1 * self.left_right_speed)
				# forward left turn
				elif self.forward_backward_speed > 0:
					print('starting forward left turn')
					self.set_pin_mode(self.set_pin_mode(1))
					speed_offset = self.forward_backward_speed_limit - self.left_right_speed_limit
					while self.left_right_speed > (-1 * self.left_right_speed_limit):
						sleep(0.020)
						self.left_right_speed -= 1
						self.motor_controller_l(speed_offset + (self.left_right_speed_limit - (-1 * self.left_right_speed)))
				elif self.forward_backward_speed < 0:
					print('starting backward left turn')
					self.set_pin_mode(self.set_pin_mode(2))
					speed_offset = self.forward_backward_speed_limit - self.left_right_speed_limit
					while self.left_right_speed > (-1 * self.left_right_speed_limit):
						sleep(0.020)
						self.left_right_speed -= 1
						self.motor_controller_l(speed_offset + (self.left_right_speed_limit - (-1 * self.left_right_speed)))
		elif direction == "right":
			if self.left_right_speed > 0:
				print('already turning right')
			elif self.left_right_speed < 0:
				print('already turning left')
				self.halt_turn()
				self.turn("right")
			else:
				# hard right turn
				if self.forward_backward_speed == 0:
					print('starting hard right')
					self.set_pin_mode(self.set_pin_mode(4))
					while self.left_right_speed < self.left_right_speed_limit:
						sleep(0.020)
						self.left_right_speed += 1
						self.motor_controller_l(self.left_right_speed)
						self.motor_controller_r(self.left_right_speed)
				elif self.forward_backward_speed > 0:
					print('starting forward right turn')
					self.set_pin_mode(self.set_pin_mode(1))
					speed_offset = self.forward_backward_speed_limit - self.left_right_speed_limit
					while self.left_right_speed < self.left_right_speed_limit:
						sleep(0.020)
						self.left_right_speed += 1
						self.motor_controller_r(speed_offset + (self.left_right_speed_limit - self.left_right_speed))
				elif self.forward_backward_speed < 0:
					print('starting backward right turn')
					self.set_pin_mode(self.set_pin_mode(2))
					speed_offset = self.forward_backward_speed_limit - self.left_right_speed_limit
					while self.left_right_speed < self.left_right_speed_limit:
						sleep(0.020)
						self.left_right_speed += 1
						self.motor_controller_r(speed_offset + (self.left_right_speed_limit - self.left_right_speed))

	# stop forward or backward movement
	def halt_forward_backward(self, In1, In2, En, In3, In4, En2):
		if self.forward_backward_speed == 0:
			print('no forward or backward movement detected')
		elif self.left_right_speed == 0:
			# come to full stop
			if self.forward_backward_speed > 0:
				# stop from forward movement
				print('halting forward movement, coming to full stop')
				self.set_pin_mode(self.set_pin_mode(1))
				while self.forward_backward_speed > 0:
					sleep(0.020)
					self.forward_backward_speed -= 1
					self.motor_controller_l(self.forward_backward_speed)
					self.motor_controller_r(self.forward_backward_speed)
			elif self.forward_backward_speed < 0:
				# stop from backward movement
				print('halting backward movement, coming to full stop')
				self.set_pin_mode(self.set_pin_mode(2))
				while self.forward_backward_speed < 0:
					sleep(0.020)
					self.forward_backward_speed += 1
					self.motor_controller_l(-1 * self.forward_backward_speed)
					self.motor_controller_r(-1 * self.forward_backward_speed)
		elif self.left_right_speed > 0:
			# go into hard right
			if self.forward_backward_speed > 0:
				print('halting forward movement, going into hard right')
				self.set_pin_mode(self.set_pin_mode(1))
				speed_offset = self.forward_backward_speed_limit - self.left_right_speed_limit
				while self.forward_backward_speed > 0:
					self.forward_backward_speed -= 1
					self.motor_controller_l(self.forward_backward_speed)
					if (self.forward_backward_speed - speed_offset) > 0:
						self.motor_controller_r(self.forward_backward_speed - speed_offset)
				self.left_right_speed = 0
				self.turn("right")
			elif self.forward_backward_speed < 0:
				print('halting backward movement, going into hard right')
				self.set_pin_mode(self.set_pin_mode(2))
				speed_offset = self.forward_backward_speed_limit - self.left_right_speed_limit
 				while self.forward_backward_speed < 0:
					self.forward_backward_speed += 1
					self.motor_controller_l(-1 * self.forward_backward_speed)
					if ((-1 * self.forward_backward_speed) - speed_offset) > 0:
						self.motor_controller_r((-1 *self.forward_backward_speed) - speed_offset)
				self.left_right_speed = 0
				self.turn("right")
		elif self.left_right_speed < 0:
			# go into hard right
			if self.forward_backward_speed > 0:
				print('halting forward movement, going into hard left')
 				self.set_pin_mode(self.set_pin_mode(1))
				speed_offset = self.forward_backward_speed_limit - self.left_right_speed_limit
				while self.forward_backward_speed > 0:
					self.forward_backward_speed -= 1
					self.motor_controller_r(self.forward_backward_speed)
					if (self.forward_backward_speed - speed_offset) > 0:
						self.motor_controller_l(self.forward_backward_speed - speed_offset)
				self.left_right_speed = 0
				self.turn("left")
			elif self.forward_backward_speed < 0:
				print('halting backward movement, going into hard left')
				self.set_pin_mode(self.set_pin_mode(2))
				speed_offset = self.forward_backward_speed_limit - self.left_right_speed_limit
				while self.forward_backward_speed < 0:
					self.forward_backward_speed += 1
					self.motor_controller_r(-1 * self.forward_backward_speed)
					if ((-1 * self.forward_backward_speed) - speed_offset) > 0:
						self.motor_controller_l((-1 *self.forward_backward_speed) - speed_offset)
				self.left_right_speed = 0
				self.turn("left")

	def forward(self):
		if self.forward_backward_speed == 0:
			if self.left_right_speed == 0:
                		print('starting forward movement')
				self.set_pin_mode(self.set_pin_mode(1))
				while self.forward_backward_speed < self.forward_backward_speed_limit:
					sleep(0.020)
					self.forward_backward_speed += 1
					self.motor_controller_l(self.forward_backward_speed)
					self.motor_controller_r(self.forward_backward_speed)
			if (self.left_right_speed > 0) or (self.left_right_speed < 0):
				print('halting turn, going forward')
				self.halt_turn()
				self.forward()
		elif self.forward_backward_speed > 0:
			print('already going forward')
		elif self.forward_backward_speed < 0:
			print('going backward, need to halt backward movement first')
			self.halt_forward_backward()
 			self.forward()

	def backward(self, In1, In2, En, In3, In4, En2):
		if self.forward_backward_speed == 0:
			if self.left_right_speed == 0:
				print('starting backward movement')
				self.set_pin_mode(self.set_pin_mode(2))
				while self.forward_backward_speed > (-1 * self.forward_backward_speed_limit):
					sleep(0.020)
					self.forward_backward_speed -= 1
					self.motor_controller_l(-1 * self.forward_backward_speed)
					self.motor_controller_r(-1 * self.forward_backward_speed)
			if (self.left_right_speed > 0) or (self.left_right_speed < 0):
				print('halting turn, going backward')
				self.halt_turn()
				self.forward()
		elif self.forward_backward_speed > 0:
			print('going forward, need to halt forward movement first')
			self.halt_forward_backward()
			self.backward()
		elif self.forward_backward_speed < 0:
			print('already going backward')

