import random
from turtle import Turtle, Screen, colormode

colormode(255)

race_active = False

screen = Screen()
screen.setup(width=500, height=400)
screen.title("Turtle Race")
screen.bgcolor(235, 240, 245)

user_choice = screen.textinput(
    title="Place Your Bet", prompt="Which turtle will win the race? Enter a color:"
)
if user_choice:
    user_choice = user_choice.lower()

turtle_colors = [
    "red",
    "orange",
    "yellow",
    "green",
    "blue",
    "purple"
]


start_y = 166.7
racers = []

for index in range(6):
    racer = Turtle("turtle")
    racer.color(turtle_colors[index])
    racer.penup()
    racer.goto(x=-235, y=start_y)
    racers.append(racer)
    start_y -= 66.7

if user_choice:
    race_active = True

while race_active:
    for racer in racers:
        if racer.xcor() > 230:
            race_active = False
            winner = racer.pencolor()
            if winner == user_choice:
                print(f"You've won! The {winner} turtle is the winner!")
            else:
                print(f"You've lost! The {winner} turtle is the winner!")
        step = random.randint(0, 10)
        racer.forward(step)

screen.exitonclick()
