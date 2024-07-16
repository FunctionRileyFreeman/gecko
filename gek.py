import turtle

# Function to draw the gecko's body
def draw_body():
    turtle.penup()
    turtle.goto(0, -50)
    turtle.pendown()
    turtle.circle(50)

# Function to draw the gecko's head
def draw_head():
    turtle.penup()
    turtle.goto(0, 50)
    turtle.pendown()
    turtle.circle(30)

# Function to draw a leg
def draw_leg(x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.circle(20)

# Function to draw the gecko
def draw_gecko():
    turtle.speed(1)
    turtle.color("green")
    
    # Draw body
    draw_body()
    
    # Draw head
    draw_head()
    
    # Draw legs
    draw_leg(-50, 0)
    draw_leg(50, 0)
    draw_leg(-30, -70)
    draw_leg(30, -70)
    
    turtle.hideturtle()

# Initialize turtle
turtle.Screen().bgcolor("lightblue")

# Draw the gecko
draw_gecko()

# Finish drawing
turtle.done()
