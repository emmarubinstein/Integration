from marvelmind import MarvelmindHedge
from time import sleep
import sys
from math import sqrt, pow, acos, degrees

class trig():

	def angle(self, xOrig, yOrig, xCurrent, yCurrent):
		### theta 1 ####
		self.yDiff= yCurrent-yOrig
		self.xDiff= xCurrent-xOrig

		ySquared = pow(self.yDiff,2)
		xSquared = pow(self.xDiff,2)

		self.mag = sqrt(ySquared + xSquared)

		if self.mag == 0:
			self.mag = 0.0001
			
		angle = degrees(acos(self.xDiff/self.mag))

		return angle









#		### theta 2 ###
#		self.xDiff2 = xFinal - xCurrent
#		self.yDiff2 = yFinal - yCurrent
#
#		#ySquared2 = pow(self.yDiff2, 2)
#		#xSquared2 = pow(self.xDiff2, 2)
#
#		self.mag2 = sqrt(ySquared2 + xSquared2)
#		if self.mag2 == 0:
#			self.mag2 = 0.0001
#
#		angle2 = degrees(acos(self.xDiff2/self.mag2))
#
#		angle3 = angle2 - angle
#
#		return angle3
#		
#