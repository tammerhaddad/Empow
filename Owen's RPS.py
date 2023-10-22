from turtle import *
import time
import random
difvalue = 0
plyspd = 0
dif = input('how hard do you want your game to be? easy, medium, or hard?')
if dif == "easy":
    difvalue = 1
    plyspd = 3
if dif == "medium":
    difvalue = 2
    plyspd = 2
if dif == "hard":
    difvalue = 3
    plyspd = 1
screen = Screen()
screen.setup(width=500,height=500)
screen.tracer(0)
class Player(Turtle):
    def __init__(self):
        Turtle.__init__(self)
        self.penup()
        self.shape('turtle')
        self.goto(-200,0)
        self.color('blue')
        
    def turn(self,x,y):
        newheading = self.towards(x,y)
        self.setheading(newheading)
player = Player()
screen.onclick(player.turn)
def play():
    counter = 0
    while True:
        player.forward(plyspd)
        if abs(player.xcor()) > 250 or abs(player.ycor()) > 250:
            player.backward(plyspd)
        screen.update()
        time.sleep(1/60)
        counter += 1
        if counter % 10 == 0:
            Projectile(0,0,random.randrange(0,360))
        for p in Projectile.alive:
            p.forward(difvalue)
            if abs(p.xcor()) > 250 or abs(p.ycor()) > 250:
                p.hideturtle()
                Projectile.alive.remove(p)
            if p.distance(player) < 15:
                screen.clear()
                hideturtle()
                write("GAME OVER", align= 'center',font=('Impact',20,'normal'))
                screen.update()
                time.sleep(3)
                screen.bye()
                return

class Projectile(Turtle):
    alive = []

    def __init__(self, x, y, heading):
        Turtle.__init__(self)
        self.penup()
        self.shape('arrow')
        self.goto(x,y)
        self.setheading(heading)
        self.alive.append(self)
   


play()
