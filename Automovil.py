class Automovil: #crear clase viene siendo una plantilla
    def __init__(self, marca, color):#Atributos, el primer atributo siempre self
        #Definir atributos de la clase
        #Son los que empiezan con "self"
        self.marca = marca
        self.color = color

    def avanzar(self): #metodos llevan "self" para acceder a los atributos
        print(f"El coche avanza y es un: {self.marca}")

    def retroceder(self):
        print(f"El coche retrocede y es de color: {self.color}")
#Crear objetos
if __name__ == "__main__":
    auto = Automovil("BMW", "Azul")
    auto.avanzar() #.Acceder a metodos y atributos de los objetos
    auto.retroceder()

    auto1 = Automovil("Honda", "Gris")
    auto1.retroceder()
    auto1.avanzar()
