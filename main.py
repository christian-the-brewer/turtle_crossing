import time
from turtle import Screen
from player import Player
from score import Score
from car import Car, COLORS

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

game = True

while game:
    time.sleep(0.1)
    screen.update()