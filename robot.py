import time
import atexit
from Adafruit_MotorHAT import Adafruit_MotorHAT, Adafruit_DCMotor

# create a default object, no changes to I2C address or frequency
mh = Adafruit_MotorHAT(addr=0x60)

rightMotor = mh.getMotor(2)
leftMotor = mh.getMotor(1)

def stop():
        mh.getMotor(1).run(Adafruit_MotorHAT.RELEASE)
        mh.getMotor(2).run(Adafruit_MotorHAT.RELEASE)
        mh.getMotor(3).run(Adafruit_MotorHAT.RELEASE)
        mh.getMotor(4).run(Adafruit_MotorHAT.RELEASE)

def lf(speed=150, time_sec=0):
        leftMotor.setSpeed(speed)
        leftMotor.run(Adafruit_MotorHAT.FORWARD)
        if time_sec > 0:
            time.sleep(time_sec)

def lb(speed=150, time_sec=0):
        leftMotor.setSpeed(speed)
        leftMotor.run(Adafruit_MotorHAT.BACKWARD)
        if time_sec > 0:
            time.sleep(time_sec)

def rf(speed=150, time_sec=0):
        rightMotor.setSpeed(speed)
        rightMotor.run(Adafruit_MotorHAT.FORWARD)
        if time_sec > 0:
            time.sleep(time_sec)

def rb(speed=150, time_sec=0):
        rightMotor.setSpeed(speed)
        rightMotor.run(Adafruit_MotorHAT.BACKWARD)
        if time_sec > 0:
            time.sleep(time_sec)
