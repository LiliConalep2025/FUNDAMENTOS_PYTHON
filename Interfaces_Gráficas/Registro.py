from tkinter import *  
from tkinter import ttk
import csv
   
#VENTANA PRINCIPAL
raiz = Tk() 
raiz.title("REGISTRO") 

#VARIABLES
Nombre = StringVar()
Paterno = StringVar()
Materno = StringVar()
Email = StringVar()
Movil = StringVar()
Oficio = StringVar()
Estado = StringVar()
Aficiones = StringVar()

 #FUNCIÓN PARA GUARDAR LOS DATOS
def Guardar():
    nombre = Nombre.get()
    paterno = Paterno.get()
    materno = Materno.get()
    email = Email.get()
    movil = Movil.get()
    oficio = Oficio.get()
    estado = Estado.get()
    aficiones = Aficiones.get()

#CREACIÓN DEL ARCHIVO EN CASO DE NO EXISTIR (Datos.csv)
    with open('Datos.csv', 'a') as archivo_csv: #a para insertar al final en el archivo
        escritor_csv = csv.writer(archivo_csv) #Se crea un objeto para poder escribir en CSV
        escritor_csv.writerow([nombre, paterno, materno, email, movil, oficio, estado, aficiones]) #Escribir una fila en el archivo

#FUNCION PARA CANCELAR EL LLENADO
def Cancelar():
    Nombre.set(" ")
    Paterno.set(" ")
    Materno.set(" ")
    Email.set(" ")
    Movil.set(" ")
    Oficio.set(" ")
    Estado.set("Querétaro")
    Aficiones.set(" ")



#VENTANA PRINCIPAL
marcoPrincipal = ttk.Frame(raiz, padding="10 10 10 10") 
marcoPrincipal.grid(column=0, row=0, sticky=(N, W, E, S)) 
marcoPrincipal.columnconfigure(0, weight=1) 
marcoPrincipal.rowconfigure(0, weight=1)


#FRAME INFORMACIÓN 
mi_frame = ttk.Frame(marcoPrincipal, width=250, height=180, relief="groove", borderwidth=3)
mi_frame.grid(column=1, row=1)
mi_frame.grid_propagate(False) #PARA MANTENER EL TAMAÑO DEL FRAME

#FRAME AFICIONES
mi_frame1 = ttk.Frame(marcoPrincipal, width=250, height=90, relief="groove", borderwidth=3)
mi_frame1.grid(column=1, row=3)
mi_frame1.grid_propagate(False) #PARA MANTENER EL TAMAÑO DEL FRAME

#ETIQUETAS Y CAJAS DE  TEXTO
ttk.Label(mi_frame, text="Nombre:").grid(column=1, row=2, sticky=W) 
txtNombre = ttk.Entry(mi_frame, width=25, textvariable=Nombre)
txtNombre.grid(column=2, row=2, sticky=(W, E), padx=5, pady=5) 


ttk.Label(mi_frame, text="Paterno:").grid(column=1, row=3, sticky=W) 
txtPaterno = ttk.Entry(mi_frame, width=25, textvariable=Paterno)
txtPaterno.grid(column=2, row=3, sticky=(W, E), padx=5, pady=5) 

ttk.Label(mi_frame, text="Materno:").grid(column=1, row=4, sticky=W) 
txtMaterno = ttk.Entry(mi_frame, width=25, textvariable=Materno)
txtMaterno.grid(column=2, row=4, sticky=(W, E), padx=5, pady=5) 

ttk.Label(mi_frame, text="Email:").grid(column=1, row=5, sticky=W) 
txtEmail = ttk.Entry(mi_frame, width=25, textvariable=Email)
txtEmail.grid(column=2, row=5, sticky=(W, E), padx=5, pady=5) 

ttk.Label(mi_frame, text="Móvil:").grid(column=1, row=6, sticky=W) 
txtMovil = ttk.Entry(mi_frame, width=25, textvariable=Movil)
txtMovil.grid(column=2, row=6, sticky=(W, E), padx=5, pady=5) 

#COMBO DE ESTADOS
comboEstados = ttk.Combobox(marcoPrincipal, textvariable=Estado)
comboEstados.grid(column=3, row=3, sticky=W, padx=5, pady=5)
comboEstados['values'] = ("Querétaro","Jalisco", "Nayarit", "Colima", "Michoacan", "Zacatecas", "Puebla", "Oaxaca")
comboEstados.current(0) #Por default toma el primero de la lista para mostrar

#BOTONES
ttk.Button(marcoPrincipal, text="Guardar", command=Guardar).grid(column=1, row=8, sticky=W, padx=3, pady=3)
ttk.Button(marcoPrincipal, text="Cancelar", command=Cancelar).grid(column=2, row=8, sticky=W, padx=3, pady=3)

#RADIO BUTTON OFICIOS
Estudiante = ttk.Radiobutton(marcoPrincipal, text="Estudiante",variable = Oficio, value = "Estudiante")
Estudiante.grid(column=3, row=0, sticky=W)
Empleado = ttk.Radiobutton(marcoPrincipal, text="Empleado",variable = Oficio, value = "Empleado")
Empleado.grid(column=3, row=1, sticky=W)
Desempleado = ttk.Radiobutton(marcoPrincipal, text="Desempleado",variable = Oficio, value = "Desempleado")
Desempleado.grid(column=3, row=2, sticky=W)

#RADIO BUTTON AFICIONES
ttk.Label(mi_frame1, text="Aficiones:").grid(column=1, row=7, sticky=W) 
Leer = ttk.Radiobutton(mi_frame1, text="Leer",variable = Aficiones, value = "Leer")
Leer.grid(column=1, row=8, sticky=W)
Musica = ttk.Radiobutton(mi_frame1, text="Música",variable = Aficiones, value = "Musica")
Musica.grid(column=2, row=8, sticky=W)
Videojuegos = ttk.Radiobutton(mi_frame1, text="Videojuegos",variable = Aficiones, value = "Videojuegos")
Videojuegos.grid(column=3, row=8, sticky=W)


raiz.mainloop() 
