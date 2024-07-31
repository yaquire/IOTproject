import I2C_LCD_driver  # import the library
from keypad import key_Pressed
from time import sleep
import json

LCD = I2C_LCD_driver.lcd()  # instantiate an lcd object, call it LCD
sleep(0.5)
LCD.backlight(0)  # turn backlight off
sleep(0.5)
LCD.backlight(1)  # turn backlight on
LCD.lcd_display_string("Press # to input customer ID", 1)  # write on line 1
#LCD.lcd_display_string("Address = 0x27", 2, 2)  # write on line 2
# starting on 3rd column
LCD.lcd_display_string(key_Pressed,2)

if key_Pressed == "#":
    LCD.lcd_clear()
    LCD.lcd_display_string("ID number: ",1)
    id = ''
    while True:
        if type(key_Pressed)!= str: key_Pressed=str(key_Pressed)
        id = id+key_Pressed
        if len(id) == 5: break
        print('Reached the max length of string')
    filepath = 'purchases_user/'+str(id)+'.json'
    with open(filepath, 'r') as file:
        data = json.load(file)
    file.close()

    totalPrice = 0
    for item in data:
        line = item['Name'] + 'No:'+item['Quantity']
        totalPrice += float(item['Cost'])
        LCD.lcd_display_string(line)
    LCD.lcd_display_string(totalPrice)

sleep(2)  # wait 2 sec
LCD.lcd_clear()  # clear the display
