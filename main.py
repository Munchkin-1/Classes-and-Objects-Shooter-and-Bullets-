from turtle import *
import random

def generate_color():
    return f"#{random.randint(0, 0xFFFFFF):06x}"

def playing_area():
    pen = Turtle()
    pen.ht()
    pen.speed(0)
    pen.color('teal')
    pen.begin_fill()
    pen.goto(-240,240)
    pen.goto(240,240)
    pen.goto(240,-240)
    pen.goto(-240,-240)
    pen.goto(-240,240)
    pen.end_fill()
    
class Player(Turtle):
    def __init__(self, x, y, color, screen, right_key, left_key):
        super().__init__()
        self.ht()
        self.speed(0)
        self.color(color)
        self.penup()
        self.goto(x,y)
        self.setheading(90)
        self.shape("turtle")
        self.bullets = []
        self.alive = True
        self.st()
        screen.onkeypress(self.turn_left, left_key)
        screen.onkeypress(self.turn_right, right_key)
        
    def fire(self):
        
        self.bullets.append(Bullet(self))

    def turn_left(self):
        self.left(10)

    def turn_right(self):
        self.right(10)

    def move(self):
        self.forward(4)
        
        if self.xcor() > 230 or self.xcor() < -230:
            self.setheading(180 - self.heading())
        if self.ycor() > 230 or self.ycor() < -230:
            self.setheading(-self.heading())

class Bullet(Turtle):
    def __init__(self, player):
        super().__init__()
        self.ht()
        self.speed(0)
        
        self.color(player.pencolor()) 
        self.penup()
        self.goto(player.xcor(), player.ycor())
        self.setheading(player.heading())
        self.shape("triangle")
        self.forward(15) 
        self.player = player
        self.st()

    def move(self):
        self.forward(10)
        if self.xcor() > 230 or self.xcor() < -230 or self.ycor() > 230 or self.ycor() < -230:
            self.remove()

    def remove(self):
        if self in self.player.bullets:
            self.ht()
            self.player.bullets.remove(self)


screen = Screen()
screen.bgcolor("black")
screen.setup(520,520)

screen.listen()

playing_area()

p1 = Player(-100, 0, "red", screen, "d", "a")
p2 = Player(100, 0, "blue", screen, "Right", "Left")

screen.onkeypress(p1.fire, "w")
screen.onkeypress(p2.fire, "Up")


while p1.alive and p2.alive:
    p1.move()
    p2.move()
    
    for b in p1.bullets:
        b.move()
        if b.distance(p2) < 20:   
            p2.alive = False      
            b.remove()
            
    for b in p2.bullets:
        b.move()
        if b.distance(p1) < 20:   
            p1.alive = False      
            b.remove()

screen.exitonclick()