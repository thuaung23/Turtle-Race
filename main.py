# This is a simple game called Turtle Race.
# Turtle module and documentation are primarily used.
# Written on, Dec 17, 2020

# Import two classes from Turtle module.
from turtle import Turtle, Screen
import random

# Create a screen object to display an output.
screen = Screen()
# Set the boundaries to make the game easy and simple.
screen.setup(width=500, height=500)

# Get user input to compare with winning turtle.
user_bet = screen.textinput(title="Make you bet.",
                            prompt="Which turtle will win the race? Enter a color:"
                                   "\nRed\nOrange\nBlack\nGreen\nBlue\nPurple").lower()
color = ["red", "orange", "black", "green", "blue", "purple"]
y_position = [120, 80, 40, 0, -40, -80]
turtle_list = []

# Create 6 turtles with different colors.
for turtle in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(color[turtle])
    # To avoid drawing lines.
    new_turtle.penup()
    # Get turtles in positions.
    new_turtle.goto(x=-240, y=y_position[turtle])
    # Add created turtles to a list.
    turtle_list.append(new_turtle)

game_on = False

# Check if user places any inputs.
if user_bet:
    game_on = True

while game_on:
    for turtle in turtle_list:
        # For every turtles in list, whoever reaches right boundary first wins.
        if turtle.xcor() > 230:
            game_on = False
            # Get color of winning turtle to compare with user's input.
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"The winner is {winning_color} turtle.\nCongratulations. You win.")

            else:
                print(f"The winner is {winning_color} turtle.\nSorry. You lose.")

        # Move turtles at random paces.
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)

# The screen will stay on unless it was clicked.
screen.exitonclick()
