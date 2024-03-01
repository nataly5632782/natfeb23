from libreria import libreria
print("hay 10 libros sus iD son del 1 al 10")
ciclo=True
while ciclo:
    opcion=int(input("ingrese el numero del libro: "))
    if opcion==1:
        p=libreria("La biblioteca de la medianoche","Matt Haig")
        print(p.obtenernombre())
    if opcion==2:
        p=libreria("El principe cruel","Holly Black")
        print(p.obtenernombre())
    if opcion==3:
        p=libreria("Boulervard","Flor salvador")
        print(p.obtenernombre())
    if opcion==4:
        p=libreria("¿Qué paso con jeisson?","anonimo")
        print(p.obtenernombre())
    if opcion==5:
        p=libreria("silence","Flor salvador")
        print(p.obtenernombre())
    if opcion==6:
        p=libreria("A dos metros de tí","Tobias laconis")
        print(p.obtenernombre())
    if opcion==7:
        p=libreria("El tunel","Ernesto Sabato")
        print(p.obtenernombre())
    if opcion==8:
        p=libreria("Cuando no queden más estrellas que contar ","María martinez")
        print(p.obtenernombre())
    if opcion==9:
        p=libreria("Fabricante de lagrimas","Erin Doom")
        print(p.obtenernombre())
    if opcion==10:
        p=libreria("El color de las cosas invisibles","Andrea Longarela")
        print(p.obtenernombre()) 
    if opcion==11:
        ciclo=False
 