import time
import RPi.GPIO as GPIO

RED1 = 27
GREEN1 = 4
BLUE1 = 17

RED2 = 23
GREEN2 = 24
BLUE2 = 25

class LED(object):
 def __init__(self, r, g, b):
  self.red_pin = r
  self.green_pin = g
  self.blue_pin = b

  GPIO.setmode(GPIO.BCM)
  GPIO.setwarnings(False)

  GPIO.setup(self.green_pin, GPIO.OUT)
  GPIO.setup(self.blue_pin, GPIO.OUT)
  GPIO.setup(self.red_pin, GPIO.OUT)

  self.all_off()
  #print("led ready")

 def all_off(self):
  self.red_off()
  self.green_off()
  self.blue_off()
 
 def red_on(self):
  GPIO.output(self.red_pin, False)

 def red_off(self):
  GPIO.output(self.red_pin, True)

 def green_on(self):
  GPIO.output(self.green_pin, False)

 def green_off(self):
  GPIO.output(self.green_pin, True)

 def blue_on(self):
  GPIO.output(self.blue_pin, False)

 def blue_off(self):
  GPIO.output(self.blue_pin, True)

led1 = LED(RED1, GREEN1, BLUE1)
led2 = LED(RED2, GREEN2, BLUE2)

if __name__ == "__main__":
 print("Testing LED1")
 led1.all_off()
 led1.red_on()
 time.sleep(1)
 led1.all_off()
 led1.green_on()
 time.sleep(1)
 led1.all_off()
 led1.blue_on()
 time.sleep(1)
 led1.all_off()

 print("Testing LED2")
 led2.all_off()
 led2.red_on()
 time.sleep(1)
 led2.all_off()
 led2.green_on()
 time.sleep(1)
 led2.all_off()
 led2.blue_on()
 time.sleep(1)
 led2.all_off()
