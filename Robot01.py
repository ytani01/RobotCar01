#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pigpio

import os
import sys
import csv

#####
class Robot01:
    DEF_CONF_FILENAME = 'robot.csv'
    DEF_CONF_FILE = os.environ['HOME']+'/'+DEF_CONF_FILENAME

    DEF_MOTOR_VAL = { 'off':      [0,0], \
                      'stop':     [1480,1480], \
                      'break':    [1480,1480], \
                      'forward':  [1580,1380], \
                      'backward': [1380,1580], \
                      'left':     [1580,1580], \
                      'right':    [1380,1380]   }

    def __init__(self, pin):
        self.pi = pigpio.pi()
        self.pin = pin
        self.n = len(pin)

        self.motor_val = Robot01.DEF_MOTOR_VAL

        self.move('off')

    def __del__(self):
        print("__del__()")
        self.pi.stop()

    ###
    def move(self, key, sec=0.0):
        self.set_motor(self.motor_val[key])
        if sec > 0.0:
            time.sleep(sec)

    def set_motor(self, motor_val):
        for i in range(self.n):
            print(i, '<-', motor_val[i])


    ###
    def conf_load(self, conf_file=''):
        if conf_file == '':
            conf_file = Robot01.DEF_CONF_FILE
        print('conf_file =', conf_file)

        with open(conf_file, 'r', encoding='utf-8') as conf_f:
            csv_reader = csv.reader(conf_f, delimiter=',', quotechar='"')
            for row in csv_reader:
                if len(row) < 2:
                    print('empty')
                    continue
                print(row, row[0], row[0][0:1])
                if row[0][0:1] == '#':
                    print('ignore')
                    continue

                self.motor_val[row[0].lower()] = [int(row[1]), int(row[2])]

        print(self.motor_val)
        

    def conf_save(self, conf_file):
        print('conf_file =', conf_file)


#####
def main():
    pin = [12, 13]

    robot = Robot01(pin)
    
    robot.conf_load()

    robot.move('forward')


if __name__ == '__main__':
    try:
        main()
    finally:
        print('=== finally ===')
