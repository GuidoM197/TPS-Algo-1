import random

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
        self.grilla = []


        for _ in range(self.alto):
            aux = [] 
            for _ in range(self.ancho):
                aux.append("0")
            self.grilla.append(aux)
        
    def __len__(self): return self.alto
    
    def __str__(self): return f'{self.grilla}'

    def mezclar_tablero(self, n_colores):
        """
        Asigna de forma completamente aleatoria hasta `n_colores` a lo largo de
        las casillas del tablero.

        Argumentos:
            n_colores (int): Cantidad maxima de colores a incluir en la grilla.
        """
        # Parte 1: Cambiar el `raise` por tu código...
        self.colores = 0
        for fila in range(len(self.grilla)):

            for col in range(len(self.grilla[0])):
                color = random.randint(0, n_colores)
                self.grilla[fila][col] = color

                if color > self.colores: self.colores = color


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
        _cambiar_color(self.grilla, 0, 0, color_nuevo, anterior)


    def clonar(self):
        """
        Devuelve:
            Flood: Copia del Flood actual
        """
        # Parte 3: Tu código acá...
        fil, col = self.dimensiones()

        copia = Flood(fil, col)

        copia.grilla = []

        for fila in self.grilla:
            aux = []
            for columna in fila:
                aux.append(columna)
            copia.grilla.append(aux)
            
        return copia


    def esta_completado(self):
        """
        Indica si todas las coordenadas de grilla tienen el mismo color

        Devuelve:
            bool: True si toda la grilla tiene el mismo color
        """
        # Parte 4: Tu código acá...

        for i in self.grilla:
            for j in i:
                if j != self.grilla[0][0]: return False
        return True

