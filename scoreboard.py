from turtle import Turtle, window_height

ALIGNMENT = "center"
FONT = ("Arial", 13, "normal")
class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color('white')
        self.hideturtle()
        self.penup()
        self.goto(0, window_height()/2-20)
        self.update()

    def update(self):
        self.write(f"score: {self.score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.write(f"score: {self.score}", align=ALIGNMENT, font=FONT)
    
    def GameOver(self):
        self.goto(0,0)
        self.write("Game Over!!", align=ALIGNMENT, font=("Arial", 25, "normal"))
