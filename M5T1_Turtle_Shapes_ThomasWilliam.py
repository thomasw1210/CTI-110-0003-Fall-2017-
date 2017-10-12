# CTI-110
# M5T1 - Turtle Shapes
# William Thomas
# 12 October 2017
# Program to draw a square and triangle with turtle graphics.

def turtleshapes():
    # Import turtle graphics.
    import turtle
    # Create canvas.
    wn = turtle.Screen()
    # Set title.
    wn.title("Square & Triangle")
    # Rename turtle & set attributes.
    boba = turtle.Turtle()
    boba.pensize(6)
    boba.color("blue")
    # Create second turtle "jane" & set attributes.
    jane = turtle.Turtle()
    jane.pensize(4)
    jane.color("red")
    # Set boba pathing for square.
    for i in range(4):         
        boba.forward(100)
        boba.right(90)
    # Offset Jane by 100.
    jane.penup()
    jane.left(90)
    jane.forward(100)
    jane.right(90)
    jane.pendown()
    # Set turtle pathing for triangle.
    for x in range(3):
        jane.forward(100)
        jane.left(120)
    # Wait for user to close window.
    wn.mainloop()
# Run program.
turtleshapes()


