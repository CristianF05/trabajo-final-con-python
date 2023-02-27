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
#para ejecutar tinker
if __name__ == '__main__':
    window = Tk()
    application = Product(window)#para mantener un mejor orden
    window.mainloop()