import turtle
import random
import time

# Creating window
wn = turtle.Screen()
wn.title("Super Get Around!")
wn.bgcolor("grey")
wn.setup(500, 600)
wn.tracer(0)

# Grasses
grass1 = turtle.Turtle()
grass1.penup()
grass1.shape("square")
grass1.shapesize(50, 15)
grass1.color("limegreen")
grass1.goto(-300, 0)

grass2 = turtle.Turtle()
grass2.penup()
grass2.shape("square")
grass2.shapesize(50, 15)
grass2.color("limegreen")
grass2.goto(300, 0)

# Side lines
side_line1 = turtle.Turtle()
side_line1.penup()
side_line1.shape("square")
side_line1.shapesize(50, 0.4)
side_line1.color("white")
side_line1.goto(-130, 0)

side_line2 = turtle.Turtle()
side_line2.penup()
side_line2.shape("square")
side_line2.shapesize(50, 0.4)
side_line2.color("white")
side_line2.goto(130, 0)

# Lines
line1 = turtle.Turtle()
line1.left(90)
line1.penup()
line1.color("white")
line1.shape("square")
line1.shapesize(0.4, 2)
line1.goto(-65, 0)

line2 = turtle.Turtle()
line2.penup()
line2.left(90)
line2.color("white")
line2.shape("square")
line2.shapesize(0.4, 2)
line2.goto(0, 0)

line3 = turtle.Turtle()
line3.penup()
line3.left(90)
line3.color("white")
line3.shape("square")
line3.shapesize(0.4, 2)
line3.goto(65, 0)

line4 = turtle.Turtle()
line4.left(90)
line4.penup()
line4.color("white")
line4.shape("square")
line4.shapesize(0.4, 2)
line4.goto(-65, 200)

line5 = turtle.Turtle()
line5.penup()
line5.left(90)
line5.color("white")
line5.shape("square")
line5.shapesize(0.4, 2)
line5.goto(0, 200)

line6 = turtle.Turtle()
line6.penup()
line6.left(90)
line6.color("white")
line6.shape("square")
line6.shapesize(0.4, 2)
line6.goto(65, 200)

line7 = turtle.Turtle()
line7.left(90)
line7.penup()
line7.color("white")
line7.shape("square")
line7.shapesize(0.4, 2)
line7.goto(-65, -200)

line8 = turtle.Turtle()
line8.penup()
line8.left(90)
line8.color("white")
line8.shape("square")
line8.shapesize(0.4, 2)
line8.goto(0, -200)

line9 = turtle.Turtle()
line9.penup()
line9.left(90)
line9.color("white")
line9.shape("square")
line9.shapesize(0.4, 2)
line9.goto(65, -200)

# Obstickles
car1 = turtle.Turtle()
car1.penup()
car1.left(90)
car1.color("blue")
car1.shape("square")
car1.shapesize(1.5, 2.5)
car1.goto(-30, 400)

car2 = turtle.Turtle()
car2.penup()
car2.left(90)
car2.color("yellow")
car2.shape("square")
car2.shapesize(1.5, 2.5)
car2.goto(30, 700)

car3 = turtle.Turtle()
car3.penup()
car3.left(90)
car3.color("brown")
car3.shape("square")
car3.shapesize(2, 4.5)
car3.goto(100, 1000)

# Player
player = turtle.Turtle()
player.penup()
player.left(90)
player.color("red")
player.shape("square")
player.shapesize(1.5, 2.5)
player.goto(0, -100)

# Score
pen = turtle.Turtle()
pen.hideturtle()
pen.penup()
pen.goto(0, 220)
pen.color("white")
pen.pendown()
pen.write("0", align = "center", font = ("Impact", 40, "normal"))

pen2 = turtle.Turtle()
pen2.hideturtle()
pen2.penup()
pen2.goto(0, 200)
pen2.color("white")
pen2.pendown()

# Virable
lines_speed = 3.5
car_speed = 0.7
truck_speed = 0.85
score = 0
high_score = 0

# Player movement
def player_left():
    x = player.xcor()
    x -= 20
    player.setx(x)

def player_right():
    x = player.xcor()
    x += 20
    player.setx(x)

def car_slow():
    global car_speed
    global truck_speed
    global lines_speed

    car_speed -= 0.1
    truck_speed -= 0.1
    lines_speed -= 0.2

def car_fast():
    global car_speed
    global truck_speed
    global lines_speed

    car_speed += 0.1
    truck_speed += 0.1
    lines_speed += 0.2

# Keyboard blinding
wn.listen()
wn.onkeypress(player_left, "Left")
wn.onkeypress(player_right, "Right")
wn.onkeypress(car_slow, "Down")
wn.onkeypress(car_fast, "Up")

# Main game loop
while True:
    wn.update()

    # Movement
    line1.backward(lines_speed)
    line2.backward(lines_speed)
    line3.backward(lines_speed)
    line4.backward(lines_speed)
    line5.backward(lines_speed)
    line6.backward(lines_speed)
    line7.backward(lines_speed)
    line8.backward(lines_speed)
    line9.backward(lines_speed)
    car1.backward(car_speed)
    car2.backward(car_speed)
    car3.backward(truck_speed)

    # Speed limit
    if car_speed < 0.1:
        car_speed = 0.1

    if truck_speed < 0.25:
        truck_speed = 0.25

    if lines_speed < 2.5:
        lines_speed = 2.5

    # Boundaries checking
    if line1.ycor() < -310:
        line1.goto(-65, 310)

    if line2.ycor() < -310:
        line2.goto(0, 310)

    if line3.ycor() < -310:
        line3.goto(65, 310)

    if line4.ycor() < -310:
        line4.goto(-65, 310)

    if line5.ycor() < -310:
        line5.goto(0, 310)

    if line6.ycor() < -310:
        line6.goto(65, 310)

    if line7.ycor() < -310:
        line7.goto(-65, 310)

    if line8.ycor() < -310:
        line8.goto(0, 310)

    if line9.ycor() < -310:
        line9.goto(65, 310)

    if player.xcor() < -100:
        player.goto(-100, -100)

    if player.xcor() > 100:
        player.goto(100, -100)
    
    if car1.ycor() < -320:
        x = random.choice([-100, -30, 30, 100])
        car1.goto(x, 320)
        color = random.choice(['orange', 'yellow', 'lime', 'black', 'white', 'blue', 'saddlebrown', 'pink'])
        car1.color(color)

        # Write score
        score += 1
        pen.clear()
        pen.write("{}".format(score), align = "center", font = ("Impact", 40, "normal"))

    if car2.ycor() < -320:
        x = random.choice([-100, -30, 30, 100])
        car2.goto(x, 320)
        color = random.choice(['orange', 'yellow', 'lime', 'black', 'white', 'blue', 'saddlebrown', 'pink'])
        car2.color(color)

        # Write score
        score += 1
        pen.clear()
        pen.write("{}".format(score), align = "center", font = ("Impact", 40, "normal"))

    if car3.ycor() < -330:
        x = random.choice([-100, -30, 30, 100])
        car3.goto(x, 400)
        color = random.choice(['orange', 'yellow', 'lime', 'black', 'white', 'blue', 'saddlebrown', 'pink'])
        car3.color(color)

        # Write score
        score += 1
        pen.clear()
        pen.write("{}".format(score), align = "center", font = ("Impact", 40, "normal"))

    # Score checking
    if score > high_score:
        high_score = score
        pen2.clear()
        pen2.write("High score:{}".format(high_score), align = "center", font = ("Impact", 15, "normal"))

    # Player with cars collisions
    if player.distance(car1) < 34:
        time.sleep(3)
        x = random.choice([-100, -30, 30, 100])
        lines_speed = 3.5
        car1.goto(x, 400)
        car2.goto(x, 700)
        car3.goto(x, 1000)
        score = 0
        pen.clear()
        pen.write("{}".format(score), align = "center", font = ("Impact", 40, "normal"))
        car_speed = 0.7
        truck_speed = 0.85\
    
    if player.distance(car2) < 34:
        time.sleep(3)
        x = random.choice([-100, -30, 30, 100])
        car2.goto(x, 400)
        car1.goto(x, 700)
        car3.goto(x, 1000)
        score = 0
        pen.clear()
        pen.write("{}".format(score), align = "center", font = ("Impact", 40, "normal"))
        car_speed = 0.7
        truck_speed = 0.85
        lines_speed = 3.5

    if player.distance(car3) < 39:
        time.sleep(3)
        x = random.choice([-100, -30, 30, 100])
        car3.goto(x, 1000)
        car2.goto(x, 400)
        car1.goto(x, 700)
        score = 0
        pen.clear()
        pen.write("{}".format(score), align = "center", font = ("Impact", 40, "normal"))
        car_speed = 0.7
        truck_speed = 0.85
        lines_speed = 3.5

    # Cars collisions
    if car1.distance(car3) < 60 and car3.xcor() == 100:
        car1.setx(30)
    elif car1.distance(car3) < 60 and car3.xcor() == 30:
        x = random.choice([-30, 100])
        car1.setx(x)
    elif car1.distance(car3) < 60 and car3.xcor() == -30:
        x = random.choice([-100, 30])
        car1.setx(x)    
    elif car1.distance(car3) < 60 and car3.xcor() == -100:
        car1.setx(-30)

    if car2.distance(car3) < 60 and car3.xcor() == 100:
        car2.setx(30)
    elif car2.distance(car3) < 60 and car3.xcor() == 30:
        x = random.choice([-30, 100])
        car2.setx(x)
    elif car2.distance(car3) < 60 and car3.xcor() == -30:
        x = random.choice([-100, 30])
        car2.setx(x)    
    elif car2.distance(car3) < 60 and car3.xcor() == -100:
        car2.setx(-30)