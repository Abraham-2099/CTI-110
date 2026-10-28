#Abraham Ochieng
#10/28/2026
#p4 lab1 
#Use turtle and loops to draw a square and triangle 


#import turtle
import turtle

#create a turtle window and drawing object
win = turtle.Screen()
pen  = turtle.Turtle()


#set turtle options
pen.pensize(5)
pen.pencolor("purple")
pen.shape("arrow")

#code to draw the shapes
for side in range(4):
    pen.forward(100)
    pen.right(90) 

#while loop to draw triangle
sides = 3 

while sides > 0:
    pen.forward(100)
    pen.left(120)
    sides = sides - 1

#wait for user to close window
win.mainloop()