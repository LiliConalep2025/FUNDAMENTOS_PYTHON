file = open("EjemploArchivo.txt", "w") #Crear mi archivo y poder escribir en el
file.write("Este es el contenido del archivo.") #Escribir en el archivo este texto
file.close() #Liberar el recurso

lista = ["Fresa", "Mango", "Papaya"] #Creación de lista

with open("EjemploArchivo.txt", "a") as file: #Lo que escribo quiero que se agregue al final
    for e in lista:
        #With palabra reservada, estamos usando un contexto de uso de ese recurso
        file.write(e + "\n") #Cada elemento y salta una linea
print("Lista escrita en el archivo") #Manda mensaje al terminar de escribir la lista

lista2 =["Honda", "Suzuki", "BMW"]

with open("EjemploArchivo.txt", "a") as file:
    file.writelines(lista2)

print("Lista escrita con writelines.")

print("Imprimir todo el contenido del archivo.")
with open("EjemploArchivo.txt", "r") as file: #r solo lectura
    print(file.read()) #read para leer

print("Leer 2 lineas y posteriormente 5 caracteres.")
with open("EjemploArchivo.txt", "r") as file:
    print(file.readline()) #Leer una línea 
    print(file.readline()) #Lee la segunda línea
    print(file.readline(5)) #De la línea tres manda esa cantidad de caracteres

print("Almacenar el contenido en una lista y mostrar el último elemento")
with open("EjemploArchivo.txt", "r") as file:
    contenido=file.readlines() #En una lista y linea por linea
    print(contenido[-1])
    


