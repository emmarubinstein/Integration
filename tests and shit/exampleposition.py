from time import sleep
from Position import currentpos
addr = input("Who is we?")
myPos = currentpos(addr)

while True:
	myPos.position()
	sleep(.5)
	print'X:',myPos.position()[1], 'Y',myPos.position()[2]
