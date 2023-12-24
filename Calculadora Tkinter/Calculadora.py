import tkinter as tk
from pila import Pila
from tkinter import StringVar, Entry, Button, ttk

class Calculadora:

    def __init__(self):
        
        self.root = tk.Tk()
        self.root.geometry('319x410') #Hacer mas chico, botones letras quedan chicas
        self.root.title('Calculadora')
        self.root.resizable(False, False) # Temporal hasta saber como adaptar los btns al resizing

        self.ultimo_valor = Pila()
        self.entrada = ''
        self.res = StringVar()
        Entry(width = 27, bg = 'white', font = ('Arial', 37), textvariable = self.res).place(x = 0, y = 0)

        #Tanda izquierda
        Button(width = 10, height = 4, relief = 'solid', text = '1', bg = '#424949', command = lambda:self.ecuacion(1)).place(x = 0, y = 130)
        Button(width = 10, height = 4, relief = 'solid', text = '4', bg = '#424949', command = lambda:self.ecuacion(4)).place(x = 0, y = 200)
        Button(width = 10, height = 4, relief = 'solid', text = '7', bg = '#424949', command = lambda:self.ecuacion(7)).place(x = 0, y = 270)

        #Tanda central
        Button(width = 10, height = 4, relief = 'solid', text = '2', bg = '#424949', command = lambda:self.ecuacion(2)).place(x = 80, y = 130)
        Button(width = 10, height = 4, relief = 'solid', text = '5', bg = '#424949', command = lambda:self.ecuacion(5)).place(x = 80, y = 200)
        Button(width = 10, height = 4, relief = 'solid', text = '8', bg = '#424949', command = lambda:self.ecuacion(8)).place(x = 80, y = 270)
        Button(width = 10, height = 4, relief = 'solid', text = '0', bg = '#424949', command = lambda:self.ecuacion(0)).place(x = 80, y = 340)

        #Tanda derecha
        Button(width = 10, height = 4, relief = 'solid', text = '3', bg = '#424949', command = lambda:self.ecuacion(3)).place(x = 160, y = 130)
        Button(width = 10, height = 4, relief = 'solid', text = '6', bg = '#424949', command = lambda:self.ecuacion(6)).place(x = 160, y = 200)
        Button(width = 10, height = 4, relief = 'solid', text = '9', bg = '#424949', command = lambda:self.ecuacion(10)).place(x = 160, y = 270)
        Button(width = 10, height = 4, relief = 'solid', text = '%', bg = '#D68910', command = lambda:self.ecuacion('%')).place(x = 160, y = 340)
        
        #Central arriba
        Button(width = 10, height = 4, relief = 'solid', text = '/', bg = '#D68910', command = lambda:self.ecuacion('/')).place(x = 240, y = 60)
        Button(width = 10, height = 4, relief = 'solid', text = '(', bg = '#D68910', command = lambda:self.ecuacion('(')).place(x = 80, y = 60)
        Button(width = 10, height = 4, relief = 'solid', text = ')', bg = '#D68910', command = lambda:self.ecuacion(')')).place(x = 160, y = 60)
        Button(width = 10, height = 4, relief = 'solid', text = 'C', bg = '#D68910', command = lambda:self.reset()).place(x = 0, y = 60)

        #Operadores
        Button(width = 10, height = 4, relief = 'solid', text = '*', bg = '#D68910', command = lambda:self.ecuacion('*')).place(x = 240, y = 270)
        Button(width = 10, height = 4, relief = 'solid', text = '+', bg = '#D68910', command = lambda:self.ecuacion('+')).place(x = 240, y = 130)
        Button(width = 10, height = 4, relief = 'solid', text = '-', bg = '#D68910', command = lambda:self.ecuacion('-')).place(x = 240, y = 200)
        Button(width = 10, height = 4, relief = 'solid', text = '.', bg = '#D68910', command = lambda:self.ecuacion('.')).place(x = 0, y = 340)
        Button(width = 10, height = 4, relief = 'solid', text = '=', bg = '#D68910', command = lambda:self.resolver()).place(x = 240, y = 340)
        
        

        self.root.mainloop()
    
    def ecuacion(self, valor):
        self.entrada += str(valor)
        self.ultimo_valor.apilar(valor)
        self.res.set(self.entrada)
    
    def delete(self): # Funciona pero hay que fixear cosas
        if self.ultimo_valor.esta_vacia(): return

        aux = Pila()
        self.ultimo_valor.desapilar()
        self.entrada = ''

        while not self.ultimo_valor.esta_vacia():
            aux.apilar(self.ultimo_valor.desapilar())
        
        while not aux.esta_vacia():
            self.entrada += str(aux.ver_tope())
            self.ultimo_valor.apilar(aux.desapilar())

        self.res.set(self.entrada)

    def reset(self):
        self.entrada = ''
        self.res.set(self.entrada)
    
    def resolver(self):
        res = eval(self.entrada)
        self.res.set(res)
    




Calculadora()