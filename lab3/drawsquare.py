import turtle

def Drawsquare(sidelength):
    turtle.forward(sidelength)
    turtle.left(90)
    turtle.forward(sidelength)
    turtle.left(90)
    turtle.forward(sidelength)
    turtle.left(90)
    turtle.forward(sidelength)

def main():
    count = 0
    while count < 10:
        Drawsquare(sidelength)
        turtle.left(36)
        count += 1

if __name__ == '__main__':
    turtle.showturtle()
    sidelength = turtle.numinput('','Enter a number: ')
    sidelength = int(sidelength)
    main()
