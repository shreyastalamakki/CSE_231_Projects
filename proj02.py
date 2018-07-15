########################################################################
# Computer Project #2: Concentric Squares Program
# 1. The User Inputs the number of concentric squares the program draws.
# 2. Using the random function, a color for each square is randomly
#    appointed.
# 3. Loop till it reaches the number the user inputs into the program.
# 4. The turtle graphics shell opens up and the squares are drawn with a
#    random color, each centered around the origin, but length of each 
#    consecutive square 20 less in length than the previous one.
########################################################################

import turtle
import random

def pick_color():
    colors = ["blue","black","brown","red","yellow","green","orange","beige",]
    random.shuffle(colors)
    return colors[0] # The random function selects a color through the
    # available options.

random_color = pick_color()
Square_Length = 400 # The length of the square as per the instructions.
Number_Squares = int(input("Enter the number of squares: ")) # Converts the
# string input into an int shape.

if Number_Squares <= 0: 
    print(" ")
    print("Error. Please enter a positive integer.") # Prints this message if
    # the user enters a negative integer or zero.
else:
    for i in range(Number_Squares): # Ends the loop once the program reaches 
    # the inputed number of squares.
        random_color = pick_color() # picks a random color.
        turtle.color(random_color)
        turtle.up()
        turtle.goto(-Square_Length/2,Square_Length/2) # Halved the dimensions 
        # so that the turtle starts at the bottom left corner and it creates
        # a square around the origin.
        turtle.down()
        turtle.begin_fill() # the random color fills in the square.
        turtle.forward(Square_Length)
        turtle.right(90)
        turtle.forward(Square_Length)
        turtle.right(90)
        turtle.forward(Square_Length)
        turtle.right(90)
        turtle.forward(Square_Length)
        turtle.right(90)
        turtle.end_fill() # Ends the color filling process.
        Square_Length -= 20 # Reduces the next square's length by 20 units.
        
turtle.bye()

# Questions
# Q1: 6
# Q2: 6
# Q3: 6
# Q4: 5

        