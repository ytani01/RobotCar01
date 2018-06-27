#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pigpio
import CR_Servo

import os
import sys
import time

#####
class RobotCar:
    CONF_FILENAME = 'robot_car.ini'
    DEF_CONF_FILE = os.environ['HOME']+'/'+CONF_FILENAME

    DEF_PULSE = { \
            'stop':     [1480,1480], \
            'forward':  [1580,1380], \
            'backward': [1380,1580], \
            'left':     [1580,1580], \
            'right':    [1380,1380]   }

    def __init__(self, pi, pin):
        self.pi = pi
        self.pin = pin
        self.n = len(pin)

        self.pulse = RobotCar.DEF_PULSE

        self.cr_servo = CR_Servo.CR_Servo_N(self.pi, self.pin)

    def set_pulse(self, pulse, sec=0.0):
        self.cr_servo.set_pulse(pulse, sec)
        if sec > 0.0:
            time.sleep(sec)

    def move(self, key, sec=0.0):
        self.set_pulse(self.pulse[key])
        if sec > 0.0:
            time.sleep(sec)

    def conf_load(self, conf_file):
        pass

    def conf_save(self, conf_file):
        pass


#####
def main1(pi):
    pin = [12, 13]

    robot = RobotCar(pi, pin)
    print('robot:\n', robot.__dict__)

    robot.move('forward', 0.1)
    robot.move('stop', 1)
    robot.move('backward', 0.1)
    robot.move('stop', 1)
    robot.move('left', 0.1)
    robot.move('stop', 1)
    robot.move('right', 0.1)
    robot.move('stop')

if __name__ == '__main__':
    pi = pigpio.pi()
    try:
        main1(pi)
    finally:
        pi.stop()
