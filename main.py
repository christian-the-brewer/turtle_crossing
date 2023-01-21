import time
from turtle import Screen
from player import Player
from score import Score
from car import Car, COLORS

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.tracer(0)

player = Player()

#screen listeners
screen.listen()
screen.onkey(player.move_up, "Up")
screen.onkey(player.move_left, "Left")
screen.onkey(player.move_right, "Right")

game = True

while game:
    time.sleep(0.1)
    screen.update()

screen.exitonclick()