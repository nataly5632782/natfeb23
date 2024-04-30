from tkinter  import *
from tkinter import messagebox

ventana= Tk()
def n12():
    n14=n6.curselection()
    for i in n14:
        n15=n6.get(i)
    n17 = Genero.get()
    if n17 == 1:
       
       n18="Hombre"
    elif n17 == 2:
        n18="Mujer"
    messagebox.showinfo("Datos",message=f"nombre: {nombre.get()}\napellido:{Apellido.get()}\nedad:{Edad.get()}\ntelefono:{telefono.get()}\nciudad:{n15}\ngenero:{n18}")

ventana.geometry("800x700")
ventana.title("Tecnar app")
ventana.resizable(True, True)
ventana.config(bg="purple")

n= Label(ventana,text="BIENVENIDO A UNITECNAR :)",bg="black",fg="white", font=("time roman",20 ))
n0=Label(ventana, text="Ingrese sus datos",bg="white",fg="black", font=("time roman", 10))
n1=Label(ventana,text="Nombre",bg="white")
n2=Label(ventana,text="Apellido",bg="white")
n3=Label(ventana,text="edad",bg="white",padx=10)
n4=Label(ventana,text="telefono",bg="white")
n5= Label(ventana,text="CIUDAD",bg="black",fg="white", font=("time roman",10 ))
n7= Label(ventana,text="GENERO",bg="black",fg="white", font=("time roman",10 ))



n.grid(row=0, column=0, padx=100,sticky=W, pady=2)
n0.grid(row=1, column=0,padx=100, sticky=W, pady=2)
n1.grid(row=2, column=0,padx=100, sticky=W, pady=2)
n2.grid(row=3, column=0,padx=100, sticky=W, pady=2)
n3.grid(row=4, column=0,padx=100, sticky=W, pady=2)
n4.grid(row=5, column=0,padx=100,sticky=W, pady=2)

nombre=Entry(ventana)
Apellido=Entry(ventana)
Edad=Entry(ventana)
telefono=Entry(ventana)

nombre.grid(row=2, column=0, sticky=W,padx=150, pady=2)
Apellido.grid(row=3, column=0, sticky=W,padx=150, pady=2)
Edad.grid(row=4, column=0, sticky=W,padx=150, pady=2)
telefono.grid(row=5, column=0,sticky=W, padx=150, pady=2)

n5.grid(row=6, column=0,padx=200,sticky=W, pady=2)
n6=Listbox(ventana,width=30,height=5,selectmode="single")
n6.grid(row=7, column=0, sticky=W,padx=150, pady=2)

ciudades= ["Cali", "Cartagena", "Barranquilla", "Medellin",]
for ciudad in ciudades:
    n6.insert(END, ciudad)

n7.grid(row=8, column=0,padx=200,sticky=W, pady=2)
Genero= IntVar()
n8 = Radiobutton(ventana, text="Hombre", variable=Genero, value=1)
n9 = Radiobutton(ventana, text="Mujer", variable=Genero, value=2)

n8.grid(row=10, column=0,padx=200,sticky=W, pady=2)
n9.grid(row=9, column=0,padx=200,sticky=W, pady=2)

n10=Button(ventana,text="Registrar datos",command=n12)
n10.grid(row=11, column=0,padx=200,sticky=W, pady=2)

mainloop()