#!/usr/bin/python

import curses
from PCA9685 import PCA9685
import time
Dir = [
    'forward',
    'backward',
]
pwm = PCA9685(0x40, debug=True)
pwm.setPWMFreq(200) # for servo 50Hz(20ms), for DC-motor 200Hz(5ms)
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



def main(stdscr):
    Motor = MotorDriver()
    speed = 70
    # do not wait for input when calling getch
    stdscr.nodelay(1)
    while True:
        # get keyboard input, returns -1 if none available
        c = stdscr.getch()
        if c != -1:
            # print numeric value
            stdscr.addstr(str(c) + ' ')
            stdscr.refresh()
            # return curser to start position
            stdscr.move(0, 0)
            if c == ord('w') or c == 259: # w or up key
                print('forward')
                Motor.MotorRun(0, 'forward', speed)
                Motor.MotorRun(1, 'forward', speed)
            if c == ord('s') or c == 258: # s or down key
                print('backward')
                Motor.MotorRun(0, 'backward', speed)
                Motor.MotorRun(1, 'backward', speed)
            if c == ord('a') or c == 260:  # a or left key
                print('left')
                Motor.MotorRun(0, 'forward', 0)
                Motor.MotorRun(1, 'forward', speed)
            if c == ord('d') or c == 261: # d or right key
                print('right')
                Motor.MotorRun(0, 'forward', speed)
                Motor.MotorRun(1, 'forward', 0)
            if c == ord('q') or c == ord(' '): # q or space key
                print('stop')
                Motor.MotorRun(0, 'forward', 0)
                Motor.MotorRun(1, 'forward', 0)
            if c == 3:              # ctrl-c key
                print('bye')
                Motor.MotorRun(0, 'forward', 0)
                Motor.MotorRun(1, 'forward', 0)
                break
            if c == ord('z'):   # z key (speed down)
                speed = speed - 10
                if speed <= 10:
                   speed = 10
                print("Speed down")
            if c == ord('x'):   # x key (speed up)
                speed = speed + 10
                if speed >= 100:
                   speed = 100
                print("Speed up")

if __name__ == '__main__':
    curses.wrapper(main)


