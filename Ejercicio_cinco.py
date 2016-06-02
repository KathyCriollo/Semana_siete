#Ejercicio cinco
# -*- coding: utf-8 -*-
 
  
from tkinter import * # Importamos el modulo Tkinter
  
  
def DrawList(): # Creamos una lista con algunos nombres
        plist = ['Uno','Dos','Tres']
  
        for item in plist: # Insertamos los items en un Listbox
                listbox.insert(END,item);
                  
          
root = Tk()                     # Creamos una ventana de fondo
  
listbox = Listbox(root)
boton = Button(root,text = "Presionar",command = DrawList)
  
boton.pack()
listbox.pack()   # Hacemos los pack() del boton y el Listbox
root.mainloop()  # Entramos en el loop