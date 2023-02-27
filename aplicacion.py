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
        titulo.grid(row = 0, column = 20, columnspan = 2, pady = 20)
        #Name Imput de DNI
        Label(titulo, text = 'DNI: ').grid(row = 1, column = 0)
        self.name = Entry(titulo)
        self.name.grid(row = 1, column = 4)
#para ejecutar tinker
if __name__ == '__main__':
    window = Tk()
    application = Product(window)#para mantener un mejor orden
    window.mainloop()