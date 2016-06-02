#ejercicio uno
#Hola mundo con botones

from tkinter import *
app= Tk()
app.title("Aplicacion grafica en Python")
etiqueta = Label(app, text="Hola Mundo!!!")
boton = Button(app, text="OK!!!")

etiqueta.pack()
boton.pack()
app.mainloop()