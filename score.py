from turtle import Turtle
FONT = FONT = ("Arias", 14, "bold")
STARTING_LIVES = 3

class Score(Turtle):
    def __init__(self, type) -> None:
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("white")
        if type == "score":
            self.points = 0
            self.goto(0, 275)
            self.write(f"Score: {self.points}", align="center", font=FONT)
        elif type == "lives":
            self.lives = STARTING_LIVES
            self.goto(-200, 275)
            self.write(f"Lives: {self.lives}", align="center", font=FONT)
            
        def increase_score(self):
            self.points += 1
            self.clear()
            self.write(f"Score: {self.score}", align="center", font=FONT)

        def decrease_lives(self):
            self.lives -= 1
            self.clear()
            self.write(f"Lives: {self.lives}", align="center", font=FONT)
            
        def game_over(self):
            self.goto(0, 0)
            self.write("GAME OVER", align="center", font=("Arias", 20, "bold"))