from Operadores import nuevo_tema #Para importara la función que esta en el modulo Operadores.py
import Calc.operaciones as c #Importa del paquete Calc el módulo operaciones

if __name__ == "__main__": #Definir el main
    nuevo_tema ("Módulos y paquetes")

    print(c.resta(6, 1))
    print(c.suma(2, 3, 4))
    print(c.mult(5, 6))
    print(c.div(11, 2.5))

