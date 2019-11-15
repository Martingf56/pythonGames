#! /usr/bin/env python
#Juego de Pong hecho siguiendo el curso de freeCodeCamp

import turtle
import os
import time

#Crea la ventana
wn = turtle.Screen()
wn.title("Pong")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

#Score
scoreA = 0
scoreB = 0

# Paddle A
paddleA = turtle.Turtle()
paddleA.speed(0)#The speed of animation
paddleA.shape("square")
paddleA.color("white")
paddleA.shapesize(stretch_wid=5, stretch_len=1)
paddleA.penup()
paddleA.goto(-350,0)


# Paddle B
paddleB = turtle.Turtle()
paddleB.speed(0)#The speed of animation
paddleB.shape("square")
paddleB.color("white")
paddleB.shapesize(stretch_wid=5, stretch_len=1)
paddleB.penup()
paddleB.goto(350,0)

#Ball
ball = turtle.Turtle()
paddleA.speed(0)#The speed of animation
ball.shape("square")
ball.color("white")
ball.penup()
ball.dx = 0.5
ball.dy = 0.5

#Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Player A: 0 Player B: 0",align="center",font=("Courier",16, "normal"))

#Goal
goal = turtle.Turtle()
goal.speed()
goal.color("white")
goal.penup()
goal.hideturtle()
goal.goto(0, 150)

#Win 
win = turtle.Turtle()
win.speed(0)
win.color("white")
win.penup()
win.hideturtle()
win.goto(0, 120)

#Function
def paddleA_up():
    y = paddleA.ycor()
    if (y + 20 ) <= 240:
        y += 20
    paddleA.sety(y)

def paddleA_down():
    y = paddleA.ycor()
    if (y - 20 ) >= -240:
        y -= 20
    paddleA.sety(y)

def paddleB_up():
    y = paddleB.ycor()
    if (y + 20 ) <= 240:
        y += 20
    paddleB.sety(y)

def paddleB_down():
    y = paddleB.ycor()
    if (y - 20 ) >= -240:
        y -= 20
    paddleB.sety(y)

def goal_view():
    goal.write("Point!!",align="center",font=("Courier",18, "normal"))
    time.sleep(0.5)   
    goal.clear()

def win_view(winner):
    if winner == 'A':
        w ='B'
    else:
        w = 'A'
    win.write("The Winner is Player "+winner+" ,The Player "+ w + " is a LOOSER",align="center", font=("Courier",20, "normal"))


#Keyboard binding
wn.listen()
wn.onkey(paddleA_up,"w")
wn.onkey(paddleA_down,"s")
wn.onkey(paddleB_up,"Up")
wn.onkey(paddleB_down,"Down")


#Main game loop
while True:
    wn.update()

    #Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    #Border checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        os.system("aplay bounce.wav&")

    if ball.ycor() < -290 :
        ball.sety(-290)
        ball.dy *= -1
        os.system("aplay bounce.wav&")

    if ball.xcor() > 390 :#Goal
        scoreA += 1
        ball.goto(0,0)
        ball.dx *= -1
        goal_view()
        paddleB.goto(350,0)
        paddleA.goto(-350,0)

    if ball.xcor() < -390 :#Goal
        scoreB += 1
        ball.goto(0,0)
        ball.dx *= -1
        goal_view()
        paddleB.goto(350,0)
        paddleA.goto(-350,0)

    pen.clear()
    pen.write("Player A: {} Player B: {}".format(scoreA,scoreB),align="center",font=("Courier",16, "normal"))
    
    # Paddle and ball colisions
    if (ball.xcor() > 340 and ball.xcor() < 350 )and (ball.ycor() < paddleB.ycor() + 40 and ball.ycor() > paddleB.ycor() - 40):
        ball.setx(340)
        ball.dx *= -1
        os.system("aplay bounce.wav&")
    if (ball.xcor() < -340 and ball.xcor() > -350 )and (ball.ycor() < paddleA.ycor() + 40 and ball.ycor() > paddleA.ycor() - 40):
        ball.setx(-340)
        ball.dx *= -1
        os.system("aplay bounce.wav&")

    if scoreA == 5:
        win_view('A')
    elif scoreB == 5: 
        win_view('B')
    if scoreA == 5 or scoreB == 5:
        time.sleep(2)
        win.clear()
        scoreA = 0;scoreB = 0
    
    
