import turtle
turtle.Screen().bgcolor("blue")
turtle.Screen().setup(400,400)
poly = turtle.Turtle()
sides = 6
side_length = 80
angle = 360 / sides
for i in range(sides):
  poly.forward(side_length)
  poly.right(angle)
turtle.done()