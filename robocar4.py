#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import RobotCar
import VL53L0X
import threading
import queue
import readchar

pin = [13, 12]

cmd_Q = queue.Queue()

#####
def robot_thread():
    print('star robot_thread()', threading.get_ident())

    [idx_left, idx_right] = [0, 1]

    robot = RobotCar.RobotCar(pin)

    move_stat = 'stop'
    robot.move('stop')
    
    while True:
        cmd = cmd_Q.get()
        print(threading.get_ident(), '"'+cmd+'"')

        if cmd == ' ' or ord(cmd) < 20:
            break

        if cmd == 'z':
            robot.increment_pulse_val(move_stat, idx_left, -5)
            robot.move(move_stat)
        if cmd == 'q':
            robot.increment_pulse_val(move_stat, idx_left, 5)
            robot.move(move_stat)
        if cmd == 'e':
            robot.increment_pulse_val(move_stat, idx_right, -5)
            robot.move(move_stat)
        if cmd == 'c':
            robot.increment_pulse_val(move_stat, idx_right, 5)
            robot.move(move_stat)
           

#####
def main():
    robot_th = threading.Thread(target=robot_thread)
    robot_th.start()

    print('main()', threading.get_ident())
    
    while True:
        ch = readchar.readchar()
        print(threading.get_ident(), '"'+ch+'"')
        
        cmd_Q.put(ch)

        if ch == ' ' or ord(ch) <= 20:
            break

    print('join')
    robot_th.join()
        

if __name__ == '__main__':
    main()
