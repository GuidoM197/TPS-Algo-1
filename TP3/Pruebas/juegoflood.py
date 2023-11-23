from flood import Flood, recorrer_matriz_recur, _cambiar_color
from pila import Pila
from cola import Cola

def copiar_pila(origen):
    aux = Pila()
    copia = Pila()

    while not origen.esta_vacia():

        aux.apilar(origen.desapilar())


    while not aux.esta_vacia():

        dato = aux.ver_tope()
        copia.apilar(dato)
        origen.apilar(dato)
        aux.desapilar()

    return copia


def verificar_existencia(pila, movimiento):
    '''
    Compueba la existencia de un movimiento en la pila.
    '''
    copia = pila
    act = copia.ver_tope()

    while not copia.esta_vacia():
        if act == movimiento: return True
        act = copia.desapilar()
    
    return False


def encontrar_max(diccionario):
    maximo = 0
    cantidad_veces_max = 0

    for color in diccionario:
        if diccionario[color] > cantidad_veces_max:
            maximo = color
            cantidad_veces_max = diccionario[color]

    print(f'encontre color! \n')
    return maximo


def busqueda_mayor_ocurrencia(matriz, diccionario, i, j):
    color = matriz[i][j]
    return _busqueda_mayor_ocurrencia(matriz, diccionario, i, j, color)


def _busqueda_mayor_ocurrencia(matriz, diccionario, i, j, color):
    if matriz[i][j] != color: return diccionario
    
    if matriz[i][j] != matriz[0][0]: #Compruebo no estar teniendo como posibilidad el color base
        diccionario[color] = diccionario.get(color, 0) + 1 #agrego el color y la cantidad que hay adyacentes

        if not (j + 1) == len(matriz[0]):
            _busqueda_mayor_ocurrencia(matriz, diccionario, i, j+1, color) #Busco si esta ese mismo color a su derecha

        if not (i + 1) == len(matriz):
            _busqueda_mayor_ocurrencia(matriz, diccionario, i+1, j, color) #Busco si esta ese mismo color a su izquierda
        
        return diccionario #Para este punto ya puedo devolver el diccionario

    if not (j + 1) == len(matriz[0]): #Busco un slot mas a la derecha del actual
        color = matriz[i][j+1]
        _busqueda_mayor_ocurrencia(matriz, diccionario, i, j+1, color)

    if not (i + 1) == len(matriz): #Busco un slot mas abajo del actual
        color = matriz[i+1][j]
        _busqueda_mayor_ocurrencia(matriz, diccionario, i+1, j, color)


def busqueda_mejor_mov(matriz):
    colores = {} #creo un diccionario donde se guardan todos los colores y sus ocurrencias entre ellos
    i = 0
    j = 0
    busqueda_mayor_ocurrencia(matriz, colores, i, j+1) #Arranco a buscar por derecha
    busqueda_mayor_ocurrencia(matriz, colores, i+1, j) #Arranco a buscar por debajo

    return encontrar_max(colores)


def matriz_completa(matriz):
    return recorrer_matriz_recur(matriz)


def clonar(matriz):
    copia = []
    for fila in matriz:
        copia.append(fila.copy())
    return copia


class JuegoFlood:
    """
    Clase para administrar un Flood, junto con sus estados y acciones
    """

    def __init__(self, alto, ancho, n_colores):
        """
        Genera un nuevo JuegoFlood, el cual tiene un Flood y otros
        atributos para realizar las distintas acciones del juego.

        Argumentos:
            alto, ancho (int): Tamaño de la grilla del Flood.
            n_colores: Cantidad maxima de colores a incluir en la grilla.
        """
        self.flood = Flood(alto, ancho) 
        self.flood.mezclar_tablero(n_colores) 
        self.pasos_solucion = Cola() 
        self.mejor_n_movimientos, _ = self._calcular_movimientos() 
        self.n_movimientos = 0 
        

        # Parte 3: Agregar atributos a la clase...
        self.clon = self.flood.clonar() # Busco el tablero original 
        self.pila_rehacer = Pila() 
        self.pila_deshacer = Pila() 
        self.pila_aux = Pila()
        self.puede_rehacer = False 
        self.primer_deshacer = True


    def cambiar_color(self, color):
        """
        Realiza la acción para seleccionar un color en el Flood, sumando a la
        cantidad de movimientos realizados y manejando las estructuras para
        deshacer y rehacer

        Argumentos:
            color (int): Nuevo color a seleccionar
        """
        # Parte 3: Modificar el código... 
        
        self.pila_deshacer.apilar(self.flood.clonar())

        self.flood.cambiar_color(color)
        
        self.pila_aux.apilar(self.flood.clonar()) #Agrego el cambio a esta pila para luego comparar si son el mismo flood

        if self.pila_aux.ver_tope() == self.pila_deshacer.ver_tope(): #Comparo para descartar en el caso de que sea el mismo para no tener repetidos ni sumar movs
            self.pila_deshacer.desapilar()
            self.n_movimientos -= 1

        self.n_movimientos += 1

        if not self.pila_rehacer.esta_vacia() and not verificar_existencia(copiar_pila(self.pila_deshacer), self.flood.clonar()):
            self.pila_rehacer = Pila() 

        self.puede_rehacer = False
        self.primer_deshacer = True

        if not self.pasos_solucion.esta_vacia() and self.pasos_solucion.ver_frente() == color: 
            self.pasos_solucion.desencolar() 
        else: 
            self.pasos_solucion = Cola() 
            

    def deshacer(self):
        """
        Deshace el ultimo movimiento realizado si existen pasos previos,
        manejando las estructuras para deshacer y rehacer.
        """
        # Parte 3: cambiar el `return` por tu código...
        if self.pila_deshacer.esta_vacia(): return 

        if self.primer_deshacer: # Verifico que es el primer dehacer para apilar el flood actual
            self.pila_deshacer.apilar(self.pila_aux.ver_tope())

        self.pila_rehacer.apilar(self.pila_deshacer.desapilar()) #Le paso el tope de la pila a la pila rehacer

        if self.pila_deshacer.esta_vacia(): return #Verifico por las dudas que no este vacio para no romper el flood

        self.flood.grilla = self.pila_deshacer.ver_tope() #Cambio el flood

        self.n_movimientos -= 1

        self.puede_rehacer = True
        self.primer_deshacer = False
        self.pasos_solucion = Cola()

    
    def rehacer(self):
        """
        Rehace el movimiento que fue deshecho si existe, manejando las
        estructuras para deshacer y rehacer.
        """
        # Parte 3: cambiar el `return` por tu código...
        if self.pila_rehacer.esta_vacia() or self.puede_rehacer == False: return

        self.flood.grilla = self.pila_rehacer.ver_tope()

        self.pila_deshacer.apilar(self.pila_rehacer.desapilar())

        self.n_movimientos += 1
        self.pasos_solucion = Cola()


    def _calcular_movimientos(self):
        """
        Realiza una solución de pasos contra el Flood actual (en una Cola)
        y devuelve la cantidad de movimientos que llevó a esa solución.

        COMPLETAR CON EL CRITERIO DEL ALGORITMO DE SOLUCIÓN.

        Devuelve:
            int: Cantidad de movimientos que llevó a la solución encontrada.
            Cola: Pasos utilizados para llegar a dicha solución
        """
        # Parte 4: tu código acá...
        # self.clon = self.flood.clonar()
        # max_movimientos = 0
        # pasos_aux = Cola()

        # while not matriz_completa(self.clon):

        #     mejor_mov = busqueda_mejor_mov(self.clon)
        #     _cambiar_color(self.clon, 0, 0, mejor_mov, self.clon[0][0])
        #     max_movimientos += 1
        #     pasos_aux.encolar(mejor_mov)

        
        # return max_movimientos, pasos_aux
        return 999, Cola()


    def hay_proximo_paso(self):
        """
        Devuelve un booleano indicando si hay una solución calculada
        """
        return not self.pasos_solucion.esta_vacia()


    def proximo_paso(self):
        """
        Si hay una solución calculada, devuelve el próximo paso.
        Caso contrario devuelve ValueError

        Devuelve:
            Color del próximo paso de la solución
        """
        return self.pasos_solucion.ver_frente()


    def calcular_nueva_solucion(self):
        """
        Calcula una secuencia de pasos que solucionan el estado actual
        del flood, de tal forma que se pueda llamar al método `proximo_paso()`
        """
        _, self.pasos_solucion = self._calcular_movimientos()


    def dimensiones(self):
        return self.flood.dimensiones()


    def obtener_color(self, fil, col):
        return self.flood.obtener_color(fil, col)


    def obtener_posibles_colores(self):
        return self.flood.obtener_posibles_colores()


    def esta_completado(self):
        return self.flood.esta_completado()