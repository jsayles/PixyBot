from pixy import *
from ctypes import *
import robot
import time

y_trigger_a = 180
y_speed_a = 150 
y_trigger_b = 160
y_speed_b = 205 
y_trigger_c = 140
y_speed_c = 255 

x_min = 100
x_mid = 180
x_max = 250

l_cal = 1.0
r_cal = 0.97

run_secs = 0.4

print ("Pixy Python Track Laser Example")

# Initialize Pixy Interpreter thread #
pixy_init()

class Blocks (Structure):
  _fields_ = [ ("type", c_uint),
               ("signature", c_uint),
               ("x", c_uint),
               ("y", c_uint),
               ("width", c_uint),
               ("height", c_uint),
               ("angle", c_uint) ]

class Robot():

    def drive(self, x, y, a):
        print ("drive(%d, %d, %d)" % (x,y,a))

        # Y controls speed
        if y >= y_trigger_a:
            speed = y_speed_a
        elif y >= y_trigger_b:
            speed = y_speed_b
        elif y >= y_trigger_c:
            speed = y_speed_b
        else:
            speed = 0
        #print("speed: %d" % speed)



        # X controls direction
        l_adjust = 1.0
        r_adjust = 1.0
        if x > x_min and x < x_mid:
            r_adjust = 1.0 * x / x_mid
            print ("r_adjust: %s" % r_adjust)
        elif x < x_max and x > x_mid: 
            l_adjust = 1.0 * (x - x_mid) / x_mid
            print ("l_adjust: %s" % l_adjust)
        l_speed = int(speed * l_cal * l_adjust)
        r_speed = int(speed * r_cal * r_adjust)

        # Go!
        robot.lf(speed=l_speed)
        robot.rf(speed=r_speed)
        time.sleep(run_secs)

    def stop(self):
	robot.stop()

robo = Robot()
    
blocks = BlockArray(100)

while 1:

  count = pixy_get_blocks(100, blocks)

  if count > 0:
    for index in range (0, count):
        if blocks[index].signature == 1:
            a = blocks[index].x * blocks[index].y
	    robo.drive(blocks[index].x, blocks[index].y, a)
            break

  robo.stop()
