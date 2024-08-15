import I2C_LCD_driver  # import the library
from time import sleep
import json
import os
import RPi.GPIO as GPIO  # import RPi.GPIO module

GPIO.setmode(GPIO.BCM)  # choose BCM mode
GPIO.setwarnings(False)

GPIO.setup(18, GPIO.OUT)  # Set GPIO 18 as output
PWM = GPIO.PWM(18, 100)  # Set 100Hz PWM output at GPIO 18


def payment_success():
    # Success tune: short ascending tones
    for freq in [500, 1000, 1500]:
        PWM.ChangeFrequency(freq)  # Change frequency to the desired tone
        PWM.start(50)  # Start PWM with 50% duty cycle
        sleep(0.2)  # Delay for 0.2 seconds
        PWM.stop()  # Stop the PWM signal
        sleep(0.1)  # Short delay between tones

def payment_failure():
    # Failure tune: descending tones
    for freq in [1500, 1000, 500]:
        PWM.ChangeFrequency(freq)  # Change frequency to the desired tone
        PWM.start(50)  # Start PWM with 50% duty cycle
        sleep(0.4)  # Delay for 0.4 seconds
        PWM.stop()  # Stop the PWM signal
        sleep(0.1)  # Short delay between tones


def buzzerSounds():
    GPIO.setup(18, GPIO.OUT)  # set GPIO 18 as output

    PWM = GPIO.PWM(18, 100)  # set 100Hz PWM output at GPIO 18

    while True:  # loops the next 3 lines
        for i in range(0, 101, 20):
            PWM.start(i)
            sleep(2)
    return



# LCD prins from LEFT->Right
def keypad():
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
    while True:
        for i in range(3):  # loop thru’ all columns
            GPIO.output(COL[i], 0)  # pull one column pin low
            for j in range(4):  # check which row pin becomes low
                if GPIO.input(ROW[j]) == 0:  # if a key is pressed
                    key_Pressed = MATRIX[j][i]
                    print(key_Pressed)  # print the key pressed
                    while GPIO.input(ROW[j]) == 0:  # debounce
                        sleep(0.1)
                    return key_Pressed
                    break
            GPIO.output(COL[i], 1)  # write back default value of 1



while True:
    try:
        LCD = I2C_LCD_driver.lcd()  # instantiate an lcd object, call it LCD
        sleep(0.5)
        LCD.backlight(0)  # turn backlight off
        sleep(0.5)
        LCD.backlight(1)  # turn backlight on
        #LCD.lcd_display_string("Address = 0x27", 2, 2)  # write on line 2
        # starting on 3rd column
        lcdDisplay  = []
        id = ''
        LCD.lcd_display_string('ID:')
        while True:
            key_pressed = keypad()

            if key_pressed:
                LCD.lcd_clear
                key_pressed = str(key_pressed)
                id += key_pressed
                LCD.lcd_display_string('ID:'+id)
                sleep(0.3)
            sleep(0.1)
            if len(id) == 5:

                filepath = f'purchases_user/{id}.json'
                if not os.path.exists(filepath):
                    file_exists = False

                    payment_failure()

                    LCD.lcd_clear()
                    LCD.lcd_display_string("ID not FOUND")
                    sleep(1)
                    break
                else:
                    file_exists = True
                    with open(filepath, mode='r') as file:
                     data = json.load(file)
                    LCD.lcd_clear()
                    total_cost = 0
                    for item in data:
                        name  = item['Name']
                        Quantity = item['Quantity']
                        price = item['Price']
                        Cost = item['Cost']
                        total_cost += float(Cost)

                        payment_success()

                        LCD.lcd_clear()
                        LCD.lcd_display_string(f'{name}',1)
                        LCD.lcd_display_string(f'Number Items: {Quantity}',2)
                        sleep(3)
                    LCD.lcd_clear()
                    LCD.lcd_display_string(f'TOTAL PRICE',1)
                    LCD.lcd_display_string(f'${total_cost}',2)
                    sleep(3)
                    break

    except KeyboardInterrupt:
        break
        print('Input ended')
    finally:
        LCD.lcd_clear()
        LCD.lcd_display_string("!DONE!")
