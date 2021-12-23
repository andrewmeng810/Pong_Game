import turtle as t


class Ball(t.Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('white')
        self.shapesize(stretch_wid=1, stretch_len=1)
        self.penup()
        self.goto(0, 0)
        self.x_move = 10
        self.y_move = 10
        self.ball_speed = 0.1

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def y_bounce(self):
        # x coordinate stays the same, y coordinate decreases
        self.y_move *= -1

    def x_bounce(self):
        # x coordinate stays the same, y coordinate decreases
        self.x_move *= -1
        # every time when the play hit the ball, the ball goes faster
        self.ball_speed *= 0.85

    def reset_position(self):
        self.goto(0, 0)
        # reset the ball speed once player missed the ball
        self.ball_speed = 0.1
        self.x_bounce()



