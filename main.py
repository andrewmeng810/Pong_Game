"""
1. Create the screen
2. Create and move the paddle
3. Create another paddle
4. Create the ball and make it move
5. Detect collision with wall and bounce
6. Detect collision with paddle
7. Detect when paddle mises
8. Keep score
"""

import turtle as t
import paddle as p
import ball as b
import time
import scoreboard as s

screen = t.Screen()
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title('Pong Game')
screen.tracer(0)

# Create left paddle
l_paddle = p.Paddle((-350, 0))
# Create right paddle
r_paddle = p.Paddle((350, 0))

# able to move the paddle
screen.listen()
screen.onkey(r_paddle.go_up, 'Up')
screen.onkey(r_paddle.go_down, 'Down')

screen.onkey(l_paddle.go_up, 'w')
screen.onkey(l_paddle.go_down, 's')

# Create the ball
ball = b.Ball()

# Create the scoreboard
scoreboard = s.Scoreboard()


is_game_on = True
while is_game_on:
    screen.update()  # show the final position after each segment's movement
    ball.move()
    time.sleep(ball.ball_speed)

    # Detect if the ball hit the wall (top and bottom)
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.y_bounce()

    # Detect if ball hit the left or right paddle
    if (ball.xcor() > 320 and ball.distance(r_paddle) < 50) or (
            ball.xcor() < -320 and ball.distance(l_paddle) < 50):
        ball.x_bounce()

    # Detect if R paddle miss
    if ball.xcor() > 350:
        ball.reset_position()
        scoreboard.increase_l_score()

    # Detect if L paddle miss
    if ball.xcor() < -350:
        ball.reset_position()
        scoreboard.increase_r_score()


screen.exitonclick()
