from turtle import Turtle
ALIGNMENT = "center"


class Score(Turtle):

    def __int__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.updated_score()

    def updated_score(self):
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=("Arial", 24, "normal"))

    def increase_score(self):
        self.score += 1
        self.clear()
        self.updated_score()
