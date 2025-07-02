import turtle
import time

#Triangulo
turtle.forward(100)
time.sleep(2)
turtle.left(120)
time.sleep(2)
turtle.forward(100)
time.sleep(2)
turtle.left(120)
time.sleep(2)
turtle.forward(100)
time.sleep(2)

#Cuadrado
turtle.penup() #Como levantar mano de la hoja
turtle.setx(150)
turtle.sety(150)
turtle.pendown()
turtle.left(120)
time.sleep(2)
turtle.forward(100)
time.sleep(2)
turtle.left(90)
time.sleep(2)
turtle.forward(100)
time.sleep(2)
turtle.left(90)
time.sleep(2)
turtle.forward(100)
time.sleep(2)
turtle.left(90)
time.sleep(2)
turtle.forward(100)
time.sleep(2)

#Pentágono

turtle.penup() #Como levantar mano de la hoja
turtle.setx(-150)
turtle.sety(-150)
turtle.setheading(0) #Reiniciar dirección
turtle.pendown()

turtle.forward(80)
time.sleep(2)
turtle.left(72)
time.sleep(2)
turtle.forward(80)
time.sleep(2)
turtle.left(72)
time.sleep(2)
turtle.forward(80)
time.sleep(2)
turtle.left(72)
time.sleep(2)
turtle.forward(80)
time.sleep(2)
turtle.left(72)
time.sleep(2)
turtle.forward(80)
time.sleep(2)

done()
