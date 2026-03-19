#Creating a flower in Python 
import turtle 
pen = turtle.Turtle()  
pen.speed(3)
pen.color("light blue")
for i in range(6):  #loop draws 6 petals
  pen.begin_fill()
  pen.circle(100, 60)  #1st arc of petal
  pen.left(120)  
  pen.circle(100,60)  #2nd arc of petal 
  pen.left(120)   #positioning for next petal
  pen.left(60)   #adjusting for symmetry 
  pen.end_fill()   #fill shape

#Corona of flower 
pen.penup()   #pen lifted such that no line is drawn
pen.goto(0,-20)   #pen in the middle of all the petals
pen.pendown()   #pen down to draw pistil
pen.color("yellow")
pen.begin_fill()
pen.circle(20)    #small circle drawn
pen.end_fill()
pen.hideturtle()  
turtle.done()
