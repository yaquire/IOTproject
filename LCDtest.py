import threading  # for threading
import time

import I2C_LCD_driver  # import the library
from time import sleep
import json
import RPi.GPIO as GPIO  # import RPi.GPIO module

GPIO.setmode(GPIO.BCM)  # choose BCM mode
GPIO.setwarnings(False)


def buzzerSounds():
    GPIO.setup(18, GPIO.OUT)  # set GPIO 18 as output

    PWM = GPIO.PWM(18, 100)  # set 100Hz PWM output at GPIO 18

    while True:  # loops the next 3 lines
        for i in range(0, 101, 20):
            PWM.start(i)
            sleep(2)


def keypad_Function():
    MATRIX = [[1, 2, 3], [4, 5, 6], [7, 8, 9], ["*", 0, "#"]]  # layout of keys on keypad
    ROW = [6, 20, 19, 13]  # row pins
    COL = [12, 5, 16]  # column pins
    # set column pins as outputs, and write default value of 1 to each
    for i in range(3):  # 0,1,2
        GPIO.setup(COL[i], GPIO.OUT)
        GPIO.output(COL[i], 1)
    # set row pins as inputs, with pull up
    for j in range(4):
        GPIO.setup(ROW[j], GPIO.IN, pull_up_down=GPIO.PUD_UP)
        # scan keypad
        for i in range(3):  # loop thru’ all columns
            GPIO.output(COL[i], 0)  # pull one column pin low
            for j in range(4):  # check which row pin becomes low
                if GPIO.input(ROW[j]) == 0:  # if a key is pressed
                    key_Pressed = MATRIX[j][i]
                    print(key_Pressed)  # print the key pressed
                    while GPIO.input(ROW[j]) == 0:  # debounce
                        sleep(0.1)
            GPIO.output(COL[i], 1)  # write back default value of

    return key_Pressed


def LCD_display(key_Pressed):
    LCD = I2C_LCD_driver.lcd()  # instantiate an lcd object, call it LCD
    sleep(0.5)
    LCD.backlight(0)  # turn backlight off
    sleep(0.5)
    LCD.backlight(1)  # turn backlight on
    # LCD.lcd_display_string("Address = 0x27", 2, 2)  # write on line 2
    # starting on 3rd column
    id = ''
    id += str(key_Pressed)
    printed = 'ID Number: '
    printed = printed + id
    if len(id) == 5: code = 'BREAK'
    return code, id
