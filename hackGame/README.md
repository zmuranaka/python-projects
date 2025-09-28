# Hack Game with Pygame Zero

## What is this Project?

If you've ever seen a movie or TV show that portrays a "hacker", they were probably furiously typing cryptic green text into a black terminal. This project is a simple game I made with [Pygame Zero](https://pygame-zero.readthedocs.io/en/stable/) to simulate this experience. The inspiration of the project came from the website [Hacker Typer](https://hackertyper.net/).

## How do I Start the Game?

First of all, you need Python3 and Pygame Zero installed to run the game. You can find instructions on how to install Pygame Zero [here](https://pygame-zero.readthedocs.io/en/stable/installation.html). After that, all you need to do to run the game is double click the driver.py file, which will launch a GUI menu that allows you to choose the dimensions of the game. Another way to start the game is by double clicking the hackGame.py file, which sets the dimensions to the default of 800 x 600. Another way to run the game is by launching a command prompt from the folder where the files are located and typing either ```driver.py```, which will launch the GUI menu, or ```hackGame.py``` followed by the dimensions you want (width x height). For example, to launch the game with a width of 1000 and a height of 600, you would type ```hackGame.py 1000 600``` into the command prompt and press enter.

## How do I Play the Game?

This game is not a game in the sense that it is one you can win - it's a game in the sense that you can fool people you know into thinking you are an elite hacker. The game is very simple in that typing almost anything on your keyboard generates a line of "hacker code" on the screen. The only keys that do not do this are escape and end, which close the window, backspace and delete, which delete the last line, and enter, which skips the next line.

## What is the Code Displayed in the Game?

The code displayed in the game is just a random mix of programming languages and is not supposed to do anything but look impressive to the average person.

## Files:

driver.py

&nbsp;&nbsp;&nbsp;&nbsp;This file contains the GUI menu that allows you to choose the dimensions of the game. The three options are 1024 x 768 (4/3 aspect ratio), 1280 x 800 (16/10 aspect ratio), and 1536 x 864 (16/9 aspect ratio). When one of the dimension boxes is clicked, hackGame.py is called from the command prompt using the dimensions as arguments.

hackGame.py

&nbsp;&nbsp;&nbsp;&nbsp;This file is the actual game. It draws the window depending on the given command-line argument dimensions (or 800 x 600 if no dimensions were given) and handles all of the keypresses during the game, most of which generate a random line of "hacker code".

## Sources:

Sources that helped me create the project:

https://www.dk.com/us/book/9781465473615-coding-games-in-python/

Coding Games in Python, published by DK, was a helpful starting point to learning Pygame Zero.

https://pygame-zero.readthedocs.io/en/stable/

&nbsp;&nbsp;&nbsp;&nbsp;The Pygame Zero documentation was very helpful during the creation of this game.

https://stackoverflow.com/questions/25651990/oserror-winerror-193-1-is-not-a-valid-win32-application

&nbsp;&nbsp;&nbsp;&nbsp;This webpage was helpful when I was creating driver.py.

https://hackertyper.net/

&nbsp;&nbsp;&nbsp;&nbsp;This website was the main inspiration of the project.

## Author:

Zachary Muranaka
&nbsp;&nbsp;&nbsp;&nbsp;zmuranaka@gmail.com
&nbsp;&nbsp;&nbsp;&nbsp;https://zmuranaka.dev
