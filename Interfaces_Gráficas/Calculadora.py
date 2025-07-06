from tkinter import *
from tkinter import ttk

raiz = Tk()
raiz.title("CALCULADORA") 

#VARIABLES
resultado = StringVar()

#FUNCIÓN PARA LOS NUMEROS
def agregar_numero(num):
    actual = resultado.get()
    resultado.set(actual + str(num))

marcoPrincipal = ttk.Frame(raiz, padding="10 10 10 10") 
marcoPrincipal.grid(column=0, row=0, sticky=(N, W, E, S)) 
marcoPrincipal.columnconfigure(0, weight=1) 
marcoPrincipal.rowconfigure(0, weight=1)

#FUNCIÓN LIMPIAR
def limpiar():
    resultado.set("")

#FUNCIÓN RESULTADO
def calcular_resultado():
    try:
        resultado.set(str(eval(resultado.get())))
    except:
        resultado.set("Error")

#FRAME INFORMACIÓN 
mi_frame = ttk.Frame(marcoPrincipal, width=350, height=250, relief="groove", borderwidth=3)
mi_frame.grid(column=1, row=1)
mi_frame.grid_propagate(False) #PARA MANTENER EL TAMAÑO DEL FRAME

#BOTONES
ttk.Button(mi_frame, text="7", command=lambda: agregar_numero(7)).grid(column=1, row=3, sticky=W, padx=2, pady=2)
ttk.Button(mi_frame, text="8", command=lambda: agregar_numero(8)).grid(column=2, row=3, sticky=W, padx=2, pady=2)
ttk.Button(mi_frame, text="9", command=lambda: agregar_numero(9)).grid(column=3, row=3, sticky=W, padx=2, pady=2)
ttk.Button(mi_frame, text="/", command=lambda: agregar_numero('/')).grid(column=4, row=3, sticky=W, padx=2, pady=2)

ttk.Button(mi_frame, text="4", command=lambda: agregar_numero(4)).grid(column=1, row=4, sticky=W, padx=2, pady=2)
ttk.Button(mi_frame, text="5", command=lambda: agregar_numero(5)).grid(column=2, row=4, sticky=W, padx=2, pady=2)
ttk.Button(mi_frame, text="6", command=lambda: agregar_numero(6)).grid(column=3, row=4, sticky=W, padx=2, pady=2)
ttk.Button(mi_frame, text="*", command=lambda: agregar_numero('*')).grid(column=4, row=4, sticky=W, padx=2, pady=2)

ttk.Button(mi_frame, text="1", command=lambda: agregar_numero(1)).grid(column=1, row=5, sticky=W, padx=2, pady=2)
ttk.Button(mi_frame, text="2", command=lambda: agregar_numero(2)).grid(column=2, row=5, sticky=W, padx=2, pady=2)
ttk.Button(mi_frame, text="3", command=lambda: agregar_numero(3)).grid(column=3, row=5, sticky=W, padx=2, pady=2)
ttk.Button(mi_frame, text="-", command=lambda: agregar_numero('-')).grid(column=4, row=5, sticky=W, padx=2, pady=2)

ttk.Button(mi_frame, text="0", command=lambda: agregar_numero(0)).grid(column=1, row=6, sticky=W, padx=2, pady=2)
ttk.Button(mi_frame, text=".", command=lambda: agregar_numero('.')).grid(column=2, row=6, sticky=W, padx=2, pady=2)
ttk.Button(mi_frame, text="=", command=lambda: calcular_resultado()).grid(column=3, row=6, sticky=W, padx=2, pady=2)
ttk.Button(mi_frame, text="+", command=lambda: agregar_numero('+')).grid(column=4, row=6, sticky=W, padx=2, pady=2)
ttk.Button(mi_frame, text="C", command=limpiar).grid(column=1, row=2, columnspan=4, sticky="we", padx=2, pady=2)

#ETIQUETAS
ttk.Label(mi_frame,textvariable=resultado,font=("Arial", 16),background="white", relief="sunken",anchor="e",padding=5).grid(column=1, row=1, columnspan=3, pady=5, sticky="we")
raiz.mainloop()