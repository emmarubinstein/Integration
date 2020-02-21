from marvelmind import Marverlmindhedge
from time import sleep
import sys
from positionlesting2 import postion

hedge = MarvelmindHedge(tty = "/dev/ttyACM0" , adr =16 , debug = False)
hedge.start()
while True:
	try:
		sleep(1) # print (hedge.position()) # get last position and print
		hedge.print_position()

			if pos[0] == x:	
				print("x coordinate is found")
			if pos[0] < x:
				print("move in the +x direction")
			if pos[0] > x: 
				print("move in the -x direction")
			if pos[1] == y:
				print("y coordinate is found")
			if pos[1] < y:
				print("move in the +y direction")
			if pos[1] > y: 
				print("move in the -y direction")

			if pos[2] == z:
				print("z coordinate is found")
			if pos[2] < z:
				print("move in the +z direction")
			if pos[2] > z:
				print("move in the -z direction")

	    	
        	except KeyboardInterrupt:
			hedge.stop()  # stop and close serial port
			sys.exit()