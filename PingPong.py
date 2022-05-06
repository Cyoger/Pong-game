import turtle
import os
import winsound



win = turtle.Screen()
win.title("Pong by Cyoger")
win.bgcolor("#856ff8")
win.setup(width=800, height=600)
win.tracer(0)

#score
score_a = 0
score_b = 0

# Paddle 1
paddle_1 = turtle.Turtle()
paddle_1.speed(0)
paddle_1.shape("square")
paddle_1.shapesize(stretch_wid=5, stretch_len=1)
paddle_1.color("red")
paddle_1.penup()
paddle_1.goto(-350, 0)


# Paddle 2
paddle_2 = turtle.Turtle()
paddle_2.speed(0)
paddle_2.shape("square")
paddle_2.shapesize(stretch_wid=5, stretch_len=1)
paddle_2.color("blue")
paddle_2.penup()
paddle_2.goto(350, 0)


# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.10
ball.dy = -0.10

#pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0  Player B: 0", align="center", font=("Courier", 15, "normal"))

# helper functions
def paddle_1_up():
    y = paddle_1.ycor()
    y += 20
    paddle_1.sety(y)


def paddle_1_down():
    y = paddle_1.ycor()
    y -= 20
    paddle_1.sety(y)


def paddle_2_up():
    y = paddle_2.ycor()
    y += 20
    paddle_2.sety(y)


def paddle_2_down():
    y = paddle_2.ycor()
    y -= 20
    paddle_2.sety(y)


# keyboard controls
win.listen()
win.onkeypress(paddle_1_up, "w")
win.onkeypress(paddle_1_down, "s")
win.onkeypress(paddle_2_up, "Up")
win.onkeypress(paddle_2_down, "Down")

# game loop
while True:
    win.update()

    # move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # border checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        #os.system("aplay bounce.wav&")   #Linux
        #os.system("afplay bounce.wav&")  #Mac
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1	
        #os.system("aplay bounce.wav&")  #Linux
        #os.system("afplay bounce.wav&") #Mac
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
        
    if ball.xcor() > 390:
        ball.goto(0 , 0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 15, "normal"))
    
    if ball.xcor() < -390:
        ball.goto(0 , 0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 15, "normal"))
    
    #paddle and ball interactions
    if ball.xcor() < -340 and ball.ycor() < paddle_1.ycor() + 50 and ball.ycor() > paddle_1.ycor() - 50:
        #ball.setx(340)
        ball.dx *= -1
        #os.system("aplay bounce.wav&")   #Linux
        #os.system("afplay bounce.wav&")  #Mac
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
    
    if ball.xcor() > 340 and ball.ycor() < paddle_2.ycor() + 50 and ball.ycor() > paddle_2.ycor() - 50:
        #ball.setx(340)
        ball.dx *= -1
        #os.system("aplay bounce.wav&")   #Linux
        #os.system("afplay bounce.wav&")  #Mac
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)