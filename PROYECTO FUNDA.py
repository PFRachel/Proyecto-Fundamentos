#PROYECTO FUNDAMENTOS#
"''////////////////////////////////////////////////////////////////////////////////"""
import tkinter #Realizar la interfaz
from tkinter import * # se importa alguna documentación de la biblioteca
import pygame # biblioteca para el sonido
import tkinter as tk # facilidad de usar
import os # para entrar a los archivos
import threading # biblioteca para hacer hilos(ejecutar varias funciones al mismo tiempo)
from PIL import Image, ImageTk

#import RPi.GPIO as GPIO
pygame.init() # esto es para que pygame inicie y funcione

"__________________SONIDO DE FONDO____________"



"__________FUNCION CARGAR IMAGENES_______________________"
def cargarImagen(nombre): # funcion cargar imagenes 
    ruta = os.path.join('Imagenes', nombre)  # Carpeta de imágenes
    imagen = PhotoImage(file=ruta) # ruta de las imagenes 
    return imagen # mostramos la imagen
"_______________________________________________"

###################################################################
###################################################################
"_______________VENTANA PRINCIPAL (INICIO)_________________________"
###################################################################

def Vprincipal(): # funcion para la primer ventana de entrada
    principal = Tk() # se crea la ventana
    principal.title("Game World") # se crea un nombre visible al lado izquierdo superior
    principal.geometry("1000x900")  # tamaño de la ventana creada

    "__________CARGAR  IMAGEN DE FONDO__________________________"
    fondo = cargarImagen("fondoP.png") #se pone para que acepte la imagen
    imagen = tkinter.Label(principal,image = fondo) #le decimos  que lo ponga de pantalla
    imagen.place(x=0,y=0) # ubicacion  de la  imagen de fondo
    imagen.pack() # para que funcione

    canvas = Canvas(principal, width=1000, height=900)
    canvas.pack()

    def pause_button_clicked():
        if pygame.mixer.music.get_busy():
            pygame.mixer.music.pause()
            canvas.itemconfig(pause_button, image=Pause_image)
        else:

            pygame.mixer.music.unpause()

            canvas.itemconfig(pause_button, image=Sound_image)

    Sound_image = cargarImagen("Sound.png")
    Pause_image = cargarImagen("Sound.png")

    pause_button = Button(principal, image=Sound_image, command=pause_button_clicked)
    pause_button.place(x=950, y=850)

    # Initialize pygame mixer music
    pygame.mixer.init()
    pygame.mixer.music.load("Song.mp3")
    pygame.mixer.music.play(-1)


    "__________________TITULO_________________________"
    titulo =Label(principal,text="MINI- \nFUTBOLIN", bg="sky blue",fg="black", font =("Rockwell Extra Bold",92))#Nombre de juego muy llamativo
    titulo.place(x=6,y=5) # ubicacion del nombre del juego
    "___________________BOTONES______________________"

    confi=Button(principal,text="⚙️ \n INICIAL",bg="green",fg="black", font =("arial",30),command=lambda: configuracion() )# boton de configuracion inicial
    confi.place(x=200,y=500)# ubicacion de configuracion inicial

    binformacion=Button(principal,text="About",bg="green",fg="black", font =("arial",30),command=lambda: informacion() )# boton de informacion
    binformacion.place(x=5,y=800) # ubicacion de boton informacion (about)


    principal.mainloop() # iniciar la ventana


###################################################################
###################################################################
"_______________VENTANA DE CONFIGURACION INICIAL _________________________"

###################################################################
"Elige el escudo de su equipo"
def configuracion():    

    # Variables globales
    global  escudo_seleccionado, escudo_selecciondo2
    escudo_seleccionado = 1
    escudo_seleccionado2 = 1
    
     # Cargar imágenes de
    ########################################################################################
    escudo1_imagen = cargarImagen("escudo1.png").subsample(6, 6)  # Reducir tamaño
    escudo2_imagen = cargarImagen("escudo2.png").subsample(4,4)  # Reducir tamaño
    escudo3_imagen = cargarImagen("escudo3.png").subsample(2, 2)  # Reducir tamaño

    # Función para seleccionar skin
    def seleccionar_escudo(escudo_numero):
        global escudo_seleccionado
        escudo_seleccionado = escudo_numero
        escudo_imagen = cargarImagen(f"escudo{escudo_seleccionado}.png")

 # Crear ventana principal
    ventana = Toplevel()
    ventana.title("Seleccion del equipo")
    ventana.minsize(800,900)
    ventana.config(bg="lightblue")
    
    # Etiqueta de título
    titulo_label = Label(ventana, text="¡Selecciona tu equipo!", font=("Arial", 24))
    titulo_label.pack(pady=20)

    equipo= Label(ventana, text="Equipo visitante", font=("Arial", 20))
    equipo.pack(padx=15, pady=15)

    # Marco para las opciones de skin
    marco= Frame(ventana)
    marco.pack()

    # Crear y colocar los botones con las imágenes de las skins (mismo tamaño)
    escudo1_boton = Button(marco, image=escudo1_imagen, command=lambda: seleccionar_escudo(1) )
    escudo1_boton.config(width=200, height=200)
    escudo1_boton.pack(side=LEFT, padx=15, pady=15)

    escudo2_boton = Button(marco, image=escudo2_imagen, command=lambda: seleccionar_escudo(2) )
    escudo2_boton.config(width=200, height=200) 
    escudo2_boton.pack(side=LEFT, padx=10, pady=10)

    escudo3_boton = Button(marco, image=escudo3_imagen, command=lambda: seleccionar_escudo(3) )
    escudo3_boton.config(width=200, height=200)
    escudo3_boton.pack(side=LEFT, padx=10, pady=10)


#######################################################

    # Función para seleccionar skin
    def seleccionar_escudo2(escudo_numero2):
        global escudo_seleccionado2
        escudo_seleccionado2 = escudo_numero2
        escudo_imagen2 = cargarImagen(f"escudo{escudo_seleccionado2}.png")

    equipo= Label(ventana, text="Equipo de la casa", font=("Arial", 20))
    equipo.pack(padx=20, pady=20)

     # Marco para las opciones de skin
    marco= Frame(ventana)
    marco.pack()

    # Crear y colocar los botones con las imágenes de las skins (mismo tamaño)
    escudo1_b = Button(marco, image=escudo1_imagen, command=lambda: seleccionar_escudo2(1) )
    escudo1_b.config(width=200, height=200)
    escudo1_b.pack(side=LEFT, padx=25, pady=25)

    escudo2_b = Button(marco, image=escudo2_imagen, command=lambda: seleccionar_escudo2(2) )
    escudo2_b.config(width=200, height=200) 
    escudo2_b.pack(side=LEFT, padx=20, pady=20)

    escudo3_b = Button(marco, image=escudo3_imagen, command=lambda: seleccionar_escudo2(3) )
    escudo3_b.config(width=200, height=200)
    escudo3_b.pack(side=LEFT, padx=20, pady=20)





#######################################################
#######################################################
#######################################################


    # Botón para confirmar las selecciones
    confirmar_boton = Button(ventana, text="¡Siguiente!", bg="RoyalBlue2",command=lambda: portero() and ventana.destroy(),font=("Arial", 20, "bold"))
    confirmar_boton.pack(pady=20)
    confirmar_boton.pack(pady=70)

    ventana.mainloop()


        
"ELIGE EL PORTERO Y EL ARTILLERO"
    # Función para obtener el nombre del jugador
def portero():
    # Variables globales
    global portero_seleccionado, portero_seleccionado2
    portero_seleccionado = 1
    portero_seleccionado2 = 1
    
    # Cargar imágenes de
    ########################################################################################
    Arquero1 = cargarImagen("P1.png").subsample(6, 6)  # Reducir tamaño
    Arquero2 = cargarImagen("P2.png").subsample(4, 4)  # Reducir tamaño
    Arquero3 = cargarImagen("P3.png").subsample(2, 2)  # Reducir tamaño

    # Función para seleccionar skin
    def seleccionar_portero(portero_numero):
        global portero_seleccionado
        portero_seleccionado = portero_numero
        portero_imagen = cargarImagen(f"P{portero_seleccionado}.png")


        # Crear ventana principal

    ventana = Toplevel()
    ventana.title("Seleccion del Arquero")
    ventana.minsize(800, 900)
    ventana.config(bg="lightblue")

    # Etiqueta de título
    titulo_label = Label(ventana, text="¡Selecciona tu Portero!", font=("Arial", 24))
    titulo_label.pack(pady=20)

    por= Label(ventana, text="Portero  del visitante", font=("Arial", 20))
    por.pack(padx=15, pady=15)

    # Marco para las opciones de skin
    marco = Frame(ventana)
    marco.pack()

    # Crear y colocar los botones con las imágenes de las skins (mismo tamaño)
    Arquero1_boton = Button(marco, image=Arquero1, command=lambda:seleccionar_portero(1))
    Arquero1_boton.config(width=200, height=200)
    Arquero1_boton.pack(side=LEFT, padx=15, pady=15)

    Arquero2_boton = Button(marco, image=Arquero2, command=lambda: seleccionar_portero(2))
    Arquero2_boton.config(width=200, height=200)
    Arquero2_boton.pack(side=LEFT, padx=10, pady=10)

    Arquero3_boton = Button(marco, image=Arquero3, command=lambda: seleccionar_portero(3))
    Arquero3_boton.config(width=200, height=200)
    Arquero3_boton.pack(side=LEFT, padx=10, pady=10)

    ###################################
    ######################################
          # Función para seleccionar skin
    def seleccionar_portero2(portero_numero2):
        global portero_seleccionado2
        portero_seleccionado2 = portero_numero2
        portero_imagen2 = cargarImagen(f"P{portero_seleccionado2}.png")
        

    por2= Label(ventana, text="Portero de la casa", font=("Arial", 20))
    por2.pack(padx=20, pady=20)


    marco = Frame(ventana)
    marco.pack()
        
    # Crear y colocar los botones con las imágenes de las skins (mismo tamaño)
    Arquero1_b= Button(marco, image=Arquero1, command=lambda:seleccionar_portero2(1))
    Arquero1_b.config(width=200, height=200)
    Arquero1_b.pack(side=LEFT, padx=25, pady=25)

    Arquero2_b = Button(marco, image=Arquero2, command=lambda: seleccionar_portero2(2))
    Arquero2_b.config(width=200, height=200)
    Arquero2_b.pack(side=LEFT, padx=20, pady=20)

    Arquero3_b = Button(marco, image=Arquero3, command=lambda: seleccionar_portero2(3))
    Arquero3_b.config(width=200, height=200)
    Arquero3_b.pack(side=LEFT, padx=20, pady=20)



    #########################################
    ###########################################

    # Botón para confirmar las selecciones
    confirmar_boton = Button(ventana, text="¡Siguiente!", bg="RoyalBlue2", command=lambda:Artillero(),
                             font=("Arial", 20, "bold"))
    confirmar_boton.pack(pady=20)
    confirmar_boton.pack(pady=20)
    ventana.mainloop()

    # Función para iniciar el juego (opcional)
def Artillero():
    # Variables globales
    global artillero_seleccionado,  artillero_seleccionado2
    artillero_seleccionado = 1
    artillero_seleccionado2 =1 
    
    # Cargar imágenes de
    ########################################################################################
    Artillero1 = cargarImagen("A1.png").subsample(6, 6)  # Reducir tamaño
    Artillero2 = cargarImagen("A2.png").subsample(4, 4)  # Reducir tamaño
    Artillero3 = cargarImagen("A3.png").subsample(2, 2)  # Reducir tamaño

    # Función para seleccionar skin
    def seleccionar_artillero(artillero_numero):
        global artillero_seleccionado
        artillero_seleccionado = artillero_numero
        artillero_imagen = cargarImagen(f"A{artillero_seleccionado}.png")
        

        # Crear ventana principal

    ventana = Toplevel()
    ventana.title("Seleccion del Artillero")
    ventana.minsize(800, 900)
    ventana.config(bg="lightblue")

    # Etiqueta de título
    titulo_label = Label(ventana, text="¡Selecciona tu Artillero!", font=("Arial", 24))
    titulo_label.pack(pady=20)
    
    equipo= Label(ventana, text="Artillero del visitante", font=("Arial", 20))
    equipo.pack(padx=15, pady=15)


    # Marco para las opciones de skin
    marco = Frame(ventana)
    marco.pack()

    # Crear y colocar los botones con las imágenes de las skins (mismo tamaño)
    Artillero1_boton = Button(marco, image=Artillero1, command=lambda: seleccionar_artillero(1))
    Artillero1_boton.config(width=200, height=200)
    Artillero1_boton.pack(side=LEFT, padx=15, pady=15)

    Artillero2_boton = Button(marco, image=Artillero2, command=lambda: seleccionar_artillero(2))
    Artillero2_boton.config(width=200, height=200)
    Artillero2_boton.pack(side=LEFT, padx=10, pady=10)

    Artillero3_boton = Button(marco, image=Artillero3, command=lambda: seleccionar_artillero(3))
    Artillero3_boton.config(width=200, height=200)
    Artillero3_boton.pack(side=LEFT, padx=10, pady=10)


#######################################
########################################
      # Función para seleccionar skin
    def seleccionar_artillero2(artillero_numero2):
        global artillero_seleccionado2
        artillero_seleccionado2 = artillero_numero2
        artillero_imagen2 = cargarImagen(f"A{artillero_seleccionado2}.png")
        
    po= Label(ventana, text="Artillero de la casa", font=("Arial", 20))
    po.pack(padx=20, pady=20)
            # Marco para las opciones de skin
    marco = Frame(ventana)
    marco.pack()

    # Crear y colocar los botones con las imágenes de las skins (mismo tamaño)
    Artillero1_b= Button(marco, image=Artillero1, command=lambda: seleccionar_artillero2(1))
    Artillero1_b.config(width=200, height=200)
    Artillero1_b.pack(side=LEFT, padx=25, pady=25)

    Artillero2_b = Button(marco, image=Artillero2, command=lambda: seleccionar_artillero2(2))
    Artillero2_b.config(width=200, height=200)
    Artillero2_b.pack(side=LEFT, padx=20, pady=20)

    Artillero3_b = Button(marco, image=Artillero3, command=lambda: seleccionar_artillero2(3))
    Artillero3_b.config(width=200, height=200)
    Artillero3_b.pack(side=LEFT, padx=20, pady=20)
        
#############################################
#############################################
            # Botón para confirmar las selecciones
    confirmar_boton = Button(ventana, text="¡Siguiente!", bg="RoyalBlue2", command=lambda: mostrar_selecciones(),
                             font=("Arial", 20, "bold"))
    confirmar_boton.pack(pady=20)
    confirmar_boton.pack(pady=20)

    

    ventana.mainloop()

# Variables globales para las imágenes
escudo_imagen = None
portero_imagen = None
artillero_imagen = None

#from PIL import Image, ImageTk
##############################################################
def mostrar_selecciones():
    global escudo_seleccionado, portero_seleccionado, artillero_seleccionado,escudo_seleccionado2, portero_seleccionado2, artillero_seleccionado2

    ventana_selecciones = Toplevel()
    ventana_selecciones.title("Selecciones del usuario")
    ventana_selecciones.minsize(800, 600)

    # Mostrar selecciones de Configuracion
    label_configuracion = Label(ventana_selecciones, text="Equipo Visitante:")
    label_configuracion.pack(pady =10)
    escudo_image = Image.open(f"Imagenes/escudo{escudo_seleccionado}.png")
    escudo_image = escudo_image.resize((200, 200))
    escudo_imagen = ImageTk.PhotoImage(escudo_image)
    label_escudo_seleccionado = Label(ventana_selecciones, image=escudo_imagen)
    label_escudo_seleccionado.image = escudo_imagen  # Keep a reference to the image
    label_escudo_seleccionado.pack(padx=15, pady=15)

    # Mostrar selecciones de Portero
    label_portero = Label(ventana_selecciones, text="Portero:")
    label_portero.pack()
    portero_image = Image.open(f"Imagenes/P{portero_seleccionado}.png")
    portero_image = portero_image.resize((200, 200))
    portero_imagen = ImageTk.PhotoImage(portero_image)
    label_portero_seleccionado = Label(ventana_selecciones, image=portero_imagen)
    label_portero_seleccionado.image = portero_imagen  # Keep a reference to the image
    label_portero_seleccionado.pack(padx=10, pady=10)

    # Mostrar selecciones de Artillero
    label_artillero = Label(ventana_selecciones, text="Artillero:")
    label_artillero.pack()
    artillero_image = Image.open(f"Imagenes/A{artillero_seleccionado}.png")
    artillero_image = artillero_image.resize((200, 200))
    artillero_imagen = ImageTk.PhotoImage(artillero_image)
    label_artillero_seleccionado = Label(ventana_selecciones, image=artillero_imagen)
    label_artillero_seleccionado.image = artillero_imagen  # Keep a reference to the image
    label_artillero_seleccionado.pack(padx=10, pady=10)

    #####################################################
        # Mostrar selecciones de Configuracion
    onfiguracion = Label(ventana_selecciones, text="Equipo de la casa:")
    onfiguracion.pack()
    escud = Image.open(f"Imagenes/escudo{escudo_seleccionado2}.png")
    escud = escud.resize((200, 200))
    escud = ImageTk.PhotoImage(escud)
    label_escudo_seleccionado2 = Label(ventana_selecciones, image=escud)
    label_escudo_seleccionado2.image = escudo_imagen  # Keep a reference to the image
    label_escudo_seleccionado2.pack(side=RIGHT, padx=25, pady=25)

    # Mostrar selecciones de Portero
    label_portero2 = Label(ventana_selecciones, text="Portero :")
    label_portero2.pack()
    portero_image2 = Image.open(f"Imagenes/P{portero_seleccionado2}.png")
    portero_image2 = portero_image.resize((200, 200))
    portero_imagen2 = ImageTk.PhotoImage(portero_image2)
    label_portero_seleccionado2 = Label(ventana_selecciones, image=portero_imagen2)
    label_portero_seleccionado2.image = portero_imagen  # Keep a reference to the image
    label_portero_seleccionado2.pack(side=RIGHT, padx=20, pady=20)

    # Mostrar selecciones de Artillero
    label_artillero2 = Label(ventana_selecciones, text="Artillero:")
    label_artillero2.pack(side=RIGHT, padx=20, pady=20)
    artillero_image2= Image.open(f"Imagenes/A{artillero_seleccionado2}.png")
    artillero_image2 = artillero_image.resize((200, 200))
    artillero_imagen2 = ImageTk.PhotoImage(artillero_image2)
    label_artillero_seleccionado2 = Label(ventana_selecciones, image=artillero_imagen2)
    label_artillero_seleccionado2.image = artillero_imagen  # Keep a reference to the image
    label_artillero_seleccionado2.pack(side=RIGHT, padx=20, pady=20)
    

    # Botón para ir al partido
    boton_siguiente = Button(ventana_selecciones, text="Siguiente", command=lambda: partido(ventana_selecciones))
    boton_siguiente.pack(pady=20)

    
    ventana_selecciones.mainloop()
################################################
##############################################
def partido(ventana_selecciones):
    global escudo_seleccionado, gris_images, verde_image
    ventana_selecciones.destroy()  # Cierra la ventana anterior

    ventana_partido = Toplevel()
    ventana_partido.title("Partido")
    ventana_partido.geometry("1200x800")

    # Create a Canvas that covers the entire window
    canvas = Canvas(ventana_partido, width=1200, height=800, highlightthickness=0)
    canvas.place(x=0, y=0)

    # Cargar imagen de fondo
    fondo_partido = cargarImagen("Estadio.png")
    canvas.create_image(0, 0, image=fondo_partido, anchor='nw')

    # Mostrar escudo seleccionado
    escudo_image = Image.open(f"Imagenes/escudo{escudo_seleccionado}.png")
    escudo_image = escudo_image.resize((300, 300))  # Ajustar tamaño de la imagen
    escudo_imagen = ImageTk.PhotoImage(escudo_image)
    canvas.create_image(200, 200, image=escudo_imagen)

    # 5 Gris.png next to each other
    global gris_images
    gris_images = []
    x_pos = 40
    for i in range(5):
        gris_image = cargarImagen("Gris.png")
        gris_images.append(gris_image)
        canvas.create_image(x_pos, 600, image=gris_image)
        x_pos += 70

    # 5 Gris.png next to each other
    global gris_images_2
    gris_images_2 = []
    x_pos = 850
    for i in range(5):
        gris_image = cargarImagen("Gris.png")
        gris_images_2.append(gris_image)
        canvas.create_image(x_pos, 600, image=gris_image)
        x_pos += 70

    # Cargar la imagen verde
    global verde_image
    verde_image = cargarImagen("Verde.png")

    # Llama a la función cambio_imagen cada 100 ms para verificar el contacto
    ventana_partido.after(100, cambio_imagen)
    cambio_imagen(canvas)
    ventana_partido.mainloop()


    ventana_partido.mainloop()







###################################################################
###################################################################
    "_______________VENTANA DEL ABOUT_________________________"
###################################################################
###################################################################
def informacion():
    Vtercer = Toplevel() #Se crea la ventana
    Vtercer.minsize(800,900)# tamaño de la ventana creada
    Vtercer.resizable(width=NO,height=NO) #no sea grande ni pequeña evitar distorción
    "Cargar la imagen de fondo"
    "___________________________________________"
    fondo2 = cargarImagen("fondo1.png") #se pone para que acepte la imagen
    imagen = tkinter.Label(Vtercer,image = fondo2) #le decimos  que lo ponga de pantalla
    imagen.place(x=0,y=0) # ubicacion  de la  imagen de fondo 
    "___________________________________________"

    
    Vtercer.title("Información") #crea nombre a la ventana visible parte superior izquierda
    titulo=Label(Vtercer,text="Detalles esenciales  ",bg="lawn green")#texto inincail de la ventana 
    titulo.place(x=250,y=4) #ubicacion
  
    info= Label(Vtercer,text="Este proyecto fue realizado por Rachell Freer Piedra,siendo estudiante \n de Ingenieria en Computadores ",bg="sky blue")#texto
    info.place(x=30,y=40) # ubicacion 
    "____________________________________"
    "imagen del creador"
    fotoPersonal = cargarImagen("personal.png") #cargar la imagen
    PersonalReducida= fotoPersonal.subsample(6,6) # reducir la imagen 
    # etiqueta para mostrar la foto 
    etiq_personal= Label(Vtercer, image= PersonalReducida) # esto es para mostrar
    etiq_personal.place(x=450, y=100)  # Ajustar la posición 

    
    "_____________________________________"
    carnet= Label(Vtercer,text="Carnet del estudiante \n 2024119149 ",bg="turquoise")#texto
    carnet.place(x=450,y=380) # ubicacion
    edad= Label(Vtercer,text="Edad cumplida \n 17 años ",bg="turquoise")#texto
    edad.place(x=450,y=320) # ubicacion
    
    nombre= Label(Vtercer,text="Asignatura: \n Fundamentos de sistemas Computacionales ",bg="turquoise")  # nombre del creador 
    nombre.place(x=30,y=300) # ubicacion
    profe= Label(Vtercer,text="Profesor: \n Luis Alberto Chavarría Zamora ",bg="turquoise")  # nombre del creador 
    profe.place(x=30,y=360) # ubicacion
    year=Label(Vtercer,text="Año: 2024",bg="turquoise")  # nombre del creador
    year.place(x=250,y=450) # ubicacion
    lugar=Label(Vtercer,text="País de producción:  Costa Rica ",bg="turquoise")  # nombre del creador
    lugar.place(x=30,y=420) # ubicacion
    version=Label(Vtercer,text="Versión:  1.0 ",bg="turquoise")  # nombre del creador
    version.place(x=30,y=450) # ubicacion
    


    Vtercer.mainloop()# para que funciones



###################################################################
"_______________VENTANA DE PRELIMINARES DEL JUEGO________________________"
###################################################################
    


    

Vprincipal()    




















