from marvelmind import MarvelmindHedge
from time import sleep

hedge = MarvelmindHedge(tty="/dev/ttyACM0",adr = 16, debug=False)
hedge.start()

while(1):
	pos_list = hedge.position_list()
	
	print(pos_list[0][1])
	print(pos_list[1][1])
	print(pos_list[2][1])

	sleep(0.5)