from marvelmind import MarvelmindHedge
import sys
from time import sleep

class currentposition():
	def __init__(self):
		self.hedge = MarvelmindHedge(tty = "/dev/ttyACM0", adr=16, debug=False) 
		self.hedge.start() #start thread

	def position(self):
		pos = self.hedge.position()
		return pos