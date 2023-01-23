from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class Car(Turtle):
    def __init__(self):
        super().__init__()
        self.cars = []
        

    def create_car(self, y, speed, direction):
        self.color(random.choice(COLORS))
        self.shape("square")
        self.shapesize(stretch_len=2)
        self.penup()
        self.speed = speed
        self.direction = direction
        self.y = y
        self.goto((300 * direction) * -1, y)
        self.cars.append(self)

    def move(self):
        if self.xcor() > 350 or self.xcor() < -350:
           self.goto((340 * self.direction) * -1, self.y) 
        self.fd(self.speed * self.direction)

    def move_cars(self):
        for car in cars:
            car.move()