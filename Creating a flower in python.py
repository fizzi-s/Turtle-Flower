#Creating a flower in Python 
import turtle 
pen = turtle.Turtle()
pen.speed(2)
pen.color("light blue")
for i in range(6):
  pen.begin_fill()
  pen.circle(100, 60)
  pen.left(120)
  pen.circle(100,60)
  pen.left(120)
  pen.left(60)
  pen.end_fill()
 
pen.penup()
pen.goto(0,-20)
pen.pendown()
pen.color("yellow")
pen.begin_fill()
pen.circle(20)
pen.end_fill()
pen.hideturtle()
turtle.done()
