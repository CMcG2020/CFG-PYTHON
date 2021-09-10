import turtle

def triangle(side_length, color):
    angle = 120

    turtle.color(color, color)
    turtle.begin_fill()

    for side in range(3):
        turtle.forward(side_length)
        turtle.right(angle)

triangle(400, 'red')
triangle(300, 'pink')
triangle(200, 'blue')
triangle(100, 'yellow')

#2.7
#def circle_area(radius):
#area = 3.14 * (radius ** 2)
#return area
#area = circle_area(9)
#print(area)