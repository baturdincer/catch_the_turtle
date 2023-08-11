import turtle
import random
click=0
gameOver=False
screen = turtle.Screen()
screen.bgcolor("light blue")
tosba = turtle.Turtle()
tosba.speed("fastest")
tosba.penup()
tosba.shape("turtle")
tosba.fillcolor("green")
tosba.turtlesize(3, 3, 4)
style = ("Courier", 25)
scoretosba = turtle.Turtle()
timetosba = turtle.Turtle()
timetosba.hideturtle()
scoretosba.hideturtle()
scoretosba.penup()
scoretosba.goto(0, 360)
timetosba.penup()
timetosba.goto(0, 320)
scoretosba.write(arg=f"Score: {click}", align="center", font=style)


def clickcounter(x,y):
    scoretosba.clear()
    global click
    global scoretext
    click += 1
    scoretosba.write(arg=f"Score: {click}", align="center", font=style)

def timer(time):
    global gameOver
    timetosba.clear()
    if time>0:
        timetosba.clear()
        timetosba.write(arg=f"Time left: {time}", align="center", font=style)
        screen.ontimer(lambda: timer(time-1),1000)
    else:
        timetosba.write(arg="Game Over!", align="center", font=style)
        gameOver=True
        tosba.hideturtle()



def randompos():
    randx = random.randint(-480, 480)
    randy = random.randint(-380, 380)
    tosba.setposition(randx, randy)

def game():
    global gameOver
    if not gameOver:
        randompos()
        screen.ontimer(game,1000)


tosba.onclick(clickcounter)
timer(3)
game()
screen.mainloop()
