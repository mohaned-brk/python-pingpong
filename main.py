import turtle
screen=turtle.Screen()
screen.bgcolor("black")
screen.title("my game")
screen.setup(700,700)
t=turtle.Turtle()
t.hideturtle()
t.penup()
t.goto(-300,300)
t.pendown()
t.speed(5)
t.color('white')
t.pensize(3)
for i in range(4):
    t.forward(600)
    t.right(90)








#paddels
Upaddel=turtle.Turtle()
Upaddel.fillcolor("blue")
Upaddel.pensize(1)
Upaddel.shape("square")
Upaddel.shapesize(0.25, 3)
Upaddel.penup()
Upaddel.goto(0, 270)
Upaddel.end_fill()


Dpaddel=turtle.Turtle()
Dpaddel.fillcolor("red")
Dpaddel.pensize(1)
Dpaddel.shape("square")
Dpaddel.shapesize(0.25, 3)
Dpaddel.penup()
Dpaddel.goto(0, -250)
Dpaddel.end_fill()

#ball
Ball=turtle.Turtle()
Ball.color("white")
Ball.shape("circle")
Ball.shapesize(0.75,0.75)
Ball.dx =4
Ball.dy =4
Ball.penup()

#function to move paddels:
def Upaddelr():
   u=Upaddel.xcor()
   if u < 590:
       u=u+100
   Upaddel.setx(u)

def Dpaddelr():
   u=Dpaddel.xcor()
   if u < 590:
       u=u+50
   Dpaddel.setx(u)
def Upaddell():
   u=Upaddel.xcor()
   if u > -590:
       u=u-50
   Upaddel.setx(u)
def Dpaddell():
   u=Dpaddel.xcor()
   if u > -590:
       u=u-50
   Dpaddel.setx(u)
def scores(p1,p2) :
    score.hideturtle()
    score.pensize(3)
    score.penup()
    score.goto(0, 0)
    score.pendown()
    score.color("white")
    score.forward(60)
    score.back(120)
    score.penup()
    score.goto(0, 50)
    score.color("blue")
    score.write(p1,6,font = "Arial")
    score.pendown()
    score.penup()
    score.goto(0, -50)
    score.color("red")
    score.write(p2 ,6,font = "Arial" )
    score.pendown()
    Ball.sety(0)
    Ball.setx(0)
    Ball.dx=4
    Ball.dy=4


screen.listen()
screen.onkeypress(Upaddelr, "Right")
screen.onkeypress(Upaddell, "Left")
screen.onkeypress(Dpaddelr, "d")
screen.onkeypress(Dpaddell, "q")
p1=p2=x=0
score = turtle.Turtle()


while( 1!=0 ):
    screen.update()
    Ball.setx(Ball.xcor() + Ball.dx)
    Ball.sety(Ball.ycor() + Ball.dy)
    if Ball.xcor() < -289:
        Ball.setx(-290)
        Ball.dx = (abs(Ball.dx)+2 )

    elif Ball.xcor() > 289:
        Ball.dx = (Ball.dx+2 )* -1
        Ball.setx(290)

    elif Ball.dy > 0 and Upaddel.xcor()-35 < Ball.xcor() < Upaddel.xcor()+35 and Ball.ycor() > 270:
        Ball.color("blue")
        Ball.dy = (Ball.dy+3)*-1
        Ball.sety(270)


    elif Ball.dy < 0 and Dpaddel.xcor()-35 < Ball.xcor() < Dpaddel.xcor()+35 and Ball.ycor() < -250:
        Ball.color("red")
        Ball.dy = (abs(Ball.dy)+3)
        Ball.sety(-250)
    elif Ball.ycor() > 275:
        p2=p2+1
        scores(p1,p2)

        score.clear()


    elif Ball.ycor() < -255:
       p1=p1+1
       scores(p1,p2)
       score.clear()





    else:
        continue
