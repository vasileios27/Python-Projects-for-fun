#!/usr/bin/env python
# coding: utf-8

# In[1]:


import turtle
import os


wn = turtle.Screen() # creates a windo
wn.title("Pong") # gives a titile to the windo
wn.bgcolor("black") # set the color of the windo
wn.setup(width=800, height=600) # sets the dimentions of the windo
wn.tracer(0) # stops the windo to update

# Score
score_a = 0
score_b = 0

# Paddle A
paddle_a = turtle.Turtle() # turtle object that defines the paddle
paddle_a.speed(0) # the speed of annimation, not the speed of movement
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1) # stretches the dimentios of the paddle
paddle_a.penup()
paddle_a.goto(-350,0) #starting point of paddle


# Paddle B
paddle_b = turtle.Turtle() # turtle object that defines the paddle
paddle_b.speed(0) # the speed of annimation, not the speed of movement
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(+350,0) #starting point of paddle

#Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Player A: 0 Player B: 0",align="center", font=("Courier",24,"normal"))

# Functions
"""
The functions bellow are created to give movement to the paddles
"""
def paddle_a_up():
    y = paddle_a.ycor() # returns the y coordinates
    y += 20 # add 20 pictels to y
    paddle_a.sety(y) # give the new y

def paddle_a_down():
    y = paddle_a.ycor() # returns the y coordinates
    y -= 20 # add 20 pictels to y
    paddle_a.sety(y) # give the new y

def paddle_b_up():
    y = paddle_b.ycor() # returns the y coordinates
    y += 20 # add 20 pictels to y
    paddle_b.sety(y) # give the new y

def paddle_b_down():
    y = paddle_b.ycor() # returns the y coordinates
    y -= 20 # add 20 pictels to y
    paddle_b.sety(y) # give the new y

# Keyboard binding
wn.listen() # interacts with the keyboard
wn.onkeypress(paddle_a_up,"w")
wn.onkeypress(paddle_a_down,"s")
wn.onkeypress(paddle_b_up,"Up")
wn.onkeypress(paddle_b_down,"Down")




# Ball
ball = turtle.Turtle() # turtle object that defines the paddle
ball.speed(0) # the speed of annimation, not the speed of movement
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0,0) #starting point of paddle
ball.dx = 0.3 # movement of ball by 2 in x
ball.dy = 0.3 # movement of ball by 2 in y



# Main game loop
"""
Every time that the loop is running the windo will be update,
so the goal of it is to manualy update the windo
"""
while True:
    wn.update() # this functions updates the windo

    # Movement of the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border checking
    if ball.ycor()>290:
        ball.sety(290)
        ball.dy *= -1
        os.system("afplay bounce.wav&") #for mac is afplay
        #for linux is aplay

    if ball.ycor()<-290:
        ball.sety(-290)
        ball.dy *= -1
        os.system("afplay bounce.wav&")

    if ball.xcor()> 390:
        ball.goto(0,0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("Player A: {} Player B: {}".format(score_a,score_b)\
        ,align="center", font=("Courier",24,"normal"))


    if ball.xcor()< -390:
        ball.goto(0,0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("Player A: {} Player B: {}".format(score_a,score_b)\
        ,align="center", font=("Courier",24,"normal"))

    # Paddle and ball collisions
    if (ball.xcor() > 340 and ball.xcor()< 350) and (ball.ycor() < paddle_b.ycor() + 40 and \
    ball.ycor() > paddle_b.ycor() - 40):
        ball.setx(340)
        ball.dx *= -1
        os.system("afplay bounce.wav&")

    if (ball.xcor() < -340 and ball.xcor()> -350) and (ball.ycor() < paddle_a.ycor() + 40 and \
    ball.ycor() > paddle_a.ycor() - 40):
        ball.setx(-340)
        ball.dx *= -1
        os.system("afplay bounce.wav&")
# In[ ]:
