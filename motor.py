# motor.py  30 March 2017  D.J.Whale
#
# Example of driving 4 motors from a Raspberry Pi
# Using 4tronix (camjam) motor controller H bridge board

# MOTOR B - normal controller
BACK_RIGHT_B = 7
BACK_RIGHT_F = 8

# MOTOR A - normal controller
FRONT_RIGHT_B = 9
FRONT_RIGHT_F = 10

# MOTOR B - extra controller
BACK_LEFT_B  = 22 # 7
BACK_LEFT_F  = 23 # 8

# MOTOR A - extra controller
FRONT_LEFT_B  = 24 # 9
FRONT_LEFT_F  = 25 # 10

import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)

GPIO.setup(BACK_RIGHT_B,  GPIO.OUT)
GPIO.setup(BACK_RIGHT_F,  GPIO.OUT)
GPIO.setup(FRONT_RIGHT_B, GPIO.OUT)
GPIO.setup(FRONT_RIGHT_F, GPIO.OUT)

GPIO.setup(BACK_LEFT_B,   GPIO.OUT)
GPIO.setup(BACK_LEFT_F,   GPIO.OUT)
GPIO.setup(FRONT_LEFT_B,  GPIO.OUT)
GPIO.setup(FRONT_LEFT_F,  GPIO.OUT)


def move_forward():
	GPIO.output(BACK_RIGHT_B,  False)
	GPIO.output(BACK_RIGHT_F,  True)
	GPIO.output(FRONT_RIGHT_B, False)
	GPIO.output(FRONT_RIGHT_F, True)
	GPIO.output(BACK_LEFT_B,   False)
	GPIO.output(BACK_LEFT_F,   True)
	GPIO.output(FRONT_LEFT_B,  False)
	GPIO.output(FRONT_LEFT_F,  True)

def move_backward():
	GPIO.output(BACK_RIGHT_B,  False)
	GPIO.output(BACK_RIGHT_F,  False)
	GPIO.output(FRONT_RIGHT_B, False)
	GPIO.output(FRONT_RIGHT_F, False)
	GPIO.output(BACK_LEFT_B,   False)
	GPIO.output(BACK_LEFT_F,   False)
	GPIO.output(FRONT_LEFT_B,  False)
	GPIO.output(FRONT_LEFT_F,  False)

def turn_left():
	GPIO.output(BACK_RIGHT_B,  False)
	GPIO.output(BACK_RIGHT_F,  False)
	GPIO.output(FRONT_RIGHT_B, False)
	GPIO.output(FRONT_RIGHT_F, False)
	GPIO.output(BACK_LEFT_B,   False)
	GPIO.output(BACK_LEFT_F,   False)
	GPIO.output(FRONT_LEFT_B,  False)
	GPIO.output(FRONT_LEFT_F,  False)

def turn_right():
	GPIO.output(BACK_RIGHT_B,  False)
	GPIO.output(BACK_RIGHT_F,  False)
	GPIO.output(FRONT_RIGHT_B, False)
	GPIO.output(FRONT_RIGHT_F, False)
	GPIO.output(BACK_LEFT_B,   False)
	GPIO.output(BACK_LEFT_F,   False)
	GPIO.output(FRONT_LEFT_B,  False)
	GPIO.output(FRONT_LEFT_F,  False)

def stop():
	GPIO.output(BACK_RIGHT_B,  False)
	GPIO.output(BACK_RIGHT_F,  False)
	GPIO.output(FRONT_RIGHT_B, False)
	GPIO.output(FRONT_RIGHT_F, False)
	GPIO.output(BACK_LEFT_B,   False)
	GPIO.output(BACK_LEFT_F,   False)
	GPIO.output(FRONT_LEFT_B,  False)
	GPIO.output(FRONT_LEFT_F,  False)

#stop()

try:
    while True:
        raw_input("ENTER for forward")
        move_forward()

        #raw_input("ENTER for backward")
        #move_backward()

        #raw_input("ENTER for left")
        #turn_left()

        #raw_input("ENTER for right")
        #turn_right()

        raw_input("ENTER for stop")
        stop()
finally:
    stop()
    GPIO.cleanup()








