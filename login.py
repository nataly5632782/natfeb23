from tkinter import *
from PIL import Image, ImageTk 

main = Tk()

path = Image.open("logo (1).png")
icono = ImageTk.PhotoImage(path)
main.iconphoto(True, icono)
main.title("Unitecnar")
main.geometry("1024x920")
main.resizable(True, True)
main.config(bg="azure2")

fr1 = Frame(main)
fr2 = Frame(main)

titulo = Label(fr2, text="Inicio Sesion", font=("Times New Roman", 25))
titulo.pack()

nombre = Label(fr2, text="Ingrese Nombre")
nombre.pack()
user = Entry(fr2)
user.pack()

clave = Label(fr2, text="Ingrese Clave")
clave.pack()
user1 = Entry(fr2)
user1.pack()

n2 = Label(fr1, text="Imagen", image=icono)
n2.pack()

def obtener():
    nombre = user.get()
    clave1 = user1.get()
    print(nombre, clave1)

boton = Button(fr2, text="ingresar", command=obtener)
boton.pack()

fr1.pack(side="left")
fr2.pack(side="right")

main.mainloop()
