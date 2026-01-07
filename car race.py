import turtle
road=turtle.Screen()
road.bgpic("race.gif")
road.addshape("red car.gif")
road.addshape("blue car.gif")

redcar=turtle.Turtle()
redcar.shape("red car.gif")
redcar.setheading(90)
redcar.penup()
redcar.goto(-100,-240)

bluecar=turtle.Turtle()
bluecar.shape("blue car.gif")
bluecar.setheading(90)
bluecar.penup()
bluecar.goto(100,-240)

def player1():
    redcar.forward(10)
def player2():
    bluecar.forward(10)

turtle.onkeypress(player1,"Up")
turtle.onkeypress(player2,"W")
turtle.listen()

while True:
    road.update()
    if redcar.pos()>(-100,200):
        road.bgpic("redfinish.gif")
    if bluecar.pos()>(100,200):
        road.bgpic("blue finish.gif")
     
turtle.done()