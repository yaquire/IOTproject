import os
import time
from time import sleep
import multiprocessing
import json
key_Pressed = ''
id = ''

def clear_terminal():
    os.system('clear')


def display_Input():  # emulates keypad
    print('Thing in is;', key_Pressed)
    return


def keypad():  # emulates keypad
    global key_Pressed
    thing_in = 4
    print('Input =', thing_in)
    key_Pressed = thing_in
    print(key_Pressed)
    return




if __name__ == '__main__':
    startTimer = time.perf_counter()
    process_Keypad = multiprocessing.Process(target=keypad)
    process_Display = multiprocessing.Process(target=display_Input)

    process_Keypad.start()
    process_Keypad.join()
    print(key_Pressed)
    process_Display.start()
    process_Display.join()

    endtime = time.perf_counter()
    print(f'Finished in {endtime} second(s)\n ID: {id}')
