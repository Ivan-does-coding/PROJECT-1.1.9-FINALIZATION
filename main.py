import turtle as t

# The base + fill color of the Island
t.pensize(7)
t.penup()
t.setposition(-100,-25)
t.color("black")
t.begin_fill()
t.forward(200)
t.left(120)
t.pendown()

# The right face of the Island base 
t.forward(20)
t.right(32.5)
t.forward(30)
t.left(92.5)
t.forward(200)
t.left(120)

#The left face of the Island base
t.forward(30)
t.right(22.5)
t.forward(20)
t.color("saddle brown")
t.end_fill()

t.left(82.5)


#base ocean color
t.penup()
t.setposition(-200, -125)
t.pendown()
t.pensize(210)
t.pencolor("dark blue")
t.forward(400)
t.pensize(10)

#the wave function
def wave():
    t.pencolor("dark blue")
    t.fillcolor("dark blue")
    t.begin_fill()
    t.circle(80, 70)
    t.left(90)
    t.forward(90)
    t.left(160)
    t.circle(-80, 50)
    t.end_fill()

#set up waves
t.right(160)

#drawing the waves
space = + -120
while (300 > space):
    wave()
    t.penup()
    t.setposition(space, 5)
    t.pendown()
    t.right(275)
    space = space + 90

t.penup()
t.goto(-20,100)
t.left(185)
t.pendown()
t.color("black")
t.penup()

t.goto(0,175)

#This is the main wall (Triangle)
t.color("darkslategray")
t.pensize(7)
t.begin_fill()
t.right(90)
t.forward(50)
t.pendown()
t.left(90)
t.forward(25)
t.left(120)
t.forward(50)
t.end_fill()
t.penup()
t.left(80)
t.forward(60)
t.left(140)



#This will be the block that has slipped off the wall.
t.pendown()
t.color("darkslategray")
t.begin_fill()
for i in range (4):
  t.forward(25)
  t.right(90)
t.end_fill()

t.penup()
t.goto(-20,100)
t.left(20)


### Setting position for island creation (first half)
t.left(90)
t.forward(20)
t.left(90)

### Drawing island from center top to bottom LEFT
t.begin_fill()
t.pendown()
t.color("forest green")
for i in range(5):
  t.right(5)
  t.forward(15)
t.forward(20)
for i in range(3):
  t.left(10)
  t.forward(15)
t.color("black")
for i in range(4):
  t.left(30)
  t.forward(3)
t.forward(30)
for i in range(5):
  t.right(5)
  t.forward(20)

### Resetting position for island creation (second half)
t.penup()
t.setposition(-20,100)
t.left(175)
t.forward(20)
t.right(90)


### Drawing island from center top to bottom RIGHT
t.pendown()
t.color("forest green")
t.forward(35)
t.right(5)
t.forward(35)
for i in range(3):
  t.left(10)
  t.forward(15)
t.color("black")
for i in range(5):
  t.forward(5)
  t.right(30)
t.forward(30)
for i in range(3):
  t.forward(10)
  t.left(5)
t.left(30)
t.forward(30)
for i in range(3):
  t.right(5)
  t.forward(10)

### Connect RIGHT and LEFT + Fill color grey
t.right(90)
t.forward(195)
t.right(90)
t.forward(7)
t.color("grey")
t.end_fill()

t.right(45)
t.color("black")
t.forward(15)
t.color("grey")
t.pensize(15)
t.forward(106)

t.penup()
t.right(45)

t.goto(-150,150)

#Small Square Ruin
t.pensize(5)

l = 0
t.begin_fill()
while (l < 2):
  t.color("darkslategray")
  t.forward(25)
  t.left(90)
  t.forward(30)
  t.left(90)
  l = l + 1
t.end_fill()

#Draw Shrubbury Details

def medium_bush():
  for i in range(6):
    t.pensize(7)
    t.begin_fill()
    t.color("green")
    t.circle(4)
    t.end_fill()
    t.right(40)
    t.forward(5)

def main_bush():
    t.color("forest green")
    t.circle(4)
    t.left(90)
    t.forward(8)
    t.right(90)
    t.circle(4/2)
    t.left(90)
    t.forward(8)
    t.right(90)
    t.circle(4/4)
    t.left(90)
    t.forward(8)
    t.right(90)

def small_grass():
  t.pensize(3)
  t.color("olive drab")
  t.left(90)
  t.circle(4,90)
  t.penup()
  t.circle(4,270)
  t.pendown()
  t.forward(4)
  t.backward(4)
  t.right(180)
  t.penup()
  t.circle(4,270)
  t.pendown()
  t.circle(4,90)

#Draw medium bush
t.penup()
t.goto(65,135)
t.pendown()
t.left(120)
medium_bush()
t.right(50)
t.forward(10)
t.right(130)
t.pensize(9)
t.forward(10)

#Draw main bush
t.penup()
t.goto(-110,145)
t.right(55)
t.pendown()
main_bush()

# Draw small grass
t.penup()
t.goto(-40,145)
t.right(20)
t.pendown()
small_grass()

#Show turtle jump into ocean
t.penup()
t.goto(-150,150)
t.shape("turtle")
t.showturtle()
t.speed(1)
t.goto(-100,-150)

wn = t.Screen()
wn.mainloop()
