import time
import RPi.GPIO as GPIO

class LED(object):
 def __init__(self):
  self.green_pin = 10
  self.blue_pin = 4
  self.red_pin = 17
  GPIO.setmode(GPIO.BCM)  
  GPIO.setup(self.green_pin, GPIO.OUT)
  GPIO.setup(self.blue_pin, GPIO.OUT)
  GPIO.setup(self.red_pin, GPIO.OUT)
  GPIO.output(self.green_pin, True)
  GPIO.output(self.blue_pin, True)
  GPIO.output(self.red_pin, True)
  print("led ready")

 def green_on(self):
  GPIO.output(self.green_pin, True)

 def greenr_off(self):
  GPIO.output(self.green_pin, False)

if __name__ == "__main__":
 l = LED()
 #l.green_on()
