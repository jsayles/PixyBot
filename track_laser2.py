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

a_trigger_reverse = 0.10

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

    training_loops = 100
    trained_loops = 0
    x_min = 0
    x_max = 0
    y_min = 0
    y_max = 0
    a_min = 0
    a_max = 0
   

    def train(self, x, y, a):
        if self.trained_loops >= self.training_loops:
            print("X: %d-%d, Y: %d-%d, A: %d-%d" % (self.x_min, self.x_max, self.y_min, self.y_max, self.a_min, self.a_max))
            return True
        print ("train(%d, %d, %d)" % (x,y,a))
        if self.trained_loops == 0:
            self.x_min = self.x_max = x
            self.y_min = self.y_max = y
            self.a_min = self.a_max = a
        else:
           if x < self.x_min:
               self.x_min = x
           if x > self.x_max:
               self.x_max = x
           if y < self.y_min:
               self.y_min = y
           if y > self.y_max:
               self.y_max = y
           if a < self.a_min:
               self.a_min = a
           if a > self.a_max:
               self.a_max = a
        self.trained_loops = self.trained_loops + 1


    def drive(self, x, y, a):
        if not self.train(x, y, a):
            return
        print ("drive(%d, %d, %d)" % (x,y,a))

        # Y controls speed
        #if y >= y_trigger_a:
        #    speed = y_speed_a
        #elif y >= y_trigger_b:
        #    speed = y_speed_b
        #elif y >= y_trigger_c:
        #    speed = y_speed_b
        #else:
        #    speed = 0
        #print("speed: %d" % speed)

        # A controls speed
        reverse_trigger = self.a_min * a_trigger_reverse
        if a < reverse_trigger:
            speed = -150
        else:
            close_percentage = 1.0 * a / self.a_max
            speed = int(255 * close_percentage)

        # X controls direction
        l_adjust = 1.0
        r_adjust = 1.0
        if x > self.x_min and x < (self.x_max / 2):
            r_adjust = 1.0 * x / (self.x_max / 2)
        elif x < self.x_max and x > (self.x_max / 2):
            l_adjust = 1.0 * (x - (self.x_max / 2)) / (self.x_max / 2)

        # Use our adjustments to calcualte the speed of each wheel
        l_speed = int(speed * l_cal * l_adjust)
        r_speed = int(speed * r_cal * r_adjust)
        print("speed: %d, l_adjust: %s, r_adjust: %s" % (speed, l_adjust, r_adjust))

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
