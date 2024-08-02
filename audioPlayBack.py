import RPi.GPIO as GPIO  # import RPi.GPIO module
from time import sleep  # used to create delays

GPIO.setmode(GPIO.BCM)  # choose BCM mode
GPIO.setwarnings(False)
GPIO.setup(18, GPIO.OUT)  # set GPIO 18 as output
PWM = GPIO.PWM(18, 100)  # initialize PWM on pin 18 with a frequency (we'll change it later)

# Define the notes and their frequencies
# Frequencies in Hertz for notes (A4 = 440 Hz)

C4 = 261
D4 = 294
E4 = 329
F4 = 349
G4 = 392
Ab4 = 415
A4 = 440
Bb4 = 466
B4 = 493
C5 = 523
D5 = 587
E5 = 659
F5 = 698
G5 = 784
A5 = 880

# Define the Super Mario Bros. theme melody and duration for each note
mario_melody = [
    E5, E5, 0, E5, 0, C5, E5, 0,
    G5, 0, 0, 0, G4, 0, 0, 0,
    C5, 0, 0, G4, 0, 0, E4, 0,
    0, A4, 0, B4, 0, A4, A4, 0,
    G4, E5, 0, G5, A5, 0, F5, G5,
    0, E5, 0, C5, D5, B4, 0, 0,
    C5, 0, 0, G4, 0, 0, E4, 0,
    0, A4, 0, B4, 0, A4, A4, 0,
    G4, E5, 0, G5, A5, 0, F5, G5,
    0, E5, 0, C5, D5, B4, 0, 0
]

mario_tempo = [
    0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15,
    0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15,
    0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15,
    0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15,
    0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15,
    0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15,
    0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15,
    0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15,
    0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15,
    0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15
]

# Define the Sad Trombone melody and duration for each note
sad_trombone_melody = [B4, Bb4, A4, Ab4, G4]
sad_trombone_tempo = [0.5, 0.5, 0.5, 0.5, 1.0]  # durations in seconds

def ChangeFrequency(frequency):
    PWM = GPIO.PWM(18, frequency)  # initialize PWM on pin 18 with a frequency (we'll change it later)

def play_melody(melody, tempo):
    for note, duration in zip(melody, tempo):
        if note == 0:  # Rest
            sleep(duration)
        else:
            PWM.ChangeFrequency(note)
            PWM.start(50)  # 50% duty cycle
            sleep(duration)
            PWM.stop()
try:
    choice = input("Enter 'mario' to play the Super Mario theme or 'trombone' to play the Sad Trombone sound: ").strip().lower()
    
    if choice == 'mario':
        while True:
            play_melody(mario_melody, mario_tempo)
            sleep(2)  # Delay before repeating the sound effect
    elif choice == 'trombone':
        while True:
            play_melody(sad_trombone_melody, sad_trombone_tempo)
            sleep(2)  # Delay before repeating the sound effect
    else:
        print("Invalid choice. Please restart the program and enter a valid option.")
finally:
    PWM.stop()
    GPIO.cleanup()