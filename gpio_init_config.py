#! /usr/bin/env python


import RPi.GPIO as p 

p.setwarnings(False)

p.setmode(p.BCM)

p.setup(12,p.OUT)
p.setup(13,p.OUT)
p.setup(5,p.OUT)
p.setup(6,p.OUT)
p.setup(1,p.OUT)
p.setup(7,p.OUT)

p.output(12,p.LOW)
p.output(13,p.LOW)
p.output(5,p.LOW)
p.output(6,p.LOW)
p.output(1,p.LOW)
p.output(7,p.LOW)

p.cleanup()

print("init done: gpio set low")

