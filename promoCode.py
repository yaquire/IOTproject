from os import name
import sys
import RPi.GPIO as GPIO
from time import sleep

from requests.models import auth
from mfrc522 import SimpleMFRC522

RED = "\033[91m"
BLUE = "\033[94m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
RESET = "\033[0m"

# Reads from the RFID
GPIO.setwarnings(False)
reader = SimpleMFRC522()


def clearingDatabase():
    return print(RED + "Data Base has been cleared" + RESET)


def registeringCards():
    while True:
        print("Hold the card near the reader")
        # this part is from the USER_GUIDE, I need to test to understand the code better
        id = reader.read_id()
        id = str(id)
        f = open("authlist.txt", "a+")
        f = open("authlist.txt", "r+")
        # if f.mode == "r+":
        auth = f.read()
        if id not in auth:
            f.write(id)
            f.write("\n")
            f.close()
            pos = auth.count("\n")
            print("New card with UID", id, "detected; registered as entry #", pos)
        else:
            number = auth.split("\n")
            pos = number.index(id)
            print("Card with UID", id, "already registered as entry #", pos)
        sleep(2)

    return print(GREEN + "The user has been registered" + RESET)


def identifyingCards():
    ID = "q"
    name = ID
    return print(BLUE + f"{name} has been identified" + RESET)


# this will likely use the LCD for USER imput


def main():
    test_for_registering = registeringCards()


main()
