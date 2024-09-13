import turtle

# Set up the screen
screen = turtle.Screen()
screen.setup(width=800, height=600)  # Correct size for proper viewing
screen.bgcolor("black")  # Black background for better contrast

# Create turtle object
t = turtle.Turtle()
t.speed(3)
t.pensize(5)

# Colors for the 3D effect
colors = ["red", "blue", "green","black", "purple", "orange", "yellow"]

# Function to draw 3D effect text
def draw_3d_text(text, x, y, depth=10, angle=30):
    t.penup()
    t.goto(x, y)
    t.pendown()

    # Draw the shadow effect to simulate 3D depth
    for i in range(depth):
        t.pencolor(colors[i % len(colors)])  # Cycle through colors
        t.penup()
        t.goto(x - i * 2, y - i * 2)  # Offset slightly for depth effect
        t.setheading(angle)  # Slight tilt to give a 3D slant
        t.pendown()
        t.write(text, font=("Arial", 60, "bold"))

# Function to draw a colorful spiral (YouTube-related figure)
def draw_spiral(x, y, size):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.speed(0)  # Max speed for drawing
    for i in range(100):
        t.pencolor(colors[i % 6])  # Use the color pattern
        t.circle(i * size, 45)  # Draw a spiral shape
        t.left(30)

# Function to draw a starburst (another YouTube-related figure)
def draw_starburst(x, y, size):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.speed(5)
    t.pensize(2)
    for i in range(36):
        t.pencolor(colors[i % 6])  # Cycle through colors
        t.forward(size)
        t.backward(size)
        t.left(10)

def draw_text(text, x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()
    
    # Draw text with alternating colors and shadows
    for i, char in enumerate(text):
        t.pencolor(colors[i % len(colors)])
        t.penup()
        t.goto(x + i * 42, y)  # Position each character with a slight offset
        t.pendown()
        t.write(char, font=("Arial", 20, "underline"))
        
        # Draw shadow effect
        t.pencolor("gray")
        t.penup()
        t.goto(x + i * 42 + 2, y - 2)  # Slightly offset for shadow
        t.pendown()
        t.write(char, font=("Arial", 20, "underline"))



# Call the function to draw 3D "dggos960"
draw_3d_text("dggos960", -250, 100)

# Add a spiral on the left side
draw_spiral(-300, -150, 1)

# Add a starburst on the right side
draw_starburst(250, -150, 100)

# Add the text at the bottom
draw_text("Python Programming", -350, 0)


# Hide the turtle after drawing
t.hideturtle()

# Keep the window open
turtle.done()

