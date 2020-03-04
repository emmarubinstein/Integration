import RPi.GPIO as IO

en = 12
en2 = 13

IO.setmode(IO.BCM)

IO.setup(en,IO.OUT)
IO.setup(en2,IO.OUT)

p1=IO.PWM(en,1000)
p2=IO.PWM(en2,1000)
p1.start(30)
p2.start(30)

while True:
	print('hey')

print('finished')