import random

def _cambiar_color(matriz, i, j, color_nuevo, anterior):
    if i == len(matriz) or matriz[i][j] != anterior: return

    if matriz[i][j] == anterior and j < len(matriz[0]): 
        matriz[i][j] = color_nuevo 

        if (j + 1) == len(matriz[0]): 
            return _cambiar_color(matriz, i+1, 0, color_nuevo, anterior)

        _cambiar_color(matriz, i, j+1, color_nuevo, anterior)

    return _cambiar_color(matriz, i+1, 0, color_nuevo, anterior)

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
        self.largo = 0
        self.alto = alto
        self.ancho = ancho
        self.grilla = []

        for _ in range(self.alto):
            aux = []
            self.largo += 1
            for _ in range(self.ancho):
                aux.append("0")
            self.grilla.append(aux)

    def __len__(self): return self.largo
    
    def __str__(self): return f'{self.grilla}'
    
    def mezclar_tablero(self, n_colores):
        """
        Asigna de forma completamente aleatoria hasta `n_colores` a lo largo de
        las casillas del tablero.

        Argumentos:
            n_colores (int): Cantidad maxima de colores a incluir en la grilla.
        """
        # Parte 1: Cambiar el `raise` por tu código...
        for fila in range(len(self.grilla)):
            for col in range(len(self.grilla[0])):
                color = random.randint(0, n_colores)
                self.grilla[fila][col] = color

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





juego = Flood(4,4)
juego.mezclar_tablero(5)
print(len(juego))