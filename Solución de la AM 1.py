import turtle

n1 = int(input('Ingresa el número de lados del polígono : '))
l1 = int(input('Ingresa la longitud de los lados del polígono : '))

def draw_polygon(n,l):
    for _ in range(n):
        turtle.forward(l)
        turtle.right(360 / n)

draw_polygon(n1, l1)

n2 = int(input('Ingresa el número de lados del polígono : '))
l2 = int(input('Ingresa la longitud de los lados del polígono : '))

turtle.penup()
turtle.goto(80, 40)
turtle.pendown()

draw_polygon(n2, l2)
