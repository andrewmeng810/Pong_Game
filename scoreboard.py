import turtle as t

ALIGNMENT = 'center'
FONT = ('Courier', 60, 'bold')


class Scoreboard(t.Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color('white')
        self.l_score = 0
        self.r_score = 0
        self.update_scoreboard()
        self.hideturtle()

    def update_scoreboard(self):
        self.clear()
        self.goto(-100, 200)
        self.write('{}'.format(self.l_score), move=False,
                   align=ALIGNMENT, font=FONT)
        self.goto(100, 200)
        self.write('{}'.format(self.r_score), move=False,
                   align=ALIGNMENT, font=FONT)

    def increase_l_score(self):
        self.l_score += 1
        self.clear()  # to clear the previous score and write the new score
        self.update_scoreboard()

    def increase_r_score(self):
        self.r_score += 1
        self.clear()  # to clear the previous score and write the new score
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write('GAME OVER', align=ALIGNMENT, font=('Courier', 40, 'bold'))
