import time
from turtle import Screen
from player import Player
from score import Score
from car import Car, COLORS, cars

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.tracer(0)

player = Player()
car1_1 = Car(-100, 5, 1)

#screen listeners
screen.listen()
screen.onkey(player.move_up, "Up")
screen.onkey(player.move_left, "Left")
screen.onkey(player.move_right, "Right")


def move():
    for car in cars:
        car.move()

game = True

while game:
    time.sleep(0.01)
    screen.update()
    move()

screen.exitonclick()