# File: hackGame.py
# Zachary Muranaka
# Simple game that allows the user to look like a hacker

import pgzrun
import sys
from random import randint

# Check if a width and height were supplied as command-line arguments
if len(sys.argv) == 3:
    WIDTH = int(sys.argv[1]) # Get the width from the command-line arguments
    HEIGHT = int(sys.argv[2]) # Get the height from the command-line arguments
# Otherwise set a default width and height
else:
    WIDTH = 800
    HEIGHT = 600

# Global variables
verticalPosition = 25
drawFirstLine = True
drawNewLine = False
drawEmptyLine = False
previousLine = ""

def draw():
    global verticalPosition
    global drawFirstLine
    global drawNewLine
    global drawEmptyLine
    global previousLine

    # The first line always displays /* Initialize hack */
    if drawFirstLine:
        screen.draw.text("/* Initialize hack */", (5, 5), fontname="consolas", color="green", fontsize=15)
        drawFirstLine = False
    # Make sure the text does not go off of the screen
    elif drawNewLine:
        if verticalPosition > HEIGHT - 20:
            verticalPosition = 5
            screen.clear()

        if drawEmptyLine: # Check if we are going to draw an empty line
            newLine = ""
        else: # Get a new line to draw
            newLine = getNewLine()

        screen.draw.text(newLine, (5, verticalPosition), fontname="consolas", color="green", fontsize=15)
        previousLine = newLine
        verticalPosition+=20

        # Reset the variables
        drawNewLine = False
        if drawEmptyLine:
            drawEmptyLine = False
    else:
        # Make sure we never erase off of the screen
        if verticalPosition >= 20:
            verticalPosition-=20
            eraser = Rect(5, verticalPosition, WIDTH, 20)
            screen.draw.filled_rect(eraser, "black")

# Runs whenever any key is pressed
def on_key_down():
    global drawNewLine
    global drawEmptyLine

    if keyboard.ESCAPE or keyboard.END: # Shortcuts to end the game
        exit()
    elif keyboard.BACKSPACE or keyboard.DELETE: # Backspace and delete "erase" the previous line
        drawNewLine = False
    elif keyboard.RETURN or keyboard.KP_ENTER: # The enter keys draw an empty line
        drawNewLine = True
        drawEmptyLine = True
    else:
        drawNewLine = True

# Returns a line that is different than the previous line
def getNewLine():
    global previousLine
    
    possibleLine = fakeCode[randint(0, len(fakeCode)-1)]
    if possibleLine == previousLine:
        return getNewLine()
    else:
        return possibleLine 

# Array of strings that look like hacking code
# These strings will be drawn on the screen to make the user look like a hacker
# The code strings are a mix of several programming languages
# They are basically complete nonsense - however, they only have to look like real code
fakeCode = [
    # Non-indented code
    "for((i=0; i<resource_handler; i++))",
    "do",
    "done",
    "if((resource_handler > 0))",
    "arg=$1",
    "argVar=$((arg+1))",
    "powerVar=$((2**arg))",
    "then",
    "$resource_handler = 1010101101010;",
    "if($_FILES) encrypt(array_filter($_FILES));",
    "extract($_GET, EXTR_PREFIX_ALL, 'content_');",
    "<script>",
    "</script>",
    "public static void main(String[] args) {",
    "public class Handler {",
    "Scanner input = new Scanner(System.in);",
    "include <iostream>",
    "using namespace std;",
    "using namespace my_namespace;",
    "using static System.Math;",

    # Indented code
    "    breakThrough = resources[i]? resources[i] : 0;",
    "    } else if(this.console.resources_are_allocated())",
    "    } catch(const std::exception& thisException) {",
    "    struct resource_handler {",
    "    for i in range(1, 100) { ",
    "    int test = input.nextInt();",
    "    double test = input.nextDouble();",
    "        } throw std::runtime_error('Index value out of bounds');",
    "        stdBuffer = (node*) malloc (i++);",
    "        nonThrowable = new(nothrow) int[i];",
    "        if uptime > 1000:",
    "        else:",
    "            } this->retry();",
    "            i++;",
    "            var hash = document.getElementById('hashFunc')",
    "            return this.driver();",
    "            return i;",

    # Inline-commented code
    "console.log(this); // Debug",
    "class myTempClass { // Start class",
    "node* myNode = new node(); /* Create a new node */",
    "System.deny_resources(); /* Attempt to create a memory leak */",
    "for(let i = 0; i < 10; i++) { # Repeat the following 10 times",
    "foreach($vector as $key1 => $value1) { # Loop through each key in the vector",
    "delete[] nodes; // Avoid a memory leak",
    "} // End Class",

    # Comments
    "/* Initialize recursive algorithm */",
    "/* The following algorithm runs in O(log(n)) time */",
    "/* The following is a mid-square hash function */",
    "// Make sure to avoid a memory leak",
    "// Make sure to allocate enough resources for the dynamic pointers",
    "// Passes all test cases",
    "# Push the node onto the stack",
    "# Pop the node off of the stack",
    "# The following process runs as a command-line script",

    # Brackets
    "{",
    "}"
]

pgzrun.go()
