import turtle
import random

def main():
    steps = 20
    limit = 100
    boundary = (-(limit) < turtle.xcor() < limit) and (-(limit) < turtle.ycor() < limit)
    count = 0
    while boundary:
        number = random.randint(1,4)
        if number == 1:
            turtle.left(0)
        elif number == 2:
            turtle.left(90)
        elif number == 3:
            turtle.left(180)
        else:
            turtle.left(270)
        turtle.forward(steps)
        boundary = (-100.0 < turtle.xcor() < 100.0) and (-100.0 < turtle.ycor() < 100.0)
        count += 1
    turtle.penup()
    turtle.goto(0, 0)
    turtle.pendown()
    turtle.write(count * steps, font = ("Arial", 16, "normal"))

if __name__ == "__main__":
    turtle.showturtle()
    main()
