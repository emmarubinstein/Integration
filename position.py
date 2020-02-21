from time import sleep
from positionclass import currentposition

pos = currentposition()

while True: 
	pos.position()
	sleep(0.5)
	print 'X:',pos.position()[1], ' Y:',pos.position()[2]