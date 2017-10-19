# CTI-110
# M5T1 - Turtle Initials
# William Thomas
# 12 October 2017
# Program to draw initials (W & T) with turtle graphics.
 
def turtleinitials():
    # Import turtle graphics.
    import turtle
    # Create canvas.
    wn = turtle.Screen()
    # Set title.
    wn.title("Initials")
    # Rename turtle & set attributes.
    boba = turtle.Turtle()
    boba.pensize(6)
    boba.color("blue")
    # Reposition boba
    boba.penup()
    boba.forward(-150)
    boba.pendown()
    # Set boba pathing for "W".
    boba.right(60)
    boba.forward(130)
    boba.left(120)
    boba.forward(80)
    boba.right(120)
    boba.forward(80)
    boba.left(120)
    boba.forward(130)
    # lift pen and reposition for second letter.
    boba.penup()
    boba.right(60)
    boba.forward(50)
    boba.pendown()
    # Set boba pathing for "T".
    boba.forward(80)
    boba.penup()
    boba.forward(-40)
    boba.pendown()
    boba.right(90)
    boba.forward(110)
    # Wait for user to close window.
    wn.mainloop()
# Run program.
turtleinitials()
