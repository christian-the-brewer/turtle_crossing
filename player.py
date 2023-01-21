from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE = 280

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("green")
        self.seth(90)
        self.penup()
        self.goto(STARTING_POSITION)

    def move_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def move_left(self):
        if self.xcor() > -280:
            new_x = self.xcor() - 20
            self.goto(new_x, self.ycor())

    def move_right(self):
        if self.xcor() < 280:
            new_x = self.xcor() + 20
            self.goto(new_x, self.ycor())