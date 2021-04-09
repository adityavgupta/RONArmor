# Name: pir.py
# Functionality: Controls the PIR sensors based on the interrupt recieved 
from machine import Pin
from time import sleep

motion = False
LED_PIN_1 = 23

PIR_PIN_1 = 12
PIR_PIN_2 = 13
PIR_PIN_3 = 14
PIR_PIN_4 = 15

def handle_interrupt(pin):
  global motion
  motion = True
  global interrupt_pin
  interrupt_pin = pin 

led = Pin(LED_PIN_1, Pin.OUT)
pir1 = Pin(PIR_PIN_1, Pin.IN)
pir2 = Pin(PIR_PIN_2, Pin.IN)
pir3 = Pin(PIR_PIN_3, Pin.IN)
pir4 = Pin(PIR_PIN_4, Pin.IN)

pir1.irq(trigger=Pin.IRQ_RISING, handler=handle_interrupt)
pir2.irq(trigger=Pin.IRQ_RISING, handler=handle_interrupt)
pir3.irq(trigger=Pin.IRQ_RISING, handler=handle_interrupt)
pir4.irq(trigger=Pin.IRQ_RISING, handler=handle_interrupt)

try:
  while True:
    if motion:
      print('Motion detected! Interrupt caused by:', interrupt_pin)
      led.value(1)
      sleep(1)
      led.value(0)
      print('Motion stopped!')
      motion = False
except:
  print('nothing')