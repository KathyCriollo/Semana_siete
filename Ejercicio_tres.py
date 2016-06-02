#Ejercicio tres
#-*- coding:utf-8 -*-
from tkinter import *

def Call(): # se define la función
        lab= Label(root, text ='Usted presiono\n el boton')
        lab.pack()

root = Tk
root.geometry('100x100+350+70')
boton = Button(root,text= 'Presionar', command = Call)
boton.pack()
root.mainloop()