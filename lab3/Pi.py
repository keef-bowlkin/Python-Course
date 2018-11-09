import turtle, random, math


def main():
    limit = 1
    scale = 150
    iterations = 5000
    sidelength = scale * 2
    count = 0
    radius = limit * scale
#    print(area)
    turtle.tracer(0)
    turtle.setworldcoordinates(-(scale), -(scale), (scale), (scale))
    turtle.hideturtle()

    turtle.penup()
    turtle.goto(0, -(scale))
    turtle.pendown()
    turtle.circle(radius)

    turtle.penup()
    turtle.goto(-(scale), -(scale))
    turtle.pendown()
    turtle.forward(sidelength)
    turtle.left(90)
    turtle.forward(sidelength)
    turtle.left(90)
    turtle.forward(sidelength)
    turtle.left(90)
    turtle.forward(sidelength)
    turtle.left(90)

    bullseye = 0
    while(count <= (iterations)):
        turtle.penup()
        turtle.goto((random.randint(-(scale), (scale))), (random.randint(-(scale), (scale))))
        turtle.pendown()
#        turtle.position()
#        print(turtle.position())
        if math.sqrt(turtle.xcor()**2 + turtle.ycor()**2) <= radius:
            turtle.dot(5,"green")
            bullseye += 1
        else:
            turtle.dot(5,"red")
        count += 1
    turtle.update()
    pi = 4 * bullseye/iterations
    print(pi)


if __name__ == "__main__":
    main()
