#WHOOPEE CUSHION
#import all necessary libraries
import os
import random
from time import sleep
from gpiozero import Button

#define button to pin
button = Button (2)

#list of all sound effects
trumps = ['burp.wav', 'ben-fart.wav', 'marc-fart.wav', 'ca-fart.wav']

#'Action-Coding'
while True:
    button.wait_for_press()
    parp = random.choice(trumps)
    os.system("aplay {0}".format(parp))
    sleep(2)