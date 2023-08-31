from turtle import *

tsize = 20
s_width = 200
s_height = 180

class Sprite(Turtle):
    def __init__(self, x, y, clr,shp):
        Turtle.__init__(self)
        self.penup()
        self.speed(0)
        self.goto(x, y)
        self.color(clr)
        self.shape(shp)
        self.x = x
        self.y = y
        self.step = 10

    def move_up(self):
        self.goto(self.xcor(), self.ycor() + self.step)
        for wall in walls:
            if wall.is_collision(self):
                self.goto(self.xcor(), self.ycor() - self.step)

    def move_down(self):
        self.goto(self.xcor(), self.ycor() - self.step)
        for wall in walls:
            if wall.is_collision(self):
                self.goto(self.xcor(), self.ycor() + self.step)

    def move_left(self):
        self.goto(self.xcor() - self.step, self.ycor())
        for wall in walls:
            if wall.is_collision(self):
                self.goto(self.xcor() + self.step, self.ycor())

    def move_right(self):
        self.goto(self.xcor() + self.step, self.ycor())
        for wall in walls:
            if wall.is_collision(self):
                self.goto(self.xcor() - self.step, self.ycor())

    def is_collide(self, sprite):
        dist = self.distance(sprite.xcor(), sprite.ycor())
        if dist < 30:
            return True
        else:
            return False

    def lose(self):
        self.goto(-200, 0)
        self.showturtle()
        self.color('red')
        self.write('WASTED', font=('Arial', 70, 'bold'))
        self.hideturtle()

    def do_star(self):
        self.pendown()
        self.begin_fill()
        for i in range(5):
            self.left(144)
            self.fd(100)
        self.end_fill()

    def teleport(self):
        self.goto(self.x,self.y)

    def win(self):
        self.goto(-180, 0)
        self.showturtle()
        self.color('red')
        self.write('WIN', font=('Arial', 70, 'bold'))
        t = -150
        self.color('yellow')
        for i in range (3):
            self.goto(t, -100)
            self.do_star()
            self.penup()
            t+=120
        self.hideturtle()



class Wall(Turtle):
    def __init__(self,x,y):
        super().__init__()
        self.speed(0)
        self.color('blue')
        self.shape('square')
        self.x = x
        self.y=y
        self.width = 40
        self.height = 40
        self.penup()
        self.goto(self.x,self.y)

    def is_collision(self, other):
        if (self.xcor() + self.width / 2) > other.xcor() - 6 and \
                (self.xcor() - self.width / 2) < other.xcor() + 6 and \
                (self.ycor() + self.height / 2) > other.ycor() - 6 and \
                (self.ycor() - self.height / 2) < other.ycor() + 6:
            return True
        else:
            return False

class Arrow(Turtle):
    def __init__(self, x, y):
        Turtle.__init__(self)
        self.penup()
        self.speed(0)
        self.goto(x, y)
        self.color('red')
        self.shape('arrow')
        self.step = 5
        self.width = 20
        self.height = 20

    def set_move(self, x_start, y_start, x_end, y_end):
        self.x_start = x_start
        self.y_start = y_start
        self.x_end = x_end
        self.y_end = y_end
        self.goto(x_start, y_start)
        self.step = 5
        self.setheading(self.towards(x_end, y_end))  # направление

    def make_step(self):
        self.forward(self.step)
        if self.distance(self.x_end, self.y_end) < self.step:
            self.set_move(self.x_end, self.y_end, self.x_start, self.y_start)
walls = []

for i in range(-295, 197, 15):
    walls.append(Wall(i, -275))
    walls.append(Wall(i, 200))

for i in range(-275, 207, 15):
    walls.append(Wall(-295, i))
    walls.append(Wall(190, i))

for i in range(-175, 120, 15):
    walls.append(Wall(100,i))

for i in range(-275, 120, 15):
    walls.append(Wall(-200, i))

for i in range(-100, 110, 15):
    walls.append(Wall(i, 110))

for i in range(-100, 20, 15):
    walls.append(Wall(i, -175))

for i in range(-200, 25, 15):
    walls.append(Wall(i, -70))

for i in range(-175, -20, 15):
    walls.append(Wall(-100, i))

for i in range(25, 110, 15):
    walls.append(Wall(-30, i))

for i in range(-200, -150, 15):
    walls.append(Wall(i, 40))

player = Sprite(-150, -30, 'black','turtle')
player2 = Sprite(-150, -100, 'red','turtle')

tp1 = Sprite(-70,-45,'yellow','circle')
tp2 = Sprite(-175,65,'yellow','circle')
tp3 = Sprite(75,-175,'yellow','circle')
tp4 = Sprite(35,-70,'yellow','circle')
tp5 = Sprite(-175,-175,'yellow','circle')
tp6 = Sprite(160,-250,'yellow','circle')
tpts = (tp1,tp2,tp3,tp4,tp5,tp6)


scr = player.getscreen()
scr.bgcolor('light blue')

ob1 = Arrow(0, 150)
ob2 = Arrow(200, -140)
ob3 = Arrow(-300, 75)
obj = (ob1,ob2,ob3)

ob1.set_move(0, 200, 0, -250)
ob2.set_move(200, -140, -290, -140)
ob3.set_move(-300, 75, 200, 75)

scr.onkey(player.move_up, 'Up')
scr.onkey(player.move_left, 'Left')
scr.onkey(player.move_right, 'Right')
scr.onkey(player.move_down, 'Down')
scr.listen() 

def cl():
    player.hideturtle()
    player2.hideturtle()
    for i in obj:
        i.hideturtle()
    for t in tpts:
        t.hideturtle()
    for w in walls:
        w.hideturtle()

while True:
    ob1.make_step()
    ob2.make_step()
    ob3.make_step()
    if player.is_collide(ob1) or player.is_collide(ob2) or player.is_collide(ob3):
        cl()
        player.lose()
        break
    if player.is_collide(tp1) or player.is_collide(tp2) or player.is_collide(tp3) or player.is_collide(tp4) or player.is_collide(tp5)\
            or player.is_collide(tp6):
        player.teleport()
    if player.is_collide(player2):
        cl()
        player.win()
        break

done()