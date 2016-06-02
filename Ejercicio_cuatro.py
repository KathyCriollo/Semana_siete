#Ejercicio Cuatro
# -*- coding: utf-8 -*-
  
from tkinter import *           # Importamos el módulo Tkinter
root = Tk()                     # Creamos la ventana de fondo
                                # Creamos una lista con nombres
li = 'primer elemento segundo'.split()
listb = Listbox(root)           # Creamos un Widgets Listbox
for item in li:                 # Insertamos los nombres de la lista en el Listbox
    listb.insert(0,item)
  
listb.pack()                    # Hacemos el pack del widget
root.mainloop()