# CTI-110
# M5T1 - Turtle Bonus
# William Thomas
# 19 October 2017
# Program to draw a snowflake (or in my case, a ninja star) turtle graphics.

def turtlebonus():
    # Import turtle graphics.
    import turtle
    # Create canvas.
    wn = turtle.Screen()
    # Set title.
    wn.title("Super Sweet Throwing Star")
    # Rename turtle "s" & set attributes.
    star = turtle.Turtle()
    star.pensize(6)
    star.color("blue")
    # Position s.t.a. at start points.
    star.left(60)
    # Set s.t.a. pathing.
    for i in range(3):   
        star.forward(90)
        star.left(60)
        star.forward(30)       
        star.right(120)       
        star.forward(30)        
        star.left(60)      
        star.forward(60)        
        star.right(120)
        star.forward(150)
        star.right(150)
        star.forward(90)
        star.left(90)
        star.forward(120)
        star.left(120)
        star.forward(30)
        star.right(120)
        star.forward(38)
        star.left(60)
        star.forward(15)        
    # Wait for user to close window.
    wn.mainloop()
    # Run program.
turtlebonus()
