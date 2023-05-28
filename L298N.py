"""
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Raspberry Pi Pico L298N Motor Driver Shiels (MicroPython)┃
┃                                                          ┃
┃ A Micropython or Python Library to coltorl motors using  ┃
┃ L298N motor driver shield. This library makes your codes ┃
┃ easier.You can use this library if want to make a Robot, ┃
┃ Car,Robot arm remote control car using Raspberry Pi Pico ┃
┃                                                          ┃
┃ Copyright (c) 2023 Ramji Patel                           ┃
┃ GitHub: https://github.com/ramjipatel041                 ┃
┃ License: Apache                                          ┃
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
"""

import time
from machine import Pin, PWM

class L298N:
    def __init__(self, ENA, IN1, IN2):
        self.IN1 = IN1
        self.IN2 = IN2
        self.ENA = ENA
        self.pwm = PWM(self.ENA)
        self.speed = 40000
        self.ismoving = False
        self.direction = 'STOP'
        self.time = 0
         
    def forward(self):
        self.IN1.value(1)
        self.IN2.value(0)
        self.ismoving =  True
        self.direction = 'FORWARD'
        
    def backward(self):
        self.IN1.value(0)
        self.IN2.value(1)
        self.ismoving = True
        self.direction = 'BACKWARD'
        
    def stop(self):
        self.IN1.value(0)
        self.IN2.value(0)
        self.ismoving = False
        self.Direction = 'STOP'
        
    def setSpeed(self, speed):
        self.pwm.freq(15000)
        self.speed = speed
        self.pwm.duty_u16(speed)
        
    def getSpeed(self):
        return self.speed
    
    def getDirection(self):
        return self.direction
    
    def run(self, direction):
        self.direction = direction
        if self.direction == 'FORWARD':
            self.forward()
        elif self.direction == 'BACKWARD':
            self.backward()
        elif self.direction == 'STOP':
            self.stop()
        else:
            pass
    
    def forwardFor(self, Time):
        self.time = Time
        self.forward()
        time.sleep(self.time)
        self.stop()
        
    def backwardFor(self, Time):
        self.time = Time
        self.backward()
        time.sleep(self.time)
        self.stop()
        
    def runFor(self, direction, Time):
        self.direction = direction
        self.time = Time
        if self.direction == 'FORWARD':
            self.forward()
            time.sleep(self.time)
            self.stop()
        elif self.direction == 'BACKWARD':
            self.backward()
            time.sleep(self.time)
            self.stop()
        elif self.direction == 'STOP':
            self.stop()
            time.sleep(self.time)
        else:
            pass
            
    def isMoving(self):
        if self.ismoving == True:
            print('True')
        elif self.ismoving == False:
            print('False')
        else:
            pass