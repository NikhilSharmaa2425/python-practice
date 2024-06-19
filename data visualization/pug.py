import turtle

# Set up the screen
screen = turtle.Screen()
screen.setup(width=600, height=600)
# screen.bgcolor("skyblue")

# Create a turtle object
dog = turtle.Turtle()
dog.speed(3)

# Draw the dog's body
dog.penup()
dog.goto(0, -100)
dog.pendown()
dog.begin_fill()
dog.circle(100)
# dog.end_fill()

# Draw the dog's head
dog.penup()
dog.goto(0, 0)
dog.pendown()
dog.begin_fill()
dog.circle(50)
# dog.end_fill()

# Draw the dog's ears
dog.penup()
dog.goto(35, 50)
dog.pendown()
dog.setheading(60)
dog.begin_fill()
dog.circle(15, -100)
# dog.end_fill()

dog.penup()
dog.goto(-35, 50)
dog.pendown()
dog.setheading(120)
dog.begin_fill()
dog.circle(15, 100)
# dog.end_fill()

# Draw the dog's eyes
dog.penup()
dog.goto(15, 20)
dog.pendown()
# dog.dot(7, "black")

dog.penup()
dog.goto(-15, 20)
dog.pendown()
# dog.dot(7, "black")

# Draw the dog's nose
dog.penup()
dog.goto(0, -5)
dog.pendown()
# dog.dot(10, "black")

# Draw the dog's mouth
dog.penup()
dog.goto(0, -20)
dog.pendown()
dog.setheading(-60)
dog.circle(15, 120)

# Hide the turtle
dog.hideturtle()

# Keep the window open
screen.mainloop()
