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
    myid = threading.get_ident()
    print('star robot_thread()', myid)

    robot = RobotCar.RobotCar(pin)

    [idx_left, idx_right] = [0, 1]

    move_cmd = {\
                's':'stop', \
                'S':'break', \
                'w':'forward', \
                'x':'backward', \
                'a':'left', \
                'd':'right' \
    }

    move_stat = 'stop'
    robot.move('stop')
    
    while True:
        cmd = cmd_Q.get()

        if len(cmd) > 0:
            print(myid, '"'+cmd+'"')

        if cmd == ' ' or ord(cmd) < 20:
            robot.move('off')
            break

        ###
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

        ###
        if cmd in move_cmd.keys():
            move_stat = move_cmd[cmd]
            print(cmd, move_stat)
            robot.move(move_stat)

    robot = None
    print(myid, 'end')
           
#####
def readchar_thread():
    global inChar
    
    myid = threading.get_ident()
    print('start readchar_thread()', myid)

    while True:
        ch = readchar.readchar()
        print(myid, '"'+ch+'"')

        cmd_Q.put(ch)

        if ch == ' ' or ord(ch) <= 20:
            break

    print(myid, 'end')
    
#####
def main():
    robot_th = threading.Thread(target=robot_thread, daemon=True)
    robot_th.start()

    readchar_th = threading.Thread(target=readchar_thread, daemon=True)
    readchar_th.start()

    print('main()', threading.get_ident())
    
    print('join')
    #cmd_Q.join()
    robot_th.join()
    readchar_th.join()
    print('join done')
        

if __name__ == '__main__':
    main()
