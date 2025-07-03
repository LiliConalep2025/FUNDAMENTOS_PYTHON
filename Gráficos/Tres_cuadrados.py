import turtle
import time

#Cuadrado 1
turtle.penup() #Levantar la mano
turtle.goto(0, 0) #Mover al punto 0,0
turtle.setheading(-20) #Girar a -20 grados
turtle.pendown() #Bajar la mano
turtle.forward(100) #Avanzar
turtle.left(90) #Girar 90
time.sleep(1) #Tiempo de espera
turtle.forward(100)
turtle.left(90)
time.sleep(1)
turtle.forward(100)
turtle.left(90)
time.sleep(1)
turtle.forward(100)


#Cuadrado 2
turtle.penup()
turtle.goto(0, 0)
turtle.setheading(0)
turtle.pendown()
turtle.forward(100)
turtle.left(90)
time.sleep(1)
turtle.forward(100)
turtle.left(90)
time.sleep(1)
turtle.forward(100)
turtle.left(90)
time.sleep(1)
turtle.forward(100)


#Cuadrado 3
turtle.penup()
turtle.goto(0, 0)
turtle.setheading(20)
turtle.pendown()
turtle.forward(100)
turtle.left(90)
time.sleep(1)
turtle.forward(100)
turtle.left(90)
time.sleep(1)
turtle.forward(100)
turtle.left(90)
time.sleep(1)
turtle.forward(100)


turtle.done()