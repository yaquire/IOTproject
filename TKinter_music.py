from tkinter import *
import pygame #installation: pip install pygame --user

root=Tk()
root.title('EP0401')
root.geometry('500x400')

pygame.mixer.init()

def play():
    pygame.mixer.music.load('Song1.mp3')
    pygame.mixer.music.play(loops=0)

def stop():
    pygame.mixer.music.stop()


my_button=Button(root,text='Play Song',font=('Helvetica',36),command=play)
my_button.pack(pady=20)

stop_button=Button(root,text='Stop',font=('Helvetica',24),command=stop)
stop_button.pack(pady=20)

root.mainloop()
