#!/usr/bin/python

from pynput import keyboard
from PCA9685 import PCA9685
import time
Dir = [
    'forward',
    'backward',
]
pwm = PCA9685(0x40, debug=True)
pwm.setPWMFreq(50)
class MotorDriver():
    def __init__(self):
        self.PWMA = 0
        self.AIN1 = 1
        self.AIN2 = 2
        self.PWMB = 5
        self.BIN1 = 3
        self.BIN2 = 4

    def MotorRun(self, motor, index, speed):
        if speed > 100:
            return
        if(motor == 0):
            pwm.setDutycycle(self.PWMA, speed)
            if(index == Dir[0]):
                pwm.setLevel(self.AIN1, 0)
                pwm.setLevel(self.AIN2, 1)
            else:
                pwm.setLevel(self.AIN1, 1)
                pwm.setLevel(self.AIN2, 0)
        else:
            pwm.setDutycycle(self.PWMB, speed)
            if(index == Dir[0]):
                pwm.setLevel(self.BIN1, 1)
                pwm.setLevel(self.BIN2, 0)
            else:
                pwm.setLevel(self.BIN1, 0)
                pwm.setLevel(self.BIN2, 1)

    def MotorStop(self, motor):
        if (motor == 0):
            pwm.setDutycycle(self.PWMA, 0)
        else:
            pwm.setDutycycle(self.PWMB, 0)


try:
    Motor = MotorDriver()
    # control 2 motor
    #Motor.MotorRun(0, 'forward', 100)
    #Motor.MotorRun(1, 'forward', 100)
    print("start")
    while(1):
        with keyboard.Events() as events:
    	# Block for as much as possible
            event = events.get(1e6)
            if event.key == keyboard.KeyCode.from_char('w'):
                print('forward')
                Motor.MotorRun(0, 'forward', 100)
                Motor.MotorRun(1, 'forward', 100)
            if event.key == keyboard.KeyCode.from_char('s'):
                print('backward')
                Motor.MotorRun(0, 'backward', 100)
                Motor.MotorRun(1, 'backward', 100)
            if event.key == keyboard.KeyCode.from_char('a'):
                print('left')
                Motor.MotorRun(0, 'forward', 0)
                Motor.MotorRun(1, 'forward', 100)
            if event.key == keyboard.KeyCode.from_char('d'):
                print('right')
                Motor.MotorRun(0, 'forward', 100)
                Motor.MotorRun(1, 'forward', 0)
            if event.key == keyboard.KeyCode.from_char('q'):
                print('stop')
                Motor.MotorRun(0, 'forward', 0)
                Motor.MotorRun(1, 'forward', 0)

except IOError as e:
    print(e)
    
except KeyboardInterrupt:    
    print("\r\nctrl + c:")
    Motor.MotorRun(0, 'forward', 0)
    Motor.MotorRun(1, 'forward', 0)
    exit()

