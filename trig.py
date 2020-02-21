from marvelmind import MarvelmindHedge
from time import sleep
import sys
from trigclass import trig

trig = trig()

x1 = 0
y1 = 0
x2 = .6
y2 = .5
x3 = 1
y3 = 1

angle = trig.angle(x1, y1, x2, y2)

angle2 = trig.angle(x2,y2,x3,y3)

angle3 = angle2-angle

print(angle3)


