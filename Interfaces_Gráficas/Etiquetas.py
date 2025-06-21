from tkinter import *
from tkinter import ttk

raiz = Tk()
raiz.title("ETIQUETAS") 
etqTexto = ttk.Label(raiz, text="Etiqueta solo texto")
etqTexto.grid()

imagen = PhotoImage(file="mariposa.png")

etqImagen = ttk.Label(raiz)
etqImagen.grid()
etqImagen['image'] = imagen

etqCombinada = ttk.Label(raiz, text="Etiqueta Combinada", compound="center")
etqCombinada.grid()
etqCombinada['image'] = imagen

raiz.mainloop()