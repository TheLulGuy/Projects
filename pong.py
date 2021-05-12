import turtle

wm = turtle.Screen()
wm.title("Pong with Hom")
wm.bgcolor('black')
wm.setup(800, 600)
# This makes th game update manually, to speed up the performance
wm.tracer()

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
# Main game loop
while True:
    wm.update()
