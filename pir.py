from machine import Pin
from time import sleep

# motion = pir.value()

# def handle_interrupt(pin):
#   global motion
#   motion = True
#   global interrupt_pin
#   interrupt_pin = pin 

led = Pin(23, Pin.OUT)
pir = Pin(5, Pin.IN)

# pir.irq(trigger=Pin.IRQ_RISING, handler=handle_interrupt)

# while True:
#   if motion:
#     print('Motion detected! Interrupt caused by:', interrupt_pin)
#     led.value(1)
#     sleep(5)
#     led.value(0)
#     print('Motion stopped!')
#     motion = False


old_value = pir.value()
while True:
  pir_value = pir.value()
  if pir_value:
    # PIR is detecting movement! Turn on LED. 
    led.value(1)
    # Check if this is the first time movement was # detected and print a message!
    if not old_value:
      print('Motion detected!') 
  else:
    # PIR is not detecting movement. Turn off LED. 
    led.value(0)
    # # Again check if this is the first time movement # stopped and print a message.
    if old_value:
      print('Motion ended!') 
  old_value = pir_value