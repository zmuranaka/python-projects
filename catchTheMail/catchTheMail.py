# File: catchTheMail.py
# Zachary Muranaka
# Allows the user to play a simple point-and-click game of catching a mail image
# This website was helpful in the creation of this game https://pygame-zero.readthedocs.io/en/stable/

import pgzrun
from random import randint

score = 0
mail = Actor("mail")

def draw():
    screen.clear()
    mail.draw()

# Places the mail in a new position and recalls this function in 1 second
def placeMail():
    mail.x = randint(10, 800)
    mail.y = randint(10, 600)
    clock.schedule_unique(placeMail, 1)

# Runs any time the player clicks their mouse
def on_mouse_down(pos):
    global score
    
    # The player clicked the mail
    if mail.collidepoint(pos):
        score += 1
        placeMail()
    
    # The player clicked somewhere other than the mail
    else:
        if score < 5:
            print("Tough luck! Your final score was", score)
        else:
            print("Nice job! Your final score was", score)
        quit()

pgzrun.go()
