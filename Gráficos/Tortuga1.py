import turtle
import time

turtle.forward(100) #avanza 100 pixeles para adelante
time.sleep(2)
turtle.right(90)
time.sleep(2) #Tiempo de espera para mirar
turtle.backward(50)
time.sleep(2)
turtle.left(90)
time.sleep(2)
turtle.circle(150)
time.sleep(2)
turtle.penup() #Como levantar mano de la hoja
turtle.setx(-100)
turtle.sety(-100)
turtle.pendown()
turtle.circle(50)
time.sleep(2)

done()