#------------------------------
# Plataforma Guanentá 2.0
#------------------------------

# se importa la libreria tkinter con todas sus funciones
from tkinter import *
from tkinter import messagebox

#------------------------------
# funciones de la app
#------------------------------

# borrar
def borrar():
    messagebox.showinfo("Plataforma Guanentá 2.0", "Los datos serán borrados")

# salir
def salir():
    messagebox.showinfo("Plataforma Guanentá 2.0", "La app se va a cerrar")
    ventana_principal.destroy()

#------------------------------
# ventana principal de la app
#------------------------------

# se declara una variable llamada ventana_principal, que adquiere las caracteristicas de un objeto Tk()
ventana_principal = Tk()

# titulo de la ventana
ventana_principal.title("Stephanie Ortiz Pico")

# tamaño de la ventana
ventana_principal.geometry("600x500")

# deshabilitar boton maximizar
ventana_principal.resizable(False, False)

# color de fondo de la ventana
ventana_principal.config(bg="black")

#------------------------------
# frame entrada
#------------------------------
frame_entrada= Frame(ventana_principal)
frame_entrada.config(bg="thistle", width=600, height=500)
frame_entrada.place(x=0, y=0)

#------------------------------
# frame blanco
#------------------------------
frame_blanco= Frame(ventana_principal)
frame_blanco.config(bg="white", width=580, height=480)
frame_blanco.place(x=10, y=10)

#------------------------------
# frame thistle
#------------------------------
frame_thistle= Frame(ventana_principal)
frame_thistle.config(bg="thistle", width=560, height=60)
frame_thistle.place(x=20, y=20)

#--------------------------------
# barra menu
#--------------------------------
barra_menu = Menu()
ventana_principal.config(menu=barra_menu)

menu_convertir = Menu(tearoff=0)
menu_convertir.add_separator()
menu_convertir.add_command(label="Borrar", command=borrar)

menu_salir = Menu(tearoff=0)
menu_salir.add_command(label="Salir", command=salir)

barra_menu.add_cascade(label="Menú", menu=menu_convertir)
barra_menu.add_cascade(label="Salir", menu=menu_salir)

# titulo de la app
titulo = Label(frame_thistle, text="Plataforma Guanentá 2.0")
titulo.config(bg = "thistle",fg="white", font=("Helvetica", 30))
titulo.place(x=70,y=13)

# etiqueta para el nombre
lb_nombre = Label(frame_blanco, text = "Nombre del estudiante = ")
lb_nombre.config(bg="white", fg="thistle", font=("Helvetica", 18))
lb_nombre.place(x=30, y=100)

# caja de texto para el nombre
entry_nombre = Entry(frame_blanco, textvariable=lb_nombre)
entry_nombre.config(bg="white", fg="thistle", font=("Times New Roman", 18), width=20)
entry_nombre.focus_set()
entry_nombre.place(x=300, y=95)

# etiqueta para el número telefónico
lb_telefono = Label(frame_blanco, text = "Número de Teléfono = ")
lb_telefono.config(bg="white", fg="thistle", font=("Helvetica", 18))
lb_telefono.place(x=30, y=160)

# caja de texto para el número telefónico
entry_telefono = Entry(frame_blanco, textvariable=lb_telefono)
entry_telefono.config(bg="white", fg="thistle", font=("Times New Roman", 18), width=20)
entry_telefono.focus_set()
entry_telefono.place(x=300, y=155)

# etiqueta para el correo
lb_correo = Label(frame_blanco, text = "Correo Electrónico = ")
lb_correo.config(bg="white", fg="thistle", font=("Helvetica", 18))
lb_correo.place(x=30, y=220)

# caja de texto para el correo
entry_correo = Entry(frame_blanco, textvariable=lb_correo)
entry_correo.config(bg="white", fg="thistle", font=("Times New Roman", 18), width=20)
entry_correo.focus_set()
entry_correo.place(x=300, y=215)

# abrir toplevel notas
def abrir_toplevel_notas():
    global toplevel_notas
    toplevel_notas = Toplevel()
    toplevel_notas.title("Stephanie Ortiz Pico")
    toplevel_notas.resizable(False, False)
    toplevel_notas.geometry("600x400")
    toplevel_notas.config(bg="white")

    # etiqueta para notas
    lb_c = Label(toplevel_notas, text = "Notas")
    lb_c.config(bg="white", fg="thistle", font=("Helvetica", 30))
    lb_c.place(x=230, y=15)

    # etiqueta para nota actitudinal
    lb_actitudinal = Label(toplevel_notas, text = "Actitudinal")
    lb_actitudinal.config(bg="white", fg="thistle", font=("Helvetica", 18))
    lb_actitudinal.place(x=150, y=65)

    # etiqueta para nota procedimental
    lb_procedimental = Label(toplevel_notas, text = "Procedimental")
    lb_procedimental.config(bg="white", fg="thistle", font=("Helvetica", 18))
    lb_procedimental.place(x=150, y=125)

    # etiqueta para nota cognitiva
    lb_cognitiva = Label(toplevel_notas, text = "Cognitivo")
    lb_cognitiva.config(bg="white", fg="thistle", font=("Helvetica", 18))
    lb_cognitiva.place(x=150, y=185)

    # etiqueta para nota bimestral
    lb_bimestral = Label(toplevel_notas, text = "Bimestral")
    lb_bimestral.config(bg="white", fg="thistle", font=("Helvetica", 18))
    lb_bimestral.place(x=150, y=245)
    
    # etiqueta para nota autoevaluacion
    lb_autoevaluacion = Label(toplevel_notas, text = "Autoevaluacion")
    lb_autoevaluacion.config(bg="white", fg="thistle", font=("Helvetica", 18))
    lb_autoevaluacion.place(x=150, y=305)

    # caja de texto para nota actitudinal
    entry_actitudinal = Entry(toplevel_notas, textvariable="")
    entry_actitudinal.config(bg="white", fg="thistle", font=("Times New Roman", 18), width=6)
    entry_actitudinal.focus_set()
    entry_actitudinal.place(x=340,y=60)

    # caja de texto para nota procedimental
    entry_procedimental = Entry(toplevel_notas, textvariable="")
    entry_procedimental.config(bg="white", fg="thistle", font=("Times New Roman", 18), width=6)
    entry_procedimental.focus_set()
    entry_procedimental.place(x=340,y=120)

    # caja de texto para nota cognitiva
    entry_cognitiva = Entry(toplevel_notas, textvariable="")
    entry_cognitiva.config(bg="white", fg="thistle", font=("Times New Roman", 18), width=6)
    entry_cognitiva.focus_set()
    entry_cognitiva.place(x=340,y=180)
    
    # caja de texto para nota bimestral
    entry_bimestral = Entry(toplevel_notas, textvariable="")
    entry_bimestral.config(bg="white", fg="thistle", font=("Times New Roman", 18), width=6)
    entry_bimestral.focus_set()
    entry_bimestral.place(x=340,y=240)

    # caja de texto para nota autoevaluacion
    entry_autoevaluacion = Entry(toplevel_notas, textvariable="")
    entry_autoevaluacion.config(bg="white", fg="thistle", font=("Times New Roman", 18), width=6)
    entry_autoevaluacion.focus_set()
    entry_autoevaluacion.place(x=340,y=300)

# boton para calcular notas
bt_convertir = Button(frame_blanco,text="Calcular Notas", command=abrir_toplevel_notas)
bt_convertir.place(x=230, y=300, width=100, height=30)

# boton para borrar
bt_borrar = Button(frame_blanco, text="Borrar", command=borrar)
bt_borrar.place(x=190, y=35, width=100, height=30)

# run
# se ejecuta el metodo mainlop() de la clase Tk () a través de la instancia ventana_principal. Este metodo despliega una ventana en la pantalla y queda a la espera de lo que el usuario haga (click en un botón, escrubir, etc). Cada acción del usuario se conoce como un evento. El método mainloop() es un bucle infinito.
ventana_principal.mainloop()