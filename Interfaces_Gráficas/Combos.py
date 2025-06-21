from tkinter import *
from tkinter import ttk

raiz = Tk()
raiz.title("COMBOS") 

estado = StringVar()

comboEstados = ttk.Combobox(raiz, textvariable=estado)
comboEstados.grid()
comboEstados['values'] = ("Jalisco", "Nayarit", "Colima", "Michoacan")

raiz.mainloop()