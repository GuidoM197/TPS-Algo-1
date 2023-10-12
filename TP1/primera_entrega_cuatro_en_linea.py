from typing import List

#A partir de aca, comienzan las funciones auxiliares que fueron implementadas.

def verificar_contiguos(lista, ficha):

    for i in range(len(lista)):
        if i+3>len(lista)-1:
            break
        if son_cuatro_contiguos(lista, i, ficha):
            return True
        
    return False

def son_cuatro_contiguos(lista, i, ficha):
    return lista[i] == ficha and lista[i+1] == ficha and lista[i+2] == ficha and lista[i+3] == ficha    

#Esta funcion verifica si hay algun ganador horizontal
def obtener_ganador_horizontal(tablero, gano):

    for fila in range(len(tablero)):
        for _ in range(len(tablero[fila])):
            if verificar_contiguos(tablero[fila], "X"):
                    gano = "X"
                    return gano
            elif verificar_contiguos(tablero[fila], "O"):
                    gano = "O"
                    return gano
    return gano

#Esta funcion verifica si hay algun ganador vertical
def obtener_ganador_vertical(tablero, gano):

    for col in range(len(tablero[0])):
        list_temp = []
        for fil in range(len(tablero)):
            list_temp.append(tablero[fil][col])
            if verificar_contiguos(list_temp, "X"):
                gano = "X"
                break
            if verificar_contiguos(list_temp, "O"):
                gano = "O"
                break
    return gano

#Verifica si son contiguos en la diagonal
def verificar_contiguos_diagonales(lista, ficha):

    for j in range(len(lista)):
        for i in range(len(lista[j])):
            if i+3>len(lista[j])-1: 
                break
            if son_cuatro_contiguos_diagonales(lista, i, j, ficha): 
                return True
            
    return False

#Funcion auxiliar para verificar si son contiguos en la diagonal
def son_cuatro_contiguos_diagonales(lista, i, j, ficha):
    return lista[j][i] == ficha and lista[j][i+1] == ficha and lista[j][i+2] == ficha and lista[j][i+3] == ficha

#Esta funcion verifica las diagonales superiores de una matriz ( de dercha a izquierda ) 
def diagonales_superiores(tablero, list_diagonales):
    
    for i in range(len(tablero[0])): 
        aux = []
        filas = 0
        columnas = i

        while filas < len(tablero) and columnas >= 0: 
            aux.append(tablero[filas][columnas])
            filas += 1
            columnas -= 1                             
        list_diagonales.append(aux)

    return list_diagonales

#Esta funcion verifica las diagonales inferiores de una matriz ( de derecha a izquierda )
def diagonales_inferiores(tablero, list_diagonales):

    for i in range(0, len(tablero)):
        aux = []
        filas = i
        columnas = len(tablero[0]) - 1

        while filas < len(tablero) and columnas >= 0:
            aux.append(tablero[filas][columnas])
            filas += 1
            columnas -= 1
        list_diagonales.append(aux)

    return list_diagonales

#Esta funcion verificar las diagonales superiores comenzando en el centro de una matriz en el sentido inverso( de izquierda a derecha ) 
def diagonales_inferior_invertidas(tablero, list_diagonales):

    for col in range(len(tablero[0])-1, -1, -1):
        diagonales = []
        filas = 0
        columnas = col

        while filas < len(tablero) and columnas >= 0 and columnas < len(tablero[0]):
            diagonales.append(tablero[filas][columnas])
            filas += 1
            columnas += 1
        list_diagonales.append(diagonales)

    return list_diagonales

#Esta funcion verificar las diagonales inferiores comenzando en la esquina superior derecha de una matriz en el sentido inverso( de izquierda a derecha ) 
def diagonales_superior_invertidas(tablero, list_diagonales):

    for fila in range(len(tablero)):

        for col in range(len(tablero[0])-1,-1,-1):
            auxx = []
            fil = fila

            while fil <= len(tablero)-1 and col <= len(tablero[0])- 1: 
                auxx.append(tablero[fil][col])
                col += 1
                fil += 1

        list_diagonales.append(auxx)

    return list_diagonales

def obtener_ganador_diagonal(tablero, gano):
    
    todas_las_diagonales = []

    """
    Se verifican todas las diagonales de la matriz y las guardan en la lista 
    "todas_las_diagonales" para luego podes verificar si hay algun 4 en linea
    """
    diagonales_superiores(tablero, todas_las_diagonales)
    diagonales_inferiores(tablero, todas_las_diagonales)
    diagonales_superior_invertidas(tablero, todas_las_diagonales)
    diagonales_inferior_invertidas(tablero, todas_las_diagonales)

    if verificar_contiguos_diagonales(todas_las_diagonales, "X"):
        gano = "X"
    elif verificar_contiguos_diagonales(todas_las_diagonales, "O"):
        gano = "O"

    return gano

def validacion_de_tablero(filas, columnas):
    if str(filas).isdigit() and str(columnas).isdigit():
        return 4 <= int(filas) <= 10 and 4 <= int(columnas) <= 10

#A partir de esta parte estan las funciones generales.

def crear_tablero(n_filas: int, n_columnas: int) -> List[List[str]]:
    """Crea un nuevo tablero de cuatro en línea, con dimensiones
    n_filas por n_columnas.
    Para todo el módulo `cuatro_en_linea`, las cadenas reconocidas para los
    valores de la lista de listas son las siguientes:
        - Celda vacía: ' '
        - Celda con símbolo X: 'X'
        - Celda con símbolo O: 'O'

    PRECONDICIONES:
        - n_filas y n_columnas son enteros positivos mayores a tres.

    POSTCONDICIONES:
        - la función devuelve un nuevo tablero lleno de casilleros vacíos
          que se puede utilizar para llamar al resto de las funciones del
          módulo."""

    if validacion_de_tablero(n_filas, n_columnas):
        tablero = []
        for _ in range(int(n_filas)):
            aux = [] 
            for _ in range(int(n_columnas)):
                aux.append(" ")
            tablero.append(aux)
        return tablero

def es_turno_de_x(tablero: List[List[str]]) -> bool:
    """Dado un tablero, devuelve True si el próximo turno es de X. Si, en caso
    contrario, es el turno de O, devuelve False.
    - Dado un tablero vacío, dicha función debería devolver `True`, pues el
      primer símbolo a insertar es X.
    - Luego de insertar el primer símbolo, esta función debería devolver `False`
      pues el próximo símbolo a insertar es O.
    - Luego de insertar el segundo símbolo, esta función debería devolver `True`
      pues el próximo símbolo a insertar es X.
    - ¿Qué debería devolver si hay tres símbolos en el tablero? ¿Y con cuatro
      símbolos?

    PRECONDICIONES:
        - el parámetro `tablero` fue inicializado con la función `crear_tablero`
        - los símbolos del tablero fueron insertados previamente insertados con
          la función `insertar_simbolo`"""
    
    count_x = 0
    count_o = 0

    """Revisa todo el tablero y hace un recuento de X y O para verificar quien fue el ultimo jugador."""
    for fil in range(len(tablero)):
        for col in range(len(tablero[fil])):
            if tablero[fil][col] == "X":
                count_x += 1

    for fil in range(len(tablero)):
        for col in range(len(tablero[fil])):
            if tablero[fil][col] == "O":
                count_o += 1

    """Despues de revisar el tablero pregunta si hay mas X que O, en ese caso devuelve False, en el caso de que sean iguales devuelve True."""
    if count_x > count_o:
        print(f"Juega O, ingrese una columna del 0 al " + str(len(tablero[0])-1) + ": ")
        return False
    elif count_x == count_o:
        print(f"Juega X, ingrese una columna del 0 al " + str(len(tablero[0])-1) + ": ")
        return True

def insertar_simbolo(tablero: list[list[str]], columna: int) -> bool:

    """Dado un tablero y un índice de columna, se intenta colocar el símbolo del
    turno actual en dicha columna.
    Un símbolo solo se puede colocar si el número de columna indicada por
    parámetro es válido, y si queda espacio en dicha columna.
    El número de la columna se encuentra indexado en 0, entonces `0` corresponde
    a la primer columna.

    PRECONDICIONES:
        - el parámetro `tablero` fue inicializado con la función `crear_tablero`
    POSTCONDICIONES:
        - si la función devolvió `True`, se modificó el contenido del parámetro
          `tablero`. Caso contrario, el parámetro `tablero` no se vio modificado
    """

    """Primero revisa si el valor esta dentro del rango del tablero, si no es asi devuelve False, 
    en el de que si este en el rango, revisa toda la columna desde la ultima fila a la primera y si 
    encuentra un espacio "vacio" devuelve True, en el caso que todos ya esten ocupados devuelven False"""

    ultima_fila = []
    count_x = 0
    count_o = 0

    if not str(columna).isdigit() or not 0 <= int(columna) < len(tablero[0]):
        return False
    
    """Revisa si la ultima fila esta vacia, en ese caso devuelve True ya que juega X."""
    for i in range(len(tablero[0])):
        if tablero[len(tablero)-1][i] == " ":
            ultima_fila.append(tablero[len(tablero)-1][i])  
            
    """Revisa todo el tablero y hace un recuento de X y O para verificar quien fue el ultimo jugador."""
    for fil in range(len(tablero)):
        for col in range(len(tablero[fil])):
            if tablero[fil][col] == "X":
                count_x += 1

    for fil in range(len(tablero)):
        for col in range(len(tablero[fil])):
            if tablero[fil][col] == "O":
                count_o += 1

    for fila in range(len(tablero)-1,-1,-1):
        
        if ultima_fila == tablero[fila]:
            tablero[fila][int(columna)] = "X"
            return True

        if count_x > count_o and tablero[fila][int(columna)] == " ":
            tablero[fila][int(columna)] = "O"
            return True
        
        elif count_x == count_o and tablero[fila][int(columna)] == " ":
            tablero[fila][int(columna)] = "X"
            return True
        
    return False

def tablero_completo(tablero: List[List[str]]) -> bool:
    """Dado un tablero, indica si se encuentra completo. Un tablero se considera
    completo cuando no hay más espacio para insertar un nuevo símbolo, en tal
    caso la función devuelve `True`.

    PRECONDICIONES:
        - el parámetro `tablero` fue inicializado con la función `crear_tablero`
    """

    tablero_lleno = []

    for columna in range(len(tablero[0])):
        tablero_lleno.append(tablero[0][columna])
    if not " " in tablero_lleno:
        return True
    return False

def obtener_ganador(tablero: List[List[str]]) -> str:
    """Dado un tablero, devuelve el símbolo que ganó el juego.
    El símbolo ganador estará dado por aquel que tenga un cuatro en línea. Es
    decir, por aquel símbolo que cuente con cuatro casilleros consecutivos
    alineados de forma horizontal, vertical, o diagonal.
    En el caso que el juego no tenga ganador, devuelve el símbolo vacío.
    En el caso que ambos símbolos cumplan con la condición de cuatro en línea,
    la función devuelve cualquiera de los dos.

    PRECONDICIONES:
        - el parámetro `tablero` fue inicializado con la función `crear_tablero`

    EJEMPLO: para el siguiente tablero, el ganador es 'X' por tener un cuatro en
    línea en diagonal
        [
            [' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', 'X', 'O', ' ', ' ', ' '],
            [' ', ' ', 'O', 'X', ' ', ' ', ' '],
            [' ', ' ', 'X', 'O', 'X', ' ', ' '],
            [' ', 'O', 'O', 'X', 'X', 'X', 'O'],
        ]
    """

    ganador = " "

    if obtener_ganador_horizontal(tablero, ganador) == "X":
        return "X"
    elif obtener_ganador_horizontal(tablero, ganador) == "O":
        return "O"
    elif obtener_ganador_vertical(tablero, ganador) == "X":
        return "X"
    elif obtener_ganador_vertical(tablero, ganador) == "O":
        return "O"
    elif obtener_ganador_diagonal(tablero, ganador) == "X":
        return "X"
    elif obtener_ganador_diagonal(tablero, ganador) == "O":
        return "O"

    return ganador

def graficar_tablero(tablero):

    indices = []
    separacion = "".ljust(len(tablero[0])*2, "_") + "_"

    for i in range(len(tablero[0])):
        indices.append(str(i))
    print("")

    print("|" + "|".join(indices) + "|")

    print(separacion)

    print("")

    for i in range(len(tablero)):
        print("|" + "|".join(tablero[i]) + "|")
