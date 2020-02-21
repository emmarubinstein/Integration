import RPi.GPIO as IO          
from time import sleep
import time
#===INITIALIZE PINS===#
in1 = 24
in2 = 23
en = 25
in3 =17
in4 = 27
en2 = 22
mode=1
IO.setmode(IO.BCM)
IO.setup(in1,IO.OUT)
IO.setup(in2,IO.OUT)
IO.setup(en,IO.OUT)
IO.setup(in3,IO.OUT)
IO.setup(in4,IO.OUT)
IO.setup(en2,IO.OUT)
IO.output(in1,IO.LOW)
IO.output(in2,IO.LOW)
IO.output(in3,IO.LOW)
IO.output(in4,IO.LOW)
p1=IO.PWM(en,1000)
p2=IO.PWM(en2,1000)
p1.start(30)
p2.start(30)
speed=30
print("\n")
print("The default setting of the motors is 50% power going forward.....")
print("g-go s-stop f-forward b-backward l-left r-right a-accelerate d-decelerate e-exit")
print("\n")    

while(1):

    x=raw_input()
#===GO===#    
    if x=='g':
        print("go")
	print(speed)
        if(mode==1):  
            IO.output(in1,IO.HIGH)
            IO.output(in2,IO.LOW)
            IO.output(in3,IO.HIGH)
            IO.output(in4,IO.LOW)
	    n=0
            p1.ChangeDutyCycle(0)
            p2.ChangeDutyCycle(0)
            while n<speed:
                time.sleep(.02)
                n=n+1
                p1.ChangeDutyCycle(n)
                p2.ChangeDutyCycle(n)
            print("forward")
            x='z'
        elif mode==2:	    
            IO.output(in1,IO.LOW)
            IO.output(in2,IO.HIGH)
            IO.output(in3,IO.LOW)
            IO.output(in4,IO.HIGH)
	    n=0
            p1.ChangeDutyCycle(0)
            p2.ChangeDutyCycle(0)
            while n<speed:
                time.sleep(.020)
                n=n+1
                p1.ChangeDutyCycle(n)
                p2.ChangeDutyCycle(n)
            print("backward")
            x='z'
        elif mode==3:
            IO.output(in1,IO.LOW)
            IO.output(in2,IO.HIGH)
            IO.output(in3,IO.HIGH)
            IO.output(in4,IO.LOW)
	    n=0
            p1.ChangeDutyCycle(0)
            p2.ChangeDutyCycle(0)
            while n<speed:
                time.sleep(.020)
                n=n+1
                p1.ChangeDutyCycle(n)
                p2.ChangeDutyCycle(n)
            print("left")
            x='z'
        else:
	    	
            IO.output(in1,IO.HIGH)
            IO.output(in2,IO.LOW)
            IO.output(in3,IO.LOW)
            IO.output(in4,IO.HIGH)
	    n=0
            p1.ChangeDutyCycle(0)
            p2.ChangeDutyCycle(0)
            while n<speed:
                time.sleep(.020)
                n=n+1
                p1.ChangeDutyCycle(n)
                p2.ChangeDutyCycle(n)
            print("right")
            x='z'

#===STOP====#
    elif x=='s':
        print("stop")
        IO.output(in1,IO.LOW)
        IO.output(in2,IO.LOW)
        IO.output(in3,IO.LOW)
        IO.output(in4,IO.LOW)
        x='z'

#===FORWARD===#
    elif x=='f':
        print("forward")
        IO.output(in1,IO.HIGH)
        IO.output(in2,IO.LOW)
        IO.output(in3,IO.HIGH)
        IO.output(in4,IO.LOW)
	n=0
        p1.ChangeDutyCycle(0)
        p2.ChangeDutyCycle(0)
        while n<speed:
            time.sleep(.020)
            n=n+1
            p1.ChangeDutyCycle(n)
            p2.ChangeDutyCycle(n)
        mode=1
        x='z'

#===REVERSE===#
    elif x=='b':
        print("backward")
        IO.output(in1,IO.LOW)
        IO.output(in2,IO.HIGH)
        IO.output(in3,IO.LOW)
        IO.output(in4,IO.HIGH)
	n=0
        p1.ChangeDutyCycle(0)
        p2.ChangeDutyCycle(0)
        while n<speed:
            time.sleep(.020)
            n=n+1
            p1.ChangeDutyCycle(n)
            p2.ChangeDutyCycle(n)
        mode=2
        x='z'

#===LEFT===#
    elif x=='l':
        print("left")
        IO.output(in1,IO.LOW)
        IO.output(in2,IO.HIGH)
        IO.output(in3,IO.HIGH)
        IO.output(in4,IO.LOW)
	n=0
        p1.ChangeDutyCycle(0)
        p2.ChangeDutyCycle(0)
        while n<speed:
            time.sleep(.020)
            n=n+1
            p1.ChangeDutyCycle(n)
            p2.ChangeDutyCycle(n)
        mode=3
        x='z'
        
#===RIGHT===#
    elif x=='r':
        print("right")
        IO.output(in1,IO.HIGH)
        IO.output(in2,IO.LOW)
        IO.output(in3,IO.LOW)
        IO.output(in4,IO.HIGH)
	n=0
        p1.ChangeDutyCycle(0)
        p2.ChangeDutyCycle(0)
        while n<speed:
            time.sleep(.020)
            n=n+1
            p1.ChangeDutyCycle(n)
            p2.ChangeDutyCycle(n)
        mode=4
        x='z'
        
#===ACCELERATE===#
    elif x=='a':
        print("acclerate")
        speed=speed+5
        p1.ChangeDutyCycle(speed)
        p2.ChangeDutyCycle(speed)
        time.sleep(.100)
        speed=speed+5
        p1.ChangeDutyCycle(speed)
        p2.ChangeDutyCycle(speed)
        print(speed)
        x='z'
        
#===DECELERATE===#
    elif x=='d':
        print("decelerate")
        speed=speed-5
        p1.ChangeDutyCycle(speed)
        p2.ChangeDutyCycle(speed)
        time.sleep(.100)
        speed=speed-5
        p1.ChangeDutyCycle(speed)
        p2.ChangeDutyCycle(speed)
        print(speed)
        x='z'

    elif x=='e':
        IO.cleanup()
        break
    
    else:
        print("<<<  wrong data  >>>")
        print("please enter the defined data to continue.....")
