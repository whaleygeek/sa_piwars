from microbit import *

while True:
    sleep(100)
    x = accelerometer.get_x()
    if x < -200:
        print("L")
    if x > 200:
        print("R")
    
        