#Importar tkinter
from tkinter import ttk
from tkinter import *
#Creacion de la clase product
class Product:
    def __init__(self, window):#para mantener un mejor codigo
        self.wind = window
        self.wind.title('sistema de registro')#creacion del nombre de la aplicacion
        #creacion de un contenedor o frame
        titulo = LabelFrame(self.wind, text = "Ferretería El Tornillo Feliz")
        titulo.grid(row = 0, column = 0, columnspan = 3, pady = 20)
        #Creacion de DNI Imput
        Label(titulo, text = 'DNI: ').grid(row = 1, column = 0)
        self.DNI = Entry(titulo)
        self.DNI.grid(row = 1, column = 1)
        #Creacion de Apellido en un Imput
        Label(titulo, text = 'Apellido:').grid(row = 2, column = 0)
        self.apellido = Entry(titulo)
        self.apellido.grid(row = 2, column = 1)
        #creacion de nombre en un imput
        Label(titulo, text = 'Nombre: ').grid(row = 2, column = 2)
        self.nombre = Entry(titulo)
        self.nombre.grid (row = 2, column = 3)
        #creacion de Direccion en un imput
        Label(titulo, text = 'Direccion:  ').grid(row = 3, column = 0)
        self.direccion = Entry(titulo)
        self.direccion.grid(row = 3, column = 1)
        #Creacion de telefono en un imput
        Label(titulo, text = 'Telefono:  ').grid(row = 4, column = 0)
        self.direccion = Entry(titulo)
        self.direccion.grid(row = 4, column = 1)
        #Creacion de Codigo de producto en un imput
        Label(titulo, text = 'Cod_prod:  ').grid(row = 5, column = 0)
        self.cod_prod = Entry(titulo)
        self.cod_prod.grid(row = 6, column = 0)
        #Creacion de descripción en un imput
        Label(titulo, text = 'Descripción:  ').grid(row = 5, column = 1)
        self.descripcion = Entry(titulo)
        self.descripcion.grid(row = 6, column = 1)
        #Creacion de unidad en un imput
        Label(titulo, text = 'Unidad:  ').grid(row = 5, column = 2)
        self.unidad = Entry(titulo)
        self.unidad.grid(row = 6, column = 2)
#para ejecutar tinker
if __name__ == '__main__':
    window = Tk()
    application = Product(window)#para mantener un mejor orden
    window.mainloop()