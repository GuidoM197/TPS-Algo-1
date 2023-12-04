from flood import Flood, _cambiar_color
from pila import Pila
from cola import Cola

def es_adyacente_al_actual(matriz, i, j, actual):
    abajo = (i < len(matriz) - 1 and matriz[i+1][j] == actual)
    derecha = (j < len(matriz[0]) - 1 and matriz[i][j+1] == actual)
    arriba = (i > 0 and matriz[i-1][j] == actual)
    izquierda = (j > 0 and matriz[i][j-1] == actual)

    return abajo or derecha or arriba or izquierda
        

def comparar_casilleros(actual, copia):
    casilleros_diferentes = 0

    for fil in range(len(actual.grilla)):
        for col in range(len(actual.grilla[fil])):
            if copia.grilla[fil][col] != actual.grilla[fil][col]: 
                casilleros_diferentes += 1

    return casilleros_diferentes


def buscar(matriz, color_acutal):
    posibles_colores = {}

    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if matriz[i][j] != color_acutal and es_adyacente_al_actual(matriz, i, j, matriz[0][0]): 
                posibles_colores[matriz[i][j]] = posibles_colores.get(matriz[i][j], 0) + 1

    return posibles_colores


def comparacion_de_casilleros(copia, colores):
    actual = copia.clonar()
    aux = copia.clonar()
    tamaño_colores = {}

    for color in colores:
        
        _cambiar_color(aux.grilla, 0, 0, color, aux.grilla[0][0])
        _cambiar_color(aux.grilla, 0, 0, -1, aux.grilla[0][0])
        tamaño_colores[color] = tamaño_colores.get(color, 0) + comparar_casilleros(actual, aux)
        aux = actual.clonar()

    tuplas = list(tamaño_colores.items())

    max = tuplas[0]
    color_final = tuplas[0][0]

    for key, value in tuplas:
        if value > max[1]: 
            color_final = key

    return color_final


def busqueda_mejor_mov(matriz):

    colores = buscar(matriz.grilla, matriz.grilla[0][0])

    return comparacion_de_casilleros(matriz, colores)


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

        self.tablero_inicial = self.flood.clonar().grilla
        self.ultimo_flood_jugado = self.flood.clonar().grilla

        self.pila_rehacer = Pila() 
        self.pila_deshacer = Pila() 

        self.puede_rehacer = True



    def cambiar_color(self, color):
        """
        Realiza la acción para seleccionar un color en el Flood, sumando a la
        cantidad de movimientos realizados y manejando las estructuras para
        deshacer y rehacer

        Argumentos:
            color (int): Nuevo color a seleccionar
        """
        # Parte 3: Modificar el código... 

        anterior = self.flood.clonar().grilla

        self.pila_deshacer.apilar(anterior)

        self.flood.cambiar_color(color)


        if self.flood.grilla == self.pila_deshacer.ver_tope(): #Comparo para descartar en el caso de que sea el mismo para no tener repetidos ni sumar movs
            self.pila_deshacer.desapilar()
            self.n_movimientos -= 1


        if not self.pasos_solucion.esta_vacia() and self.pasos_solucion.ver_frente() == color: 
            self.pasos_solucion.desencolar() 

        else: 
            self.pasos_solucion = Cola() 

        self.pila_rehacer = Pila() #Por cada mov pila_rehacer se reinicia
        self.puede_rehacer = False
        self.n_movimientos += 1 
            

    def deshacer(self):
        """
        Deshace el ultimo movimiento realizado si existen pasos previos,
        manejando las estructuras para deshacer y rehacer.
        """
        # Parte 3: cambiar el `return` por tu código...
        if self.pila_deshacer.esta_vacia(): return 


        if self.pila_rehacer.esta_vacia():
            self.pila_rehacer.apilar(self.flood.grilla)


        if self.pila_deshacer.ver_tope() == self.flood.grilla:
            self.pila_deshacer.desapilar()
        

        if not self.pila_deshacer.esta_vacia():
            
            self.flood.grilla = self.pila_deshacer.ver_tope()
            self.pila_rehacer.apilar(self.pila_deshacer.desapilar())

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

        
        if self.pila_deshacer.esta_vacia():
            self.pila_deshacer.apilar(self.flood.grilla)
        

        if self.pila_rehacer.ver_tope() == self.flood.grilla:
            self.pila_deshacer.apilar(self.pila_rehacer.desapilar())


        if self.pila_rehacer.ver_tope() == self.tablero_inicial:
            self.pila_deshacer.apilar(self.pila_rehacer.desapilar())
        

        if not self.pila_rehacer.esta_vacia():
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
        #Parte 4: tu código acá...
        copia = self.flood.clonar()
        max_movimientos = 0
        pasos_aux = Cola()

        while not copia.esta_completado():

            mejor_mov = busqueda_mejor_mov(copia)
            _cambiar_color(copia.grilla, 0, 0, mejor_mov, copia.grilla[0][0])
            max_movimientos += 1
            pasos_aux.encolar(mejor_mov)

        
        return max_movimientos, pasos_aux


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
