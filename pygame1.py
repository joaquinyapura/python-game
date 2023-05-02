import turtle


wn = turtle.Screen()
wn.title("PONG")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)


# puntos
score_a = 0
score_b = 0


# palo A
paddlea_ = turtle.Turtle()
paddlea_.speed(0)
paddlea_.shape("square")
paddlea_.color("white")
paddlea_.shapesize(stretch_wid=5, stretch_len=1)
paddlea_.penup()
paddlea_.goto(-350, 0)


# palo B

paddleb_ = turtle.Turtle()
paddleb_.speed(0)
paddleb_.shape("square")
paddleb_.color("white")
paddleb_.shapesize(stretch_wid=5, stretch_len=1)
paddleb_.penup()
paddleb_.goto(350, 0)


# pelota

ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.3
ball.dy = -0.3


# Marcador
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Jugador 1: 0  Jugador 2: 0", align="center",
          font=("Courier", 24, "normal"))


# funciones de movimientoA

def paddle_a_arriba():
    y = paddlea_.ycor()
    y += 50
    paddlea_.sety(y)


def paddle_a_abajo():
    y = paddlea_.ycor()
    y -= 50
    paddlea_.sety(y)


# funciones de movimiento B
def paddleb_arriba():
    y = paddleb_.ycor()
    y += 50
    paddleb_.sety(y)


def paddleb_abajo():
    y = paddleb_.ycor()
    y -= 50
    paddleb_.sety(y)


# config de teclado 
wn.listen()
wn.onkeypress(paddle_a_arriba, "w")
wn.onkeypress(paddle_a_abajo, "s")

wn.onkeypress(paddleb_arriba, "Up")
wn.onkeypress(paddleb_abajo, "Down")


# maingameloop

while True:
    wn.update()

    # move the ball
    ball.setx(ball.xcor()+ball.dx)
    ball.sety(ball.ycor()+ball.dy)

    # borde
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 390:
        score_a += 1
        pen.clear()
        pen.write("Jugador 1: {}  Jugador 2: {}".format(score_a, score_b),
                  align="center", font=("Courier", 24, "normal"))
        ball.goto(0, 0)
        ball.dx *= -1

    if ball.xcor() < -390:
        score_b += 1
        pen.clear()
        pen.write("Jugador 1: {}  Jugador 2: {}".format(score_a, score_b),
                  align="center", font=("Courier", 24, "normal"))
        ball.goto(0, 0)
        ball.dx *= -1

    # COLISIONES
    if ball.xcor() > 340 and (ball.ycor() < paddleb_.ycor()+50 and ball.ycor() > paddleb_.ycor()-50):
        ball.setx(340)
        ball.dx *= -1

    if ball.xcor() < -340 and (ball.ycor() < paddlea_.ycor()+50 and ball.ycor() > paddlea_.ycor()-50):
        ball.setx(-340)
        ball.dx *= -1
