from tkinter import *  
from tkinter import ttk
   
#VENTANA PRINCIPAL
raiz = Tk() 
raiz.title("Inicio de sesión") 

marcoPrincipal = ttk.Frame(raiz, padding="15 15 15 15") 
marcoPrincipal.grid(column=0, row=0, sticky=(N, W, E, S)) 
marcoPrincipal.columnconfigure(0, weight=1) 
marcoPrincipal.rowconfigure(0, weight=1)
#VARIABLES
Usuario = StringVar()
Contrasena = StringVar()
#USUARIO
ttk.Label(marcoPrincipal, text="Usuario").grid(column=1, row=1, sticky=W) 
txtUsuario = ttk.Entry(marcoPrincipal, width=7, textvariable=Usuario)
txtUsuario.grid(column=2, row=1, sticky=(W, E)) 
#CONTRASEÑA
ttk.Label(marcoPrincipal, text="Contraseña").grid(column=1, row=2, sticky=E)
txtContrasena = ttk.Entry(marcoPrincipal, width=7, textvariable=Contrasena)
txtContrasena.grid(column=2, row=2, sticky=(W, E)) 
#BOTON
ttk.Button(marcoPrincipal, text="Ingresar").grid(column=2, row=3, sticky=W)
#Espacio del widgets hacia el contenido
for child in marcoPrincipal.winfo_children(): 
    child.grid_configure(padx=6, pady=6)

txtUsuario.focus() 

raiz.mainloop() 