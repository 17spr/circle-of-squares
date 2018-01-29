import turtle

my_turtle = turtle.Turtle()
my_turtle.speed(.0005)


def square(length, angle):
    for i in range(4):
        my_turtle.forward(length)
        my_turtle.right(angle)

# looping square
for i in range(1000):
    square(100, 90)
    my_turtle.right(11)
    
    
    
    
    
