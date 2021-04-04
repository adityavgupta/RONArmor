from machine import Pin
import time

ldr = Pin(0, Pin.IN)  # create input pin on GPIO2
while True:
    if ldr.value():
        print('Object Detected')      # get value, 0 or 1
    else:
        print('All clear')
	time.sleep(1)
