from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class Car(Turtle):
    def __init__(self, y, speed, direction):
        super().__init__()
        self.color(random.choice(COLORS))
        self.shape("square")
        self.shapesize(stretch_len=40)
        self.penup()
        self.speed = speed
        self.direction = direction
        self.y = y
        self.goto((300 * direction) * -1, position)


    def move(self):
        if self.xcor() > 350 or self.xcor() < -350:
           self.goto((300 * self.direction) * -1, self.y) 
        self.fd(self.speed * self.direction)