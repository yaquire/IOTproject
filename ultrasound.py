import csv
import RPi.GPIO as GPIO # type: ignore
import time
import os
from datetime import datetime

# Define the GPIO pins
TRIG_PIN = 25
ECHO_PIN = 27

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(TRIG_PIN,GPIO.OUT) #GPIO25 as Trig
GPIO.setup(ECHO_PIN,GPIO.IN) #GPIO27 as Echo

# ChatGPT gave me the values for this color parts & told me how to add colour
RED = "\033[91m"
BLUE = "\033[94m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
RESET = "\033[0m"

# Variables
people_count = 0
count = 0
last_detection_time = 0
detection_cooldown = 2
current_minute = datetime.now().minute 
csvfile = "test"

# Write the people count to the CSV file
def write_to_csv(file_path, minute, count):
    filePath = f"{file_path}.csv"
    try:
        with open(filePath, mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([minute, count])
            print("Current working directory:", os.getcwd())
            print(f"Writing to CSV: Minute: {minute}, No_of_People: {count}")
    except Exception as e:
        print(f"An error occurred while writing to the CSV file: {e}")
        
def ultrasound():
        # Set TRIG_PIN high for 10 microseconds to trigger the measurement
    GPIO.output(TRIG_PIN, GPIO.HIGH)
    time.sleep(0.00001)
    GPIO.output(TRIG_PIN, GPIO.LOW)

        # Measure pulse width of the echo
    pulse_start = time.time()
    pulse_end = time.time()

    while GPIO.input(ECHO_PIN) == 0:
        pulse_start = time.time() #capture start of pulse
    while GPIO.input(ECHO_PIN) == 1:
        pulse_end = time.time() #capture end of pulse

    # Calculate the distance
    pulse_duration = pulse_end - pulse_start
    distance = pulse_duration * 17150  # Speed of sound is 34300 cm/s (17150 cm/s round trip)
    return round(distance, 2)


def PeopleCounter():
    global last_detection_time #declare last_detection_time as global
    global detection_cooldown  # 2 seconds cooldown
    global count
    global current_minute
    global people_count
    try:
        while True:
            distance = ultrasound()
            if distance is not None:
                print(f"Distance: {distance} cm")
            time.sleep(1)
            # Check if the distance is within the range of 5cm to 40cm
            if 1 <= distance <= 200:
                current_time = time.time()
                if current_time - last_detection_time > detection_cooldown:
                    count += 1
                    last_detection_time = current_time
                    print(f"Person detected! Total count: {count}")
                        # Check if the hour has changed
                new_minute = datetime.now().minute
                if new_minute != current_minute:
                    people_count = count
                    # Write the count for the past hour to the CSV file
                    write_to_csv(csvfile, current_minute, people_count)
                    # Reset the people count for the new hour
                    people_count = 0
                    count = people_count
                    # Update the current hour
                    current_minute = new_minute

                time.sleep(0.1)  # Wait a bit before the next loop
    except KeyboardInterrupt:
     print("Measurement stopped by user")
     people_count = count
     write_to_csv(csvfile, current_minute, people_count)             
     GPIO.cleanup()

PeopleCounter()
    
