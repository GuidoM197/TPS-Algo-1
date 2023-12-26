import tkinter as tk
from pila import Pila
from tkinter import StringVar, Entry, Button, ttk, Frame

class Calculadora:

    def __init__(self):

        self.root = tk.Tk()
        self.root.geometry('400x472') # Hacer mas chico, botones letras quedan chicas
        self.root.title('Calculadora')
        self.root.resizable(False, False) # Temporal hasta saber como adaptar los btns al resizing

        self.ultimo_valor = Pila()
        self.abrir_parentesis = True
        self.entrada = ''
        self.res = StringVar()

        bf = Frame(self.root)
        bf1 = Frame(self.root)
        bf1.columnconfigure(0, weight = 1)

        bf.columnconfigure(0, weight = 1)
        bf.columnconfigure(1, weight = 1)
        bf.columnconfigure(2, weight = 1)
        bf.columnconfigure(3, weight = 1)

        Entry(bf1, width = 30, bg = 'white', font = ('Arial', 37), textvariable = self.res).grid(row = 0, column = 0, sticky = tk.W + tk.E)

        # Tanda izquierda
        Button(bf, width = 10, height = 4, relief = 'solid', text = '1', bg = '#424949', command = lambda:self.ecuacion(1)).grid(row = 2, column = 0, sticky = tk.W + tk.E)
        Button(bf, width = 10, height = 4, relief = 'solid', text = '4', bg = '#424949', command = lambda:self.ecuacion(4)).grid(row = 3, column = 0, sticky = tk.W + tk.E)
        Button(bf, width = 10, height = 4, relief = 'solid', text = '7', bg = '#424949', command = lambda:self.ecuacion(7)).grid(row = 4, column = 0, sticky = tk.W + tk.E)
        Button(bf, width = 10, height = 4, relief = 'solid', text = '.', bg = '#D68910', command = lambda:self.ecuacion('.')).grid(row = 5, column = 0, sticky = tk.W + tk.E)

        # Tanda central
        Button(bf, width = 10, height = 4, relief = 'solid', text = '2', bg = '#424949', command = lambda:self.ecuacion(2)).grid(row = 2, column = 1, sticky = tk.W + tk.E)
        Button(bf, width = 10, height = 4, relief = 'solid', text = '5', bg = '#424949', command = lambda:self.ecuacion(5)).grid(row = 3, column = 1, sticky = tk.W + tk.E)
        Button(bf, width = 10, height = 4, relief = 'solid', text = '8', bg = '#424949', command = lambda:self.ecuacion(8)).grid(row = 4, column = 1, sticky = tk.W + tk.E)
        Button(bf, width = 10, height = 4, relief = 'solid', text = '0', bg = '#424949', command = lambda:self.ecuacion(0)).grid(row = 5, column = 1, sticky = tk.W + tk.E)

        # Tanda derecha
        Button(bf, width = 10, height = 4, relief = 'solid', text = '3', bg = '#424949', command = lambda:self.ecuacion(3)).grid(row = 2, column = 2, sticky = tk.W + tk.E)
        Button(bf, width = 10, height = 4, relief = 'solid', text = '6', bg = '#424949', command = lambda:self.ecuacion(6)).grid(row = 3, column = 2, sticky = tk.W + tk.E)
        Button(bf, width = 10, height = 4, relief = 'solid', text = '9', bg = '#424949', command = lambda:self.ecuacion(9)).grid(row = 4, column = 2, sticky = tk.W + tk.E)
        Button(bf, width = 10, height = 4, relief = 'solid', text = '%', bg = '#D68910', command = lambda:self.ecuacion('%')).grid(row = 5, column = 2, sticky = tk.W + tk.E)
        
        # Central arriba
        Button(bf, width = 10, height = 4, relief = 'solid', text = '/', bg = '#D68910', command = lambda:self.ecuacion('/')).grid(row = 1, column = 3, sticky = tk.W + tk.E)
        Button(bf, width = 10, height = 4, relief = 'solid', text = '()', bg = '#D68910', command = lambda:self.ecuacion('()')).grid(row = 1, column = 1, sticky = tk.W + tk.E)
        Button(bf, width = 10, height = 4, relief = 'solid', text = 'DEL', bg = '#D68910', command = lambda:self.delete()).grid(row = 1, column = 2, sticky = tk.W + tk.E)
        Button(bf, width = 10, height = 4, relief = 'solid', text = 'C', bg = '#D68910', command = lambda:self.reset()).grid(row = 1, column = 0, sticky = tk.W + tk.E)

        # Operadores
        Button(bf, width = 10, height = 4, relief = 'solid', text = '*', bg = '#D68910', command = lambda:self.ecuacion('*')).grid(row = 2, column = 3, sticky = tk.W + tk.E)
        Button(bf, width = 10, height = 4, relief = 'solid', text = '+', bg = '#D68910', command = lambda:self.ecuacion('+')).grid(row = 3, column = 3, sticky = tk.W + tk.E)
        Button(bf, width = 10, height = 4, relief = 'solid', text = '-', bg = '#D68910', command = lambda:self.ecuacion('-')).grid(row = 4, column = 3, sticky = tk.W + tk.E)
        Button(bf, width = 10, height = 4, relief = 'solid', text = '=', bg = '#D68910', command = lambda:self.resolver()).grid(row = 5, column = 3, sticky = tk.W + tk.E)

        bf1.pack(fill = 'x')        
        bf.pack(fill = 'x')

        self.root.mainloop()
    
    def ecuacion(self, valor):

        if (valor == '()') and self.abrir_parentesis: 
            valor = '('
            self.abrir_parentesis = False
        elif valor == '()' and not self.abrir_parentesis: 
            valor = ')'
            self.abrir_parentesis = True

        if (valor == '%'): 

            self.res.set(self.entrada + '%')
            valor = '/100'
            self.entrada += str(valor)
            print(self.entrada)
            self.ultimo_valor.apilar(valor)
            return

        self.entrada += str(valor)
        self.ultimo_valor.apilar(valor)
        self.res.set(self.entrada)
    
    def delete(self):
        if self.ultimo_valor.esta_vacia(): return

        aux = Pila()
        ultimo = self.ultimo_valor.desapilar()
        self.entrada = ''

        if ultimo == '(': self.abrir_parentesis = True
        elif ultimo == ')': self.abrir_parentesis = False 

        while not self.ultimo_valor.esta_vacia():
            aux.apilar(self.ultimo_valor.desapilar())
        
        while not aux.esta_vacia():
            self.entrada += str(aux.ver_tope())
            self.ultimo_valor.apilar(aux.desapilar())

        self.res.set(self.entrada)

    def reset(self):
        self.entrada = ''
        self.abrir_parentesis = True
        self.ultimo_valor = Pila()
        self.res.set(self.entrada)
    
    def resolver(self):
        chequeo = self.entrada

        while (chequeo[0] == '0') and (len(chequeo) > 1) and (chequeo[1] != '0') and (chequeo[1] != '/'): 
            if chequeo[1] == '.':
                chequeo = chequeo[2:]
            else:
                chequeo = chequeo[1:]

        res = eval(chequeo)
        print(res)
        if (type(res) == float):
        
            res = str(res)

            # if (len(res) > 3) and (int(res[-1]) == 0):

            if (res[0] == '0') and (len(res) < 3):
                res = '0.00'

                if (int(res[0]) != 0) and (int(res[3]) == 0):
                    res = res[0] + '.00'

                res = float(res)
                res = int(res)
                res = str(res)

        self.ultimo_valor = Pila()
        self.entrada = str(res)

        for num in self.entrada:
            self.ultimo_valor.apilar(num)

        self.res.set(res)




Calculadora()