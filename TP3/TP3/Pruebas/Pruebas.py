import random
from cola import Cola
from pila import Pila

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


def recorrer_matriz_recur(matriz):
    color_actual = matriz[0][0]
    return _recorrer_matriz_recu(matriz, 0, 0, color_actual)


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


def _recorrer_matriz_recu(matriz, i, j, color_actual):
    if i == len(matriz): return True

    if j == len(matriz[0]):
        return _recorrer_matriz_recu(matriz, i+1, 0, color_actual)

    if i < len(matriz) and j < len(matriz[0]): 
        if matriz[i][j] != color_actual: return False

    return _recorrer_matriz_recu(matriz, i, j+1, color_actual)


def cambiar_color(matriz, color_nuevo):
    """
    Asigna el nuevo color al Flood de la grilla. Es decir, a todas las
    coordenadas que formen un camino continuo del mismo color comenzando
    desde la coordenada origen en (0, 0) se les asignará `color_nuevo`

    Argumentos:
        color_nuevo: Valor del nuevo color a asignar al Flood.
    """
    # Parte 2: Tu código acá...
    anterior = matriz[0][0]
    return _cambiar_color(matriz, 0, 0, color_nuevo, anterior)


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
    
    return 999, Cola()


def encontrar_max(diccionario):
    maximo = 0
    cantidad_veces_max = 0

    for color in diccionario:
        if diccionario[color] > cantidad_veces_max:
            maximo = color
            cantidad_veces_max = diccionario[color]

    return maximo


def busqueda_mayor_ocurrencia_por_debajo(matriz, diccionario, i, j):
    color = matriz[i][j]

    while color == matriz[0][0] and (i + 1) < len(matriz):
        i += 1
        color = matriz[i][j]
    
    if color == matriz[0][0]:
        while color == matriz[0][0] and (j + 1) < len(matriz[0]):
            j += 1
            color = matriz[i][j]
            if color != matriz[0][0]:
                return _busqueda_mayor_ocurrencia_fondo_abajo(matriz, diccionario, i, j, color)
            
    return _busqueda_mayor_ocurrencia(matriz, diccionario, i, j, color)


def busqueda_mayor_ocurrencia_por_derecha(matriz, diccionario, i, j):
    color = matriz[i][j]

    while color == matriz[0][0] and (j + 1) < len(matriz[0]):
        j += 1
        color = matriz[i][j]
    
    if color == matriz[0][0]:
        while color == matriz[0][0] and (i + 1) < len(matriz):
            i += 1
            color = matriz[i][j]
            if color != matriz[0][0]:
                return _busqueda_mayor_ocurrencia_fondo_abajo(matriz, diccionario, i, j, color)
            
    return _busqueda_mayor_ocurrencia(matriz, diccionario, i, j, color)


def _busqueda_mayor_ocurrencia(matriz, diccionario, i, j, color):
    if matriz[i][j] != color: return diccionario

    if matriz[i][j] != matriz[0][0]:
        diccionario[color] = diccionario.get(color, 0) + 1

        if not (j + 1) == len(matriz[0]):
            _busqueda_mayor_ocurrencia(matriz, diccionario, i, j+1, color)

        if not (i + 1) == len(matriz):
            _busqueda_mayor_ocurrencia(matriz, diccionario, i+1, j, color)

        return diccionario



def _busqueda_mayor_ocurrencia_fondo_der(matriz, diccionario, i, j, color):
    if matriz[i][j] != color: return diccionario

    if matriz[i][j] != matriz[0][0]:
        diccionario[color] = diccionario.get(color, 0) + 1

        if not (j - 1) <= 0:
            _busqueda_mayor_ocurrencia_fondo_der(matriz, diccionario, i, j-1, color)

        if not (i + 1) == len(matriz):
            _busqueda_mayor_ocurrencia_fondo_der(matriz, diccionario, i+1, j, color)

        return diccionario


def _busqueda_mayor_ocurrencia_fondo_abajo(matriz, diccionario, i, j, color):
    if matriz[i][j] != color: return diccionario

    if matriz[i][j] != matriz[0][0]:
        diccionario[color] = diccionario.get(color, 0) + 1

        if not (j + 1) == len(matriz[0]):
            _busqueda_mayor_ocurrencia_fondo_abajo(matriz, diccionario, i, j+1, color)

        if not (i - 1) <= 0:
            _busqueda_mayor_ocurrencia_fondo_abajo(matriz, diccionario, i-1, j, color)

        return diccionario











def busqueda_mayor_ocurrencia_iterativo_emi(matriz):
    colores = {}
    maximo = 0
    mas_repeticiones = 0
    
    for fil in matriz:
        for col in fil:
            colores[col] = colores.get(col, 0) + 1
    
    for color in colores:
        if mas_repeticiones < colores[color]:
            maximo = color
            mas_repeticiones = colores[color]
    
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

    if not (j + 1) == len(matriz[0]): #Si llego hasta acá significa que matriz[i][j] es igual a matriz[0][0], entonces busco un slot a la derecha
        color = matriz[i][j+1]
        _busqueda_mayor_ocurrencia(matriz, diccionario, i, j+1, color)

    if not (i + 1) == len(matriz): #Si llego hasta acá significa que matriz[i][j] es igual a matriz[0][0], entonces busco un slot por debajo
        color = matriz[i+1][j]
        _busqueda_mayor_ocurrencia(matriz, diccionario, i+1, j, color)


def esta_completado(matriz): #Bool
    """
    Indica si todas las coordenadas de grilla tienen el mismo color

    Devuelve:
        bool: True si toda la grilla tiene el mismo color
    """
    # Parte 4: Tu código acá...
    return recorrer_matriz_recur(matriz)


def clonar(matriz):
    """
    Devuelve:
        Flood: Copia del Flood actual
    """
    # Parte 3: Tu código acá...
    copia = []
    for fila in matriz:
        copia.append(fila.copy())
    return copia


def solucion(copia):
    max_movimientos = 0
    pasos_aux = Cola()

    while not esta_completado(copia):
        colores = {}

        mejor_mov = busqueda_mayor_ocurrencia(copia, colores, 0, 0)
        _cambiar_color(copia, 0, 0, mejor_mov, copia[0][0])
        max_movimientos += 1
        pasos_aux.encolar(mejor_mov)
    
    return max_movimientos, pasos_aux


matriz = [[1,0,1,2],
         [2,0,2,1],
         [2,0,1,3],
         [1,4,4,4]]

# copia_matriz = clonar(matriz)

# cant, pasos = solucion(copia_matriz)

# print(cant)
# print(pasos)

p1 = Pila()
p1.apilar(1)
p1.apilar(2)
p1.apilar(3)
p1.apilar(4)
p1.apilar(5)

p2 = Pila()
p2.apilar(2)
p2.apilar(3)
p2.apilar(2)
p2.apilar(6)



