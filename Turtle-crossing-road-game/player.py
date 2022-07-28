from turtle import Turtle


STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 100
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("black")
        self.penup()
        self.go_to_start()
        self.setheading(90)


    def move_forward(self):
        self.forward(MOVE_DISTANCE)

    def move_left(self):
        self.goto(self.xcor() - MOVE_DISTANCE, self.ycor())

    def move_right(self):
        self.goto(self.xcor() + MOVE_DISTANCE, self.ycor())

    def move_backward(self):
        self.backward(MOVE_DISTANCE)

    def go_to_start(self):
        self.goto(STARTING_POSITION)

    def is_reach_finish_line(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False