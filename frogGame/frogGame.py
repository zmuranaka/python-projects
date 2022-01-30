# File: frogGame.py
# Zachary Muranaka
# Allows the user to play a simple game of a frog catching flies
# This website was helpful in the creation of this game https://pygame-zero.readthedocs.io/en/stable/

import pgzrun
from random import randint

# Dimensions of screen
WIDTH = 600
HEIGHT = 600

score = 0

# Create the frog actor and set its initial position
frog = Actor("frogright")
frog.pos = 100, 100

# Create the fly actor and set its initial position
fly = Actor("fly")
fly.pos = 300, 300

gameIsOver = False

# Draws the initial setup of the game or the ending screen if the game is over
def draw():
    screen.fill("lightblue")
    frog.draw()
    fly.draw()
    screen.draw.text("Score: " + str(score), color="black", topleft=(10, 10))

    if gameIsOver:
        screen.fill("blue")
        screen.draw.text("Final Score: " + str(score), topleft=(10, 10), fontsize=60)

# Places a new fly on the screen
def newFly():
    fly.x = noCollision(frog.x)
    fly.y = noCollision(frog.y)

# Returns a random position that will not collide with where the frog already is
def noCollision(frogPosition):
    potentialPosition = randint(64, 536)
    if potentialPosition > frogPosition + 128 or potentialPosition < frogPosition - 128:
        return potentialPosition
    else:
        return noCollision(frogPosition)

# The game ends when the time is up
def timeIsUp():
    global gameIsOver
    gameIsOver = True

def update():
    global score

    if not gameIsOver:
        if keyboard.left:
            frog.image = "frogleft"
            if frog.x < 64: # Make sure the frog doesn't leave the screen
                frog.x+=20
            else:
                frog.x-=6
        if keyboard.right:
            frog.image = "frogright"
            if frog.x > 536: # Make sure the frog doesn't leave the screen
                frog.x-=20
            else:
                frog.x+=6
        if keyboard.up:
            if frog.y < 64: # Make sure the frog doesn't leave the screen
                frog.y+=20
            else:
                frog.y-=6
        if keyboard.down:
            if frog.y > 536: # Make sure the frog doesn't leave the screen
                frog.y-=20
            else:
                frog.y+=6

    if frog.colliderect(fly):
        score+=1
        newFly()

clock.schedule(timeIsUp, 10) # The game lasts 10 seconds

pgzrun.go()
