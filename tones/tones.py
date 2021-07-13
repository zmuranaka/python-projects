# File: tones.py
# Zachary Muranaka
# Plays tones whenever any key is pressed
# This website was helpful in the creation of this game https://pygame-zero.readthedocs.io/en/stable/

import pgzrun
from random import randint

octave = '4' # The default octave is 4

def beat():
    randomC = 'C' + str(randint(1, 6))
    tone.create(randomC, 0.2).play()
    print(randomC)
    randomE = 'E' + str(randint(1, 5))
    tone.create(randomE, 0.2).play()
    print(randomE)
    randomG = 'G' + str(randint(1, 5))
    tone.create(randomG, 0.2).play()
    print(randomG)
    print()
    clock.schedule_unique(beat, 0.3)
        
def on_key_down():
    global octave

    # Change the octave
    if keyboard.K_0 or keyboard.KP0:
        octave = '0'
    if keyboard.K_1 or keyboard.KP1:
        octave = '1'
    if keyboard.K_2 or keyboard.KP2:
        octave = '2'
    if keyboard.K_3 or keyboard.KP3:
        octave = '3'
    if keyboard.K_4 or keyboard.KP4:
        octave = '4'
    if keyboard.K_5 or keyboard.KP5:
        octave = '5'
    if keyboard.K_6 or keyboard.KP6:
        octave = '6'
    if keyboard.K_7 or keyboard.KP7:
        octave = '7'
    if keyboard.K_8 or keyboard.KP8:
        octave = '8'

    # Play a note
    if keyboard.A:
        tone.create('A' + octave, 0.5).play()
    if keyboard.B:
        tone.create('B' + octave, 0.5).play()
    if keyboard.C:
        tone.create('C' + octave, 0.5).play()
    if keyboard.D:
        tone.create('D' + octave, 0.5).play()
    if keyboard.E:
        tone.create('E' + octave, 0.5).play()
    if keyboard.F:
        tone.create('F' + octave, 0.5).play()
    if keyboard.G:
        tone.create('G' + octave, 0.5).play()
    
    # Starts the beat
    if keyboard.S:
        beat()      
        
pgzrun.go()
