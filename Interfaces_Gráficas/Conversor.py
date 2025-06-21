from tkinter import *  # Para importar el paquete 
from tkinter import ttk

def calcular(*args): #Definimos una función calcular
    try: #Para 
        valor = float(pies.get()) #Convertir el valor de pies .get es metodo para obtener valor
        metros.set((0.3048 * valor * 10000.0 + 0.5) / 1000.0) #.set para establecer el valor y aqui es la operación
    except ValueError: #Valor invalido que no haga nada
        pass
#Inicia la aventana prinicipal raiz porque es como un arbol
raiz = Tk() #Objeto principal siempre sera Tk, la ventana que se va a crear
raiz.title("Pies a metros") #Para poner titulo a la ventana

marcoPrincipal = ttk.Frame(raiz, padding="3 3 12 12") #Witges tipo frame padding atributo que dice separacion de las orillas arriba, abajo, iz, derecha
marcoPrincipal.grid(column=0, row=0, sticky=(N, W, E, S)) #Grid en que columna y en que fila sticky a donde se va a mover 
marcoPrincipal.columnconfigure(0, weight=1) #Dsitribuidos de forma igual filas y columnas
marcoPrincipal.rowconfigure(0, weight=1)
#Variables
pies = StringVar() #Objeto que guarda cadena y lo convierte a flotante
metros = StringVar() #Mostra el resultado

txtPies = ttk.Entry(marcoPrincipal, width=7, textvariable=pies)#Objeto tipo Entry (caja de texto)
txtPies.grid(column=2, row=1, sticky=(W, E)) #En que columna y fila

ttk.Label(marcoPrincipal, textvariable=metros).grid(column=2, row=2, sticky=(W, E))
ttk.Button(marcoPrincipal, text="Calcular", command=calcular).grid(column=3, row=3, sticky=W) #Boton (Button) command es un comando

ttk.Label(marcoPrincipal, text="pies").grid(column=3, row=1, sticky=W) #Label es etiqueta
ttk.Label(marcoPrincipal, text="es equivalente a:").grid(column=1, row=2, sticky=E)
ttk.Label(marcoPrincipal, text="metros").grid(column=3, row=2, sticky=W)

for child in marcoPrincipal.winfo_children(): #Espacio del widgets hacia el contenido
    child.grid_configure(padx=5, pady=5)

txtPies.focus() #Dale el foco
raiz.bind('<Return>', calcular) #de la raiz agrega al presionar tecla enter (return)

raiz.mainloop() #Madamos llamar un hilo que permita su ejecución
