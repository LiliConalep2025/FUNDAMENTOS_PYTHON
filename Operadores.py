def nuevo_tema(tema:str):
    print(f"\n----- {tema} -----\n")

if __name__ == "__main__":

    nuevo_tema("Operadores Aritmeticos")
    #nuevoTema(100) enviar un numero es ves de caracteres
    #print("-----Operadores Aritmeticos-----") Era el titulo inicial, pero se realizo la función 

    print("Operador suma, 5 + 6=",5 + 6)
    print("Operador resta, 10 - 3=",10 - 3)
    print("Operador multiplicación, 5 * 8=",5 * 8)
    print("Operador division, 9 / 3=",9 / 3)
    print("Operdaor division entera, 14 // 5=",14 // 5)
    print("Operador modulo, 26 % 3=",26 % 3)
    print("Operador cambio de signo, -3=",-3)
    print("Operador de exponenciacion, 8 ** 2=",8 ** 2)
    print("Operador identidad + 9=",+ 9)

    nuevo_tema("Operadores lógicos")
    print("-----Operador and-----")
    print("True and True:", True and True)
    print("True and False:", True and False)
    print("False and True:", False and True)
    print("False and False:", False and False)

    print("-----Operador or-----")
    print("True or True:", True or True)
    print("True or False:", True or False)
    print("False or True:", False or True)
    print("False or False:", False or False)

    print("-----operador not-----")
    print("not False:", not False)
    print("not True:", not True)

    nuevo_tema("Operadores de comparación")
    print("5==7:", 5==7)
    print("8!=4:", 8!=4)
    print("5<4:", 5<4)
    print("3<=4:", 3<=4)
    print("15>12:", 15>12)
    print("10>=15:", 10>=15)

    nuevo_tema("Variables")
    variable1 = 10
    _variable2 = 6.2547
    Variable3="Pepe"
    nombreVariable = 8 #Es el estilo que usa C++ (Joroba)
    nombre_variable = 34.2 #Es el estilo que usaremos en Python (Serpiente) tanto variables como funciones
    print(variable1, _variable2, Variable3, nombreVariable, nombre_variable)

    a, b, c = 5, 10.0, "Hola"
    print(a)
    print(b)
    print(c)

    #Ejemplo de variable dinámica
    nombre_variable ="Adios" #Arriba tiene aignado un flotante, y aqui un caracter
    print(nombre_variable)

    nuevo_tema("Enteros")
    w = 105
    x = 12345678987654321
    y = -58
    z = 0b00110011 #Prefijo 0b indica que es binario
    h = 0xFF #Para numero hexadecimal

    
    print(w, type(w)) #Imprimir y preguntarle que tipo de dato es
    print(x, type(x))
    print(y, type(y))
    print(z, type(z))
    print(h, type(h))

    nuevo_tema("Flotantes")
    x = 1234.56
    print(x, type(x))
    y = -0.2584
    print(y, type(y))

    nuevo_tema("Numeros Complejos")
    x = .46j
    y = 12 + 45j
    z = 2j
    c = y + z
    print(x, type(x))
    print(y, type(y))
    print(z, type(z))
    print(c, type(c))

    nuevo_tema("Booleanos")
    x = True
    print(x, type(x))

    nuevo_tema("Lista")
    lista = [10, 20.5, "Lista de Python"]
    print(lista)
    print(lista[1]) #Para imprimir un dato de la lista por indice   
    lista[0] ="Hola" 
    lista.append(34) #Agregar un valor al final de la lista
    print(lista)
    lista.insert(0, 1.1) #Agregar un valor en la parte inicial de la lista
    print(lista)
    lista.append([3, 4, 5, 6, 7, 8]) #Agregar una lista dentro de la lista
    print(lista)
    print(lista[5])
    print(lista[5][4]) #Posición 5 se agrega el 4
    print(lista[3][4]) #Posición 3 se agrega el 4

    nuevo_tema ("Tuplas") #Son inmutables y tampoco se le pueden agregar mas elementos
    tupla = (25, "Tupla", 1 + 10j)
    print(tupla)
    print(tupla[1])
    #tupla[0] = 0 no es permitido porque no permite modificaciones
    #print(tupla)
    tupla = (20, "Tupla", 1 + 10j, "Otro") #Se crea otro espacio de memoria
    print(tupla)

    nuevo_tema("Conjuntos")
    conjunto = {10, 20, 30, 40, 50, 20} #Omite el valor repetido
    print(conjunto)
    #print(conjunto[1]) no permitido porque no esta indexado
    conjunto.add(80) #Agregar un valor
    print(conjunto)
    print(50 in conjunto) #Buscar un valor en el conjunto

    nuevo_tema("Diccionarios")
    diccionario = {"Nombre": "Lili",
                    "Edad": 40,
                    "Teléfono": 1254789364,
                    90 : 4 + 3j}
    print(diccionario)
    print(diccionario["Nombre"])
    print(diccionario[90])

    nuevo_tema("Cadenas")
    cadena1 = "Esto es una cadena"
    cadena2 = 'Esto es una cadena'
    cadena_multilinea = '''Esto es una
    cadena de variaas lineas  con tabuladores y
    saltos de linea '''
    print(cadena1, type(cadena1))
    print(cadena2, type(cadena2))
    print(cadena_multilinea, type(cadena_multilinea))

    cadena3 = "Hola" * 5 #Imprime la cadena cinco veces
    print(cadena3)
    print(cadena1[2])
    print(cadena1[2:10])
    print(cadena1[:5])
    print(cadena1[5:]) #Posicion 5 hasta el final
    print(cadena1[:-5]) #Al final quitale cinco y recorrerla
    print(cadena1[5:-5])
    print(cadena1[::-1]) #Imprime al reves
