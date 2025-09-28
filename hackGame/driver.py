# File: driver.py
# Zachary Muranaka
# Displays a menu that allows the user to choose the dimensions of the game

import pgzrun
import subprocess

# Coordinates of the boxes
promptBox = Rect(150, 50, 500, 100)
resBoxes = [ Rect(150, 225, 500, 50), Rect(150, 325, 500, 50), Rect(150, 425, 500, 50) ]

def draw():
    screen.draw.textbox("Choose the dimensions of the game", promptBox, fontname="consolas", color="green")
    screen.draw.textbox("1024 x 768", resBoxes[0], fontname="consolas", color="green")
    screen.draw.textbox("1280 x 800", resBoxes[1], fontname="consolas", color="green")
    screen.draw.textbox("1536 x 864", resBoxes[2], fontname="consolas", color="green")

def on_mouse_down(pos):
    # Call hackGame.py when one of the boxes is clicked, passing the respective dimensions as command-line arguments
    if(resBoxes[0].collidepoint(pos)):
        subprocess.call(["python.exe", "hackGame.py", "1024", "768"]) # 4/3 aspect ratio
    elif(resBoxes[1].collidepoint(pos)):
        subprocess.call(["python.exe", "hackGame.py", "1280", "800"]) # 16/10 aspect ratio
    elif(resBoxes[2].collidepoint(pos)):
        subprocess.call(["python.exe", "hackGame.py", "1536", "864"]) # 16/9 aspect ratio

pgzrun.go()
