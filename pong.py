import turtle
import os

window = turtle.Screen()
window.title("Pong with Hom")
window.bgcolor('black')
window.setup(800, 600)
# This makes th game update manually, to speed up the performance
window.tracer()

# Score variables
score_a = 0
score_b = 0
# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0) # Max animation speed
paddle_a.shape("square")
paddle_a.color('white')
paddle_a.shapesize(stretch_wid=5, stretch_len=1) # 5 * 20(default side of square) = 100 pixels in width
paddle_a.penup()
paddle_a.goto(-350, 0)

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0) 
paddle_b.shape("square")
paddle_b.color('white')
paddle_b.shapesize(stretch_wid=5, stretch_len=1) 
paddle_b.penup()
paddle_b.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0) 
ball.shape("circle")
ball.color('white')
ball.penup()
ball.goto(0, 0)
# This basically means our ball moves by 2 pixels everytime
ball.dx = 2 # Delta x or change in x
ball.dy = 2

# Score printer

pen = turtle.Turtle()
pen.speed(0)
pen.color('white')
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write('Player A: 0   Player B: 0', align='center', font=('Courier', 24, 'normal'))

def paddle_a_up():
    y = paddle_a.ycor()
    y += 20 
    paddle_a.sety(y) 

def paddle_a_down():
    y = paddle_a.ycor()
    y += -20 
    paddle_a.sety(y) 

def paddle_b_up():
    y = paddle_b.ycor()
    y += 20 
    paddle_b.sety(y) 

def paddle_b_down():
    y = paddle_b.ycor()
    y += -20 
    paddle_b.sety(y)

# Binding keys to the function
window.listen() # checks for keyboard input
window.onkeypress(paddle_a_up, "w")
window.onkeypress(paddle_a_down, "s")
window.onkeypress(paddle_b_up, "Up")
window.onkeypress(paddle_b_down, "Down")


# Main game loop
while True:
    window.update()
    # Move ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        os.system('afplay bounceAudio.wav&')

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        os.system('afplay bounceAudio.wav&')

    
    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx = -1.5
        score_a += 1
        pen.clear()
        pen.write(f'Player A: {score_a}   Player B: {score_b}', align='center', font=('Courier', 24, 'normal'))
    
    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx = -1.5
        score_b += 1
        pen.clear()
        pen.write(f'Player A: {score_a}   Player B: {score_b}', align='center', font=('Courier', 24, 'normal'))


    # Paddle and ball collision

    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() - 40):
        ball.setx(340)
        ball.dx *= -1
        os.system('afplay bounceAudio.wav&')
    
    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() - 40):
        ball.setx(-340)
        ball.dx *= -1    
        os.system('afplay bounceAudio.wav&')
