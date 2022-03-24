from cgitb import text
import tkinter

ventana = tkinter.Tk()
ventana.geometry("800x500")

cajatexto = tkinter.Entry(ventana, font="Corbel")

cajatexto.pack()

etiqueta = tkinter.Label(ventana)
etiqueta.pack()

def textoCajadeTexto():
    textoA = cajatexto.get()
    print(textoA)
    etiqueta["text"] = textoA

boton=tkinter.Button(ventana, text="click", command = textoCajadeTexto)
boton.pack()

cajatexto.pack()

ventana.mainloop()