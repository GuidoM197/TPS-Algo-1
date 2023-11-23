import random
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
    copia = pila
    act = copia.ver_tope()

    while not copia.esta_vacia():
        if act == movimiento: return True
        act = copia.desapilar()
    
    return False


def _cambiar_color(matriz, i, j, color_nuevo, anterior):
    if i == len(matriz) or matriz[i][j] == color_nuevo: return

    if matriz[i][j] == anterior and j < len(matriz[0]): 
        matriz[i][j] = color_nuevo  
        
        if not (j + 1) == len(matriz[0]):
            _cambiar_color(matriz, i, j+1, color_nuevo, anterior)
        if j > 0:
            _cambiar_color(matriz, i, j-1, color_nuevo, anterior)
        if i > 0:
            _cambiar_color(matriz, i-1, j, color_nuevo, anterior)

        _cambiar_color(matriz, i+1, j, color_nuevo, anterior)

def contar_colores(contador, n_colores):
    for _ in n_colores:
        contador += 1
    return contador

class Flood:
    """
    Clase para administrar un tablero de N colores.
    """

    def __init__(self, alto, ancho):
        """
        Genera un nuevo Flood de un mismo color con las dimensiones dadas.

        Argumentos:
            alto, ancho (int): Tamaño de la grilla.
        """
        # Parte 1: Cambiar el `raise` por tu código...
        self.alto = alto
        self.ancho = ancho
        self.colores = 0
        self.grilla =  [[0,1,1,0],
                        [0,2,1,2],
                        [0,1,2,2],
                        [0,1,1,2],]

        # for _ in range(self.alto):
        #     aux = [] 
        #     for _ in range(self.ancho):
        #         aux.append("0")
        #     self.grilla.append(aux)
        
    def __len__(self): return self.alto
    
    def __str__(self): return f'{self.grilla}'

    # def mezclar_tablero(self, n_colores):
    #     """
    #     Asigna de forma completamente aleatoria hasta `n_colores` a lo largo de
    #     las casillas del tablero.

    #     Argumentos:
    #         n_colores (int): Cantidad maxima de colores a incluir en la grilla.
    #     """
    #     # Parte 1: Cambiar el `raise` por tu código...
    #     self.colores = 0
    #     for fila in range(len(self.grilla)):

    #         for col in range(len(self.grilla[0])):
    #             color = random.randint(0, n_colores)
    #             self.grilla[fila][col] = color

    #             if color > self.colores: self.colores = color


    def obtener_color(self, fil, col):
        """
        Devuelve el color que se encuentra en las coordenadas solicitadas.

        Argumentos:
            fil, col (int): Posiciones de la fila y columna en la grilla.

        Devuelve:
            Color asignado.
        """
        # Parte 1: Cambiar el `raise` por tu código...
        return self.grilla[fil][col]
    

    def obtener_posibles_colores(self):
        """
        Devuelve una secuencia ordenada de todos los colores posibles del juego.
        La secuencia tendrá todos los colores posibles que fueron utilizados
        para generar el tablero, sin importar cuántos de estos colores queden
        actualmente en el tablero.

        Devuelve:
            iterable: secuencia ordenada de colores.
        """
        # Parte 1: Cambiar el `raise` por tu código...
        return [x for x in range(self.colores + 1)]


    def dimensiones(self):
        """
        Dimensiones de la grilla (filas y columnas)

        Devuelve:
            (int, int): alto y ancho de la grilla en ese orden.
        """
        # Parte 1: Cambiar el `raise` por tu código...
        return len(self.grilla), len(self.grilla[0])


    def cambiar_color(self, color_nuevo):
        """
        Asigna el nuevo color al Flood de la grilla. Es decir, a todas las
        coordenadas que formen un camino continuo del mismo color comenzando
        desde la coordenada origen en (0, 0) se les asignará `color_nuevo`

        Argumentos:
            color_nuevo: Valor del nuevo color a asignar al Flood.
        """
        # Parte 2: Tu código acá...
        anterior = self.grilla[0][0]
        return _cambiar_color(self.grilla, 0, 0, color_nuevo, anterior)


    def clonar(self):
        """
        Devuelve:
            Flood: Copia del Flood actual
        """
        # Parte 3: Tu código acá...
        copia = []
        for fila in self.grilla:
            copia.append(fila.copy())
        return copia


    def esta_completado(self):
        """
        Indica si todas las coordenadas de grilla tienen el mismo color

        Devuelve:
            bool: True si toda la grilla tiene el mismo color
        """
        # Parte 4: Tu código acá...
        return False


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
        #self.flood.mezclar_tablero(n_colores)
        #self.mejor_n_movimientos, _ = self._calcular_movimientos()
        self.n_movimientos = 0
        self.pasos_solucion = Cola()

        # Parte 3: Agregar atributos a la clase...
        self.clon = self.flood.clonar() # Busco el tablero original
        self.pila_rehacer = Pila() 
        self.pila_deshacer = Pila() 
        self.puede_rehacer = False


    def cambiar_color(self, color):
        """
        Realiza la acción para seleccionar un color en el Flood, sumando a la
        cantidad de movimientos realizados y manejando las estructuras para
        deshacer y rehacer

        Argumentos:
            color (int): Nuevo color a seleccionar
        """
        # Parte 3: Modificar el código... 

        self.n_movimientos += 1

        self.pila_deshacer.apilar(self.flood.clonar())

        self.flood.cambiar_color(color)

        movimiento_actual = self.flood.clonar()

        if not self.pila_rehacer.esta_vacia() and not verificar_existencia(copiar_pila(self.pila_deshacer), movimiento_actual):
            self.pila_rehacer = Pila()
            print(f'Deshacer despues del nuevo mov: {self.pila_deshacer} \n')
            print(f'Rehacer despues del nuevo mov: {self.pila_rehacer} \n')

        self.puede_rehacer = False


    def deshacer(self):
        """
        Deshace el ultimo movimiento realizado si existen pasos previos,
        manejando las estructuras para deshacer y rehacer.
        """
        # Parte 3: cambiar el `return` por tu código...
        if self.pila_deshacer.esta_vacia(): return 

        ultimo_deshecho = self.pila_deshacer.ver_tope()

        print(f'Deshacer antes: {self.pila_deshacer} \n')

        self.flood.grilla = self.pila_deshacer.ver_tope()

        self.pila_rehacer.apilar(self.pila_deshacer.desapilar())

        print(f'Deshacer despues: {self.pila_deshacer} \n')

        self.puede_rehacer = True
        self.n_movimientos -= 1
        self.pasos_solucion = Cola()

    
    def rehacer(self):
        """
        Rehace el movimiento que fue deshecho si existe, manejando las
        estructuras para deshacer y rehacer.
        """
        # Parte 3: cambiar el `return` por tu código...
        if self.pila_rehacer.esta_vacia() or self.puede_rehacer == False: return

        print(f'Rehacer antes: {self.pila_rehacer} \n')

        self.flood.grilla = self.pila_rehacer.ver_tope()

        self.pila_deshacer.apilar(self.pila_rehacer.desapilar())

        print(f'Rehacer despues: {self.pila_rehacer} \n')

        self.n_movimientos += 1
        self.pasos_solucion = Cola()

    def __str__(self): return f'{self.flood}'


def main():

    # juego = Flood(4,4)
    # juego.mezclar_tablero(5)
    # print(juego)
    # juego.cambiar_color(1)
    # print(juego)
    juegoflood = JuegoFlood(4, 4, 5)

    m = [[0,1,1,0],
         [0,2,1,2],
         [0,1,2,2],
         [0,1,1,2],]
    
    print(juegoflood)

    juegoflood.cambiar_color(1)
    juegoflood.cambiar_color(2)
    juegoflood.cambiar_color(0)

    juegoflood.deshacer()
    juegoflood.deshacer()

    juegoflood.rehacer()
    juegoflood.rehacer()

    juegoflood.deshacer()

    juegoflood.cambiar_color(3)

    juegoflood.rehacer()

main()