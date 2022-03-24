from cgitb import text
import tkinter

ventana = tkinter.Tk()
ventana.geometry("800x500")

boton1 = tkinter.Button(ventana,  text="Boton1")
boton2 = tkinter.Button(ventana,  text="Boton2")
boton3 = tkinter.Button(ventana,  text="Boton3")

boton1.grid(row=5,column=5)
boton1.grid(row=5,column=7)
boton1.grid(row=5,column=9)

ventana.mainloop()