"""
MicroPython driver for L298N Motor Driver module:
https://github.com/ramjipatel041/Micropython-Driver-for-L298N-Motor-Driver.git

L298N Datasheet:
https://www.st.com/en/motor-drivers/l298.html

MIT License
Copyright (c) 2023 Ramji Patel
Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

import time
from machine import Pin

class L298N:
    def __init__(self, ENA, IN1, IN2):
        self.IN1 = IN1
        self.IN2 = IN2
        self.pwm = ENA
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