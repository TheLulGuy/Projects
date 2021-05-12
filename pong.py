import turtle

window = turtle.Screen()
window.title("Pong with Hom")
window.bgcolor('black')
window.setup(800, 600)
# This makes th game update manually, to speed up the performance
window.tracer()

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
ball.shape("square")
ball.color('white')
ball.penup()
ball.goto(0, 0)
# This basically means our ball moves by 2 pixels everytime
ball.dx = 3 # Delta x or change in x
ball.dy = -3

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

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
    
    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx = -1.5
    
    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx = -1.5

    # Paddle and ball collision

    if (ball.xcor() > 345 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() < -40):
        ball.setx(340)
        ball.dx *= -1
