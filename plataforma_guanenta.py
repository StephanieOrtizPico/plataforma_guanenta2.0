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
ventana_principal.title("Plataforma Guanentá 2.0")

# tamaño de la ventana
ventana_principal.geometry("1365x620")

# deshabilitar boton maximizar
ventana_principal.resizable(False, False)

# color de fondo de la ventana
ventana_principal.config(bg="black")

#------------------------------
# frame fondo
#------------------------------
frame_fondo= Frame(ventana_principal)
frame_fondo.config(bg="thistle", width=1365, height=620)
frame_fondo.place(x=0, y=0)

#------------------------------
# frame blanco
#------------------------------
frame_blanco= Frame(ventana_principal)
frame_blanco.config(bg="white", width=1345, height=600)
frame_blanco.place(x=10, y=10)

#------------------------------
# frame blanco
#------------------------------
frame_blanco= Frame(ventana_principal)
frame_blanco.config(bg="thistle", width=1325, height=60)
frame_blanco.place(x=20, y=20)

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
titulo = Label(frame_blanco, text="Plataforma Guanentá 2.0")
titulo.config(bg = "thistle",fg="white", font=("Helvetica", 35))
titulo.place(x=420,y=13)


# run
# se ejecuta el metodo mainlop() de la clase Tk () a través de la instancia ventana_principal. Este metodo despliega una ventana en la pantalla y queda a la espera de lo que el usuario haga (click en un botón, escrubir, etc). Cada acción del usuario se conoce como un evento. El método mainloop() es un bucle infinito.
ventana_principal.mainloop()