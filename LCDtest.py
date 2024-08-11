import I2C_LCD_driver #import the library
from time import sleep
li = [1,2,3,4]
LCD = I2C_LCD_driver.lcd() #instantiate an lcd object, call it LCD
sleep(0.5)
LCD.backlight(0) #turn backlight off
sleep(0.5)
LCD.backlight(1) #turn backlight on 
LCD.lcd_display_string("LCD Display Test", 1) #write on line 1
LCD.lcd_display_string(str(li))
                #starting on 3rd column

sleep(2) #wait 2 sec
LCD.lcd_clear() #clear the display
