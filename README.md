# Micorpython Driver for L298N Motor Driver module
This is a Micropython Driver for L298N motor driver module. This module reduces the programming complexity during using L298N module. You can now easily make your robots using L298N driver and Micropython.

## Builtin Functions
1. forward()
2. backward()
3. stop()
4. setSpeed()
5. getSpeed()
6. getDirection()
7. run()
8. forwardFor()
9. backwardFor()
10. runFor()
11. isMoving()
## Example codes for L298N_motor.py Micropython driver module
### Example-1:
```python
"""This micropython program makes the motor1 
move in forward and backward directions."""

from machine import Pin, PWM
from L298N_motor import L298N
import time

ENA = PWM(Pin(0))        
IN1 = Pin(1, Pin.OUT)         
IN2 = Pin(2, Pin.OUT)

motor1 = L298N(ENA, IN1, IN2)     #create a motor1 object
motor1.setSpeed(25000)            #set the speed of motor1. Speed value varies from 25000 to 65534

while True:
    motor1.forward()      #run motor1 forward
    time.sleep(5)         #wait for 5 seconds
    motor1.backward()     #run motor1 backward
    time.sleep(5)         #run motor2 backward
 ```
### Example-2:
```python
 """This micropython program makes the motor1 and motor2
move in forward and backward directions."""

from machine import Pin, PWM
from L298N_motor import L298N
import time

ENA = PWM(Pin(0))        
IN1 = Pin(1, Pin.OUT)         
IN2 = Pin(2, Pin.OUT)
IN3 = Pin(3, Pin.OUT)
IN4 = Pin(4, Pin.OUT)
ENB = PWM(Pin(5))

motor1 = L298N(ENA, IN1, IN2)     #create a motor1 object
motor2 = L298N(ENB, IN3, IN4)     #create a motor2 object

motor1.setSpeed(30000)            #set the speed of motor1. Speed value varies from 25000 to 65534
motor2.setSpeed(25000)            #set the speed of motor2. Speed value varies from 25000 to 65534

while True:
    motor1.forward()      #run motor1 forward
    motor2.forward()      #run motor2 forward
    time.sleep(5)         #wait for 5 seconds
    motor1.backward()     #run motor1 backward
    motor2.backward()     #run motor1 backward
    time.sleep(5)         #run motor2 backward
```   
### Example-3:
```python
"""This micropython program makes the motor1 
move in forward and backward directions with
increasing speed."""

from machine import Pin, PWM
from L298N_motor import L298N
import time

ENA = PWM(Pin(0))        
IN1 = Pin(1, Pin.OUT)         
IN2 = Pin(2, Pin.OUT)

motor1 = L298N(ENA, IN1, IN2)     #create a motor1 object
motor1.setSpeed(25000)            #set the speed of motor1. Speed value varies from 25000 to 65534

while True:
    for speed in range(25000, 65000, 100):
        motor1.setSpeed(speed)
        motor1.forward()
        time.sleep(0.1)
    motor1.stop()
    for speed in range(25000, 65000, 100):
        motor1.setSpeed(speed)
        motor1.backward()
        time.sleep(0.1)
    motor1.stop()
```   
### Example-4:
```python
"""This micropython program makes the motor1 
move in forward and backward directions with
increasing and and decreasing speed in both
directions."""

from machine import Pin, PWM
from L298N_motor import L298N
import time

ENA = PWM(Pin(0))        
IN1 = Pin(1, Pin.OUT)         
IN2 = Pin(2, Pin.OUT)

motor1 = L298N(ENA, IN1, IN2)     #create a motor1 object
motor1.setSpeed(25000)            #set the speed of motor1. Speed value varies from 25000 to 65534

while True:
    for speed in range(25000, 65000, 100):
        motor1.setSpeed(speed)
        motor1.forward()
        time.sleep(0.1)
    for speed in range(65000, 25000, -100):
        motor1.setSpeed(speed)
        motor1.forward()
        time.sleep(0.1)
    motor1.stop()
    for speed in range(25000, 65000, 100):
        motor1.setSpeed(speed)
        motor1.backward()
        time.sleep(0.1)
    for speed in range(65000, 25000, -100):
        motor1.setSpeed(speed)
        motor1.backward()
        time.sleep(0.1)
    motor1.stop()
 ```   
### Example-5:
```python
''' This is a micropython program to control the speed
and direction of the motor using seraial communication'''

from machine import Pin, PWM, UART
from L298N_motor import L298N
import time

uart = UART(1, 9600)
uart.init(9600, bits = 8, parity = None,stop = 1, rx = Pin(9), tx = Pin(8))

ENA = PWM(Pin(0))
IN1 = Pin(1, Pin.OUT)
IN2 = Pin(2, Pin.OUT)

motor1 = L298N(ENA, IN1, IN2)
motor1.setSpeed(30000)

while True:
    if uart.any() > 0:
        data = uart.read()
        print(data)
        if "FORWARD" in data:
            motor1.run("FORWARD")
        elif "BACKWARD" in data:
            motor1.run("BACKWARD")
        elif "STOP" in data:
            motor1.run("STOP")
        elif "SPEED" in data:
            uart.write(str(motor1.getSpeed()))
        elif "DIRECTION" in data:
            uart.write(str(motor1.getDirection()))
 ```    
### Example-6:
```python
''' This is a micropython program to control the
speed of motor1 using a potentiometer'''

from machine import Pin, PWM, ADC
from L298N_motor import L298N
import time

potentiometer = ADC(26)
ENA = PWM(Pin(0))        
IN1 = Pin(1, Pin.OUT)         
IN2 = Pin(2, Pin.OUT)

motor1 = L298N(ENA, IN1, IN2)

while True:
    reading = potentiometer.read_u16()
    motor1.setSpeed(int(reading))
    motor1.forward()
    time.sleep(0.1)
```
   
    


   
    
    


    





