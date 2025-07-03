#IMPORTACIÓN DE MÓDULOS
from tkinter import *  #Interfaces gráficas
from tkinter import ttk #Para widgets
from tkinter import messagebox #Para enviar el mensaje de guardado al oprimir el boton guardar
import csv #Archivo CSV en Excel
   
#VENTANA PRINCIPAL
raiz = Tk() 
raiz.title("REGISTRO DE PERSONAS") 

#VARIABLES
Nombre = StringVar() #Para texto
Paterno = StringVar()
Materno = StringVar()
Email = StringVar()
Movil = StringVar()
Oficio = StringVar()
Estado = StringVar()
leervar = BooleanVar() #Para opciones marcadas
musicavar = BooleanVar()
videojuegosvar = BooleanVar()

 #FUNCIÓN PARA GUARDAR LOS DATOS
def Guardar(): #Valores de entrada
    nombre = Nombre.get()
    paterno = Paterno.get()
    materno = Materno.get()
    email = Email.get()
    movil = Movil.get()
    oficio = Oficio.get()
    estado = Estado.get()

    aficiones = [] #Crear una lista vacia para almacenar las aficiones seleccionadas
    if leervar.get(): #If para verificar la selección
        aficiones.append("Leer")
    if musicavar.get():
        aficiones.append("Música")
    if videojuegosvar.get():
        aficiones.append("Videojuegos")

    aficiones_str = ", ".join(aficiones) #Unir los elementos de la lista separados por comas
    messagebox.showinfo("Guardado", "Registro almacenado!!.") #Mensaje al guardar los datos

    #CREACIÓN DEL ARCHIVO EN CASO DE NO EXISTIR (Datos.csv)
    with open('Datos.csv', 'a', newline='', encoding='latin-1') as archivo_csv:
        escritor_csv = csv.writer(archivo_csv) #Se crea un objeto para poder escribir en CSV
        escritor_csv.writerow([nombre, paterno, materno, email, movil, oficio, estado, aficiones_str]) #Escribir una fila en el archivo

#FUNCION PARA CANCELAR EL LLENADO
def Cancelar():
    Nombre.set(" ")
    Paterno.set(" ")
    Materno.set(" ")
    Email.set(" ")
    Movil.set(" ")
    Oficio.set(" ")
    Estado.set("Querétaro")
    leervar.set(False)
    musicavar.set(False)
    videojuegosvar.set(False)
    
#FUNCION PARA MOSTRAR LOS DATOS EN UNA TABLA
def Mostrar():
    ventana_tabla = Toplevel(raiz) #Creación de una ventana 
    ventana_tabla.title("Registros guardados") #Titulo de la ventana
    ventana_tabla.geometry("900x300") #Tamaño de la ventana

    columnas = ("Nombre", "Paterno", "Materno", "Email", "Móvil", "Oficio", "Estado", "Aficiones") #Columnas
    tabla = ttk.Treeview(ventana_tabla, columns=columnas, show="headings") #Creación de una tabla dentro de la ventana

    for col in columnas: #Recorre cada columna
        tabla.heading(col, text=col) #Encabezado de cada columna para que muestre su nombre.
        tabla.column(col, width=100) #Ancho de cada columna

    try:
        with open('Datos.csv', 'r', newline='', encoding='latin-1') as archivo_csv: #Abrir el archivo en modo lectura
            lector_csv = csv.reader(archivo_csv) #Iteración sobre las filas del archivo.
            for fila in lector_csv: #Recorerr cada fila
                print("Leyendo fila:", fila)  #Imprime la fila actual
                if len(fila) == len(columnas): #Comprobar tamaño de fila=tamaño de columna
                    tabla.insert('', 'end', values=fila) #Para insertar
    except FileNotFoundError:
        messagebox.showwarning("Aviso", "No hay datos guardados aún.") #Sino hay archivo
    tabla.pack(fill='both', expand=True) #Empaquetar la tabla
    

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
mi_frame1.grid(column=1, row=4)
mi_frame1.grid_propagate(False) #PARA MANTENER EL TAMAÑO DEL FRAME


#FRAME OCUPACION
mi_frame2 = ttk.Frame(marcoPrincipal, width=100, height=100)
mi_frame2.grid(column=3, row=1)
mi_frame2.grid_propagate(False) #PARA MANTENER EL TAMAÑO DEL FRAME

#FRAME BOTONES
mi_frame3 = ttk.Frame(marcoPrincipal, width=300, height=50)
mi_frame3.grid(column=1, row=7)
mi_frame3.grid_propagate(False) #PARA MANTENER EL TAMAÑO DEL FRAME

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
comboEstados['values'] = ("Querétaro","Jalisco", "Nayarit", "Colima", "Michoacan", "Zacatecas", "Puebla", "Oaxaca",
"Aguascalientes", "Baja California", "Campeche", "Chiapas", "Chihuahua","Ciudad de México", "Coahuila","Durango",
"Guanajuato", "Guerrero", "Hidalgo","Morelos", "Nayarit", "Nuevo León", "Quintana Roo", "San Luis Potosí", "Sinaloa",
"Sonora", "Tabasco", "Tamaulipas", "Tlaxcala", "Veracruz","Yucatán" )
comboEstados.current(0) #Por default toma el primero de la lista para mostrar

#BOTONES
ttk.Button(mi_frame3, text="Guardar", command=Guardar).grid(column=1, row=8, sticky=W, padx=3, pady=3)
ttk.Button(mi_frame3, text="Cancelar", command=Cancelar).grid(column=2, row=8, sticky=W, padx=3, pady=3)
ttk.Button(mi_frame3, text="Mostrar", command=Mostrar).grid(column=3, row=8, sticky=W, padx=3, pady=3)

#RADIO BUTTON OFICIOS
Estudiante = ttk.Radiobutton(mi_frame2, text="Estudiante",variable = Oficio, value = "Estudiante")
Estudiante.grid(column=3, row=0, sticky=W)
Empleado = ttk.Radiobutton(mi_frame2, text="Empleado",variable = Oficio, value = "Empleado")
Empleado.grid(column=3, row=1, sticky=W)
Desempleado = ttk.Radiobutton(mi_frame2, text="Desempleado",variable = Oficio, value = "Desempleado")
Desempleado.grid(column=3, row=2, sticky=W)

#CHECKBUTTON AFICIONES
ttk.Label(mi_frame1, text="Aficiones:").grid(column=1, row=7, sticky=W) 
Leer = ttk.Checkbutton(mi_frame1, text="Leer", variable=leervar)
Leer.grid(column=1, row=8, sticky=W)
Musica = ttk.Checkbutton(mi_frame1, text="Música", variable=musicavar)
Musica.grid(column=2, row=8, sticky=W)
Videojuegos = ttk.Checkbutton(mi_frame1, text="Videojuegos", variable=videojuegosvar)
Videojuegos.grid(column=3, row=8, sticky=W)

raiz.mainloop() 
