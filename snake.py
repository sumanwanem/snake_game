from turtle import Turtle, Screen
STARTING_POSITIONS = [(0,0), (-20,0), (-40,0)]
UP = 90
RIGHT = 0
DOWN = 270
LEFT = 180

class Snake:
    def __init__(self) -> None:
        #self.screen = Screen()
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)
            
    def add_segment(self, position):
        segment = Turtle("square")
        segment.color("white")
        segment.penup()
        segment.goto(position)
        self.segments.append(segment)
    
    def extend(self):
        self.add_segment(self.segments[-1].position())
    def move(self):
        for seg_num in range(len(self.segments)-1, 0, -1):
            x = self.segments[seg_num-1].xcor()
            y = self.segments[seg_num-1].ycor()
            self.segments[seg_num].goto(x,y)
        self.head.forward(20)

    def extand(self):
        segment = Turtle("square")
        segment.color("white")
        segment.penup()
        #Position new segment at the end of the snake
        segment.goto(self.segments[-1].position())
        self.segments.append(segment)


    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
        
        self.segments[0].forward(20)



