# CTI 110
# P3LAB2
# Anthony Davis
# 14 Oct 20201

# Some turtle graphics

# Part 1 - draw a triangle and a square.
import turtle
t = turtle.Turtle()
s = turtle.Turtle()

# Set pen color, size, speed if you like.
t.pencolor("red")
t.pensize (2)
t.speed (2)
s.pencolor("blue")
s.pensize (2)
s.speed (2)

for side in [1, 2, 3, 4]:
    t.forward (100)
    t.left (120)
    s.forward (100)
    s.left (90)
    

t.penup()
t.forward (-100)
t.pendown()
t.right (120)
t.right (120)
t.forward (100)
t.backward (100)
t.left (60)
t.forward (100)
t.backward (50)
t.right (120)
t.forward (50)

s.penup()
s.forward (250)
s.right (90)
s.forward (90)
s.left (90)
s.pendown()
s.right (90)
s.forward (90)
s.left (90)
s.circle (45, 190) # Half circle. 
