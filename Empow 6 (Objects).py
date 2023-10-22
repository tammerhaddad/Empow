from turtle import *
import time
import random

width = 500
height = 500
screen = Screen()
screen.setup(width=width, height=height)
screen.tracer(0)

class Player(Turtle):
    def __init__(self):
        Turtle.__init__(self)
        self.penup()
        self.shape('turtle')
        self.goto(-200,0)
        self.color('blue')

    def turn(self, x, y):
        direction = self.towards(x, y)
        self.setheading(direction)

class Projectile(Turtle):
    alive = []
    
    def __init__(self, x, y, heading):
        Turtle.__init__(self)
        self.penup()
        self.shape('arrow')
        self.goto(x,y)
        self.setheading(heading)
        self.alive.append(self)

def play():
    
    player = Player()
    counter = 0
    turtleSpeed = 4
    arrowSpeed = 1.0
    score = 0
    while True:
        canvas = getcanvas()
        x, y = canvas.winfo_pointerx(), canvas.winfo_pointery()
        print(x, " - ", y)
        arrowSpeed += 0.01
        counter += 1
        if counter % int(20/arrowSpeed) == 0:
            score += 1
            Projectile(width/2,random.randint(-1*height/2, height/2),180)
        #screen.onclick(player.turn)
        player.turn(x, y)
        player.forward(turtleSpeed)
        if abs(player.xcor()) > width/2 or abs(player.ycor()) > height/2:
            player.backward(turtleSpeed)
        for p in Projectile.alive:
            if abs(p.xcor()) > height/2 or abs(p.ycor()) > width/2:
                p.hideturtle()
                Projectile.alive.remove(p)
            p.forward(arrowSpeed)
            if p.distance(player) < 15:
                screen.clear()
                hideturtle()
                write("GAME OVER, you got: " + str(score), align='center',font=('Impact',20,'normal'))
                screen.update()
                time.sleep(3)
                screen.bye()
        screen.update()
        time.sleep(1/60)

play()
